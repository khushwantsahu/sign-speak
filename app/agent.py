# ruff: noqa
# SignSpeak — Multi-Agent ADK 2.0 Workflow
# ─────────────────────────────────────────────────────────

from __future__ import annotations

import json
import logging
import re
from collections.abc import AsyncGenerator
from typing import Any

from google.adk import Workflow
from google.adk.agents import LlmAgent
from google.adk.agents.context import Context
from google.adk.events.request_input import RequestInput
from google.adk.tools import AgentTool
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset, StdioConnectionParams
from google.adk.workflow import START, node

from google.adk.apps import App

from .config import config

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────
# Sub-Agents (specialists called via AgentTool)
# ─────────────────────────────────────────────────────────

# MCP toolset shared by specialist agents (stdio transport to local mcp_server.py)
_mcp_params = StdioConnectionParams(
    server_params={
        "command": "uv",
        "args": ["run", "python", "-m", "app.mcp_server"],
    }
)
_mcp_toolset = McpToolset(connection_params=_mcp_params)

gesture_coach = LlmAgent(
    name="gesture_coach",
    model=config.model,
    description="Expert on individual sign language hand shapes, fingerspelling, and manual alphabet.",
    instruction="""You are an encouraging and precise Sign Language Gesture Coach.

Your role:
- Teach individual letter signs, numbers, and basic static hand shapes.
- Describe how to perform gestures clearly, detailing hand orientation and position.
- **VISUAL GUIDES**: Always use matching hand emojis (like ✊ for a, ✋ for b, ✌️ for v, ☝️ for d, 🤙 for y, 🤟 for i-love-you, 🤏 or 🤌 for pinches) to visually represent the hand shape.
- Draw simple finger diagrams or ASCII representations (e.g. [||||] ✊) where helpful to illustrate finger extension/curl.
- Use the get_gesture_description tool to retrieve official descriptions of letters/words.
- CRITICAL: You MUST include the exact visual placeholders (e.g., [VISUAL: a]) and video placeholders (e.g., [VIDEO: alphabet]) returned by the get_gesture_description tool verbatim in your response. Do not modify, omit, or summarize them away. Do NOT generate or look up external image URLs yourself.
- Provide step-by-step guidance and mnemonic suggestions.
- Keep explanations simple and structured.

Always end with one quick tip for hand flexibility or posture.
""",
    tools=[_mcp_toolset],
)

phrase_coach = LlmAgent(
    name="phrase_coach",
    model=config.model,
    description="Expert on American Sign Language (ASL) grammar, common greetings, sentence construction, and word order.",
    instruction="""You are a helpful and knowledgeable Sign Language Phrase Coach.

Your role:
- Teach common signs/words and full phrases (e.g., greetings, questions, basic conversational phrases).
- **VISUAL GUIDES**: Use greeting, hand, and facial expression emojis (like 👋, 🙏, 🤝, 😊, 😮) to highlight gestures and non-manual markers (facial expressions).
- Explain key grammatical differences between ASL and English (e.g., Topic-Comment structure, time-first rule).
- Explain non-manual markers (facial expressions, body shifts).
- Use the sign_dictionary_search tool to look up how to sign specific terms/phrases.
- CRITICAL: You MUST include any visual placeholders (e.g., [VISUAL: a]) and video placeholders (e.g., [VIDEO: greetings]) returned by the tools verbatim in your response. Do not modify, omit, or summarize them away. Do NOT generate or look up external image URLs yourself.
- Guide users on combining signs to form complete sentences.

Always end with a simple conversational prompt for the user to try signing.
""",
    tools=[_mcp_toolset],
)

practice_partner = LlmAgent(
    name="practice_partner",
    model=config.model,
    description="Interactive practice partner that designs drills, gives memory aid mnemonics, and reviews user description.",
    instruction="""You are a friendly Sign Language Practice Partner.

Your role:
- Help users review what they learned by providing quizzes, translation exercises, and fingerspelling drills.
- **VISUAL GUIDES**: Incorporate visual hand shape emojis and quiz symbols (e.g. 📝, ❓, ✊, ✋, 🤟) to make exercises highly engaging and intuitive.
- Use the mnemonic_generator tool to create clever association rules for remembering specific signs/letters.
- Use the practice_quiz tool to generate exercises for the user's level (beginner/intermediate).
- CRITICAL: You MUST include any placeholders (like [VISUAL: a] or [VIDEO: greetings]) returned by the tools verbatim in your response. Do not modify, omit, or summarize them away. Do NOT generate or look up external image URLs yourself.
- Provide constructive and positive feedback on user's progress.

Always end with a specific daily challenge or short practice drill.
""",
    tools=[_mcp_toolset],
)

# ─────────────────────────────────────────────────────────
# Orchestrator (delegates to specialist sub-agents via AgentTool)
# ─────────────────────────────────────────────────────────

sign_orchestrator = LlmAgent(
    name="sign_orchestrator",
    model=config.model,
    description="Orchestrating sign language tutor that routes questions to specialized coaches.",
    instruction="""You are the SignSpeak Orchestrator.

The user's topic of interest is stored in the session state. Your job is to:
1. Determine what the user wants to focus on (letters/gestures, phrases/grammar, or practice/quizzes).
2. Delegate to the correct specialist sub-agent using these tools:
   - gesture_coach     → hand shapes, individual letters, fingerspelling
   - phrase_coach      → complete words/phrases, grammar, syntax, conversational phrases
   - practice_partner   → quizzes, drills, mnemonics, active review
3. Synthesize the sub-agent's response into a supportive, clear reply.
   CRITICAL: You MUST preserve and include the full detailed response generated by the specialist sub-agent (including all step-by-step descriptions, mnemonics, [VISUAL: <letter>] placeholders, and [VIDEO: <category>] placeholders) in your final response verbatim. Never omit, truncate, modify, or summarize away the placeholders or instructions returned by the sub-agents.
4. If a query covers multiple areas (e.g., learning a phrase and practicing it), call the appropriate sub-agents in sequence.
5. Greet the user warmly and guide them on their sign language learning journey.

IMPORTANT: Always use the specialist sub-agent tools to construct the final response rather than answering directly.
""",
    tools=[
        AgentTool(agent=gesture_coach),
        AgentTool(agent=phrase_coach),
        AgentTool(agent=practice_partner),
    ],
)

# ─────────────────────────────────────────────────────────
# Workflow Function Nodes
# ─────────────────────────────────────────────────────────

@node
async def security_checkpoint(ctx: Context, node_input: Any) -> AsyncGenerator[Any, None]:
    """Security checkpoint: PII scrubbing, prompt injection detection, audit logging."""
    raw_text = ""
    if isinstance(node_input, str):
        raw_text = node_input
    elif isinstance(node_input, dict):
        raw_text = json.dumps(node_input)
    elif node_input is not None:
        raw_text = str(node_input)

    # ── PII Scrubbing ──────────────────────────────────────
    pii_patterns = {
        "ssn":          r"\b\d{3}-\d{2}-\d{4}\b",
        "credit_card":  r"\b(?:\d{4}[- ]?){3}\d{4}\b",
        "bank_account": r"\b\d{8,17}\b",
        "email":        r"\b[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}\b",
        "phone":        r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b",
    }
    scrubbed = raw_text
    found_pii: list[str] = []
    if config.pii_redaction_enabled:
        for pii_type, pattern in pii_patterns.items():
            if re.search(pattern, scrubbed):
                found_pii.append(pii_type)
                scrubbed = re.sub(pattern, f"[REDACTED_{pii_type.upper()}]", scrubbed)

    # ── Prompt Injection Detection ─────────────────────────
    injection_keywords = [
        "ignore previous instructions",
        "ignore all instructions",
        "disregard your instructions",
        "you are now",
        "forget your role",
        "system prompt",
        "jailbreak",
        "act as",
        "pretend you are",
        "bypass",
        "override",
    ]
    is_injection = False
    if config.injection_detection_enabled:
        lower_text = scrubbed.lower()
        is_injection = any(kw in lower_text for kw in injection_keywords)

    # ── Domain Rule: block inappropriate or offensive content requests ──
    offensive_keywords = [
        "profanity",
        "swear words",
        "curse signs",
        "hate speech",
    ]
    is_offensive_request = any(kw in scrubbed.lower() for kw in offensive_keywords)

    # ── Structured Audit Log ───────────────────────────────
    severity = "INFO"
    event_type = "REQUEST_RECEIVED"
    route = "ok"

    if found_pii:
        severity = "WARNING"
        event_type = "PII_DETECTED_AND_SCRUBBED"

    if is_injection or is_offensive_request:
        severity = "CRITICAL"
        event_type = "SECURITY_EVENT_BLOCKED"
        route = "SECURITY_EVENT"

    audit_log = {
        "event_type": event_type,
        "severity": severity,
        "pii_found": found_pii,
        "injection_detected": is_injection,
        "offensive_request_detected": is_offensive_request,
        "input_length": len(raw_text),
        "scrubbed": bool(found_pii),
    }
    logger.info("[AUDIT] %s", json.dumps(audit_log))

    # Store in session state
    ctx.state["scrubbed_input"] = scrubbed
    ctx.state["security_route"] = route
    ctx.state["audit_log"] = audit_log

    # Set route so Workflow edges can branch
    ctx.route = route  # type: ignore[attr-defined]

    yield

@node(rerun_on_resume=True)
async def topic_collector(ctx: Context, node_input: Any) -> AsyncGenerator[Any, None]:
    """HITL: Ask the user what aspect of sign language they want to learn."""
    # 1. If we already have a topic saved in the session state, pass through.
    if ctx.state.get("user_topic"):
        yield
        return

    # 2. Auto-detect from input
    scrubbed_input = ctx.state.get("scrubbed_input", "")
    lower_input = scrubbed_input.lower()

    detected_topic = None
    if any(k in lower_input for k in ["letter", "gesture", "alphabet", "fingerspell", "handshape", "hand shape"]):
        detected_topic = "Gestures"
    elif any(k in lower_input for k in ["phrase", "sentence", "grammar", "greeting", "conversation", "sign"]):
        detected_topic = "Phrases"
    elif any(k in lower_input for k in ["quiz", "test", "practice", "drill", "mnemonic", "review"]):
        detected_topic = "Practice"

    if detected_topic:
        ctx.state["user_topic"] = detected_topic
        logger.info("[HITL] Auto-detected topic: %s", detected_topic)
        yield
        return

    # 3. Check for resume input
    resume = ctx.resume_inputs.get("sign_speak_topic_prompt")
    if resume is not None:
        topic = resume.get("result", resume) if isinstance(resume, dict) else str(resume)
        ctx.state["user_topic"] = topic
        logger.info("[HITL] User selected topic: %s", topic)
        yield
        return

    # 4. Prompt user
    yield RequestInput(
        interrupt_id="sign_speak_topic_prompt",
        message=(
            "Welcome to SignSpeak! 🤟\n\n"
            "What would you like to focus on today?\n"
            "  • **Gestures** — Learn individual letters (fingerspelling) & static hand shapes\n"
            "  • **Phrases** — Learn words, phrases, greetings & ASL grammar structure\n"
            "  • **Practice** — Quiz your knowledge and practice with custom drills\n\n"
            "Type your topic preference or ask a specific question:"
        ),
        response_schema={"type": "string"},
    )

@node
async def security_blocked_output(ctx: Context, node_input: Any) -> AsyncGenerator[Any, None]:
    """Terminal node for security block."""
    audit = ctx.state.get("audit_log", {})
    reason = "prompt injection attempt" if audit.get("injection_detected") else \
              "inappropriate content request" if audit.get("offensive_request_detected") else \
              "security policy violation"
    ctx.state["final_response"] = (
        f"⚠️ Your request was blocked due to a {reason}. "
        "Please rephrase your request and try again."
    )
    yield

# ─────────────────────────────────────────────────────────
# Visual Renderer Node
# ─────────────────────────────────────────────────────────

@node
async def visual_renderer(ctx: Context, node_input: Any) -> AsyncGenerator[Any, None]:
    """Replaces placeholders like [VISUAL: a] and [VIDEO: alphabet] with base64 img tags and YouTube links."""
    import re
    from app.visual_assets import VISUALS

    text = ""
    if isinstance(node_input, str):
        text = node_input
    elif hasattr(node_input, "text"):
        text = node_input.text
    else:
        text = ctx.state.get("final_response", "")

    # 1. Replace [VISUAL: x] placeholders with local relative URL image tags
    def replace_visual(match):
        char = match.group(1).lower()
        # Since we copied all 26 letters to the browser assets folder, they are available under /dev-ui/assets/gestures/
        return f'<img src="/dev-ui/assets/gestures/{char}.png?v=3" alt="Gesture {char.upper()}" width="320" />'

    text = re.sub(r"\[VISUAL:\s*([a-zA-Z])\]", replace_visual, text)

    # 2. Replace [VIDEO: x] placeholders with YouTube links
    def replace_video(match):
        cat = match.group(1).lower()
        if cat == "alphabet":
            return "[Watch ASL Alphabet Tutorial on YouTube](https://www.youtube.com/watch?v=ianCxd71xzA)"
        elif cat == "greetings":
            return "[Watch Basic ASL Greetings Tutorial on YouTube](https://www.youtube.com/watch?v=0FcwzMq4iWo)"
        return "[Video Link]"

    text = re.sub(r"\[VIDEO:\s*([a-zA-Z]+)\]", replace_video, text)

    # 3. Always append a general YouTube video reference at the end of tutor sessions
    general_links = (
        "\n\n---\n"
        "📺 **ASL Learning Resources:**\n"
        "- Learn fingerspelling: [ASL Alphabet Tutorial on YouTube](https://www.youtube.com/watch?v=ianCxd71xzA)\n"
        "- Learn greetings: [Basic ASL Greetings Tutorial on YouTube](https://www.youtube.com/watch?v=0FcwzMq4iWo)"
    )
    if "Watch ASL Alphabet" not in text and "Watch Basic ASL Greetings" not in text and "ASL Learning Resources" not in text:
        text += general_links

    ctx.state["final_response"] = text
    yield text

# ─────────────────────────────────────────────────────────
# Workflow Graph
# ─────────────────────────────────────────────────────────

root_agent = Workflow(
    name="sign_speak_workflow",
    description="SignSpeak — Interactive Sign Language and Fingerspelling Tutor.",
    edges=[
        ("START", security_checkpoint),
        (security_checkpoint, {"SECURITY_EVENT": security_blocked_output, "ok": topic_collector}),
        (topic_collector, sign_orchestrator),
        (sign_orchestrator, visual_renderer),
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
