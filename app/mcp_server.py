"""
sign-speak MCP Server
Sign-language domain tools exposed via MCP stdio transport.

Tools:
  1. get_gesture_description - Steps to perform a sign/gesture for a specific letter/word
  2. sign_dictionary_search - Search the sign language dictionary
  3. mnemonic_generator     - Generate a memory aid mnemonic for a sign
  4. practice_quiz          - Generate practice quizzes and exercises
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sign-speak-mcp")

# Mini-database of sign descriptions and mnemonics
SIGN_DATABASE = {
    "a": {
        "description": "Make a fist with your dominant hand. Keep your fingers curled tightly into your palm, and place your thumb straight up against the side of your index finger. ✊",
        "mnemonic": "Imagine your thumb is a flagpole resting against a closed building (fist).",
        "category": "alphabet",
        "visual": "![Gesture A](file:///d:/learn/5%20day/adk-workspace1/sign-speak/assets/gestures/a.png)",
    },
    "b": {
        "description": "Open your hand with all four fingers pointing straight up, pressed close together. Tuck your thumb across your palm, resting near the base of your little finger. ✋",
        "mnemonic": "Think of a flat wall (4 fingers up) with a closed door latch (thumb tucked). Looks like a capital 'B' if you squint!",
        "category": "alphabet",
        "visual": "![Gesture B](file:///d:/learn/5%20day/adk-workspace1/sign-speak/assets/gestures/b.png)",
    },
    "c": {
        "description": "Curve your four fingers and thumb into a C-shape. Your palm faces to the side, and your hand looks like the letter 'C' from the side view. 🫴",
        "mnemonic": "Simply form the shape of the letter 'C' with your hand.",
        "category": "alphabet",
        "visual": "![Gesture C](file:///d:/learn/5%20day/adk-workspace1/sign-speak/assets/gestures/c.png)",
    },
    "hello": {
        "description": "Bring your dominant hand up near your forehead, palm facing down and slightly out. Move the hand outward and slightly down, similar to a military salute but friendlier. 👋",
        "mnemonic": "A polite forehead salute to greet someone.",
        "category": "greetings",
    },
    "thank you": {
        "description": "Touch the fingertips of your open dominant hand to your chin. Move your hand outward and down toward the person you are thanking, palm facing up. 🫴",
        "mnemonic": "Sending a warm kiss or appreciation from your chin directly to the other person.",
        "category": "greetings",
    },
    "please": {
        "description": "Place your flat dominant hand on the center of your chest. Move your hand in a circular motion clockwise (from your right to left, up, and around) several times. 🫱",
        "mnemonic": "Polishing your heart to show you are sincere and polite.",
        "category": "greetings",
    },
    "family": {
        "description": "Form 'F' hands (thumb and index finger touching in a circle, other three fingers up) with both hands. Start with your thumbs/index fingers touching in front of you, then circle both hands outward and back until your pinky fingers touch. 👪",
        "mnemonic": "Creating a circle of 'F' (Family) members starting from the center out.",
        "category": "nouns",
    },
    "friend": {
        "description": "Hook your dominant index finger over your non-dominant index finger. Then reverse the gesture, hooking your non-dominant index finger over your non-dominant index finger. 🤞",
        "mnemonic": "Two fingers locking together in a strong hug of mutual trust.",
        "category": "nouns",
    },
    "help": {
        "description": "Place your closed non-dominant hand flat, palm facing up. Place your dominant hand in a fist with thumb up (like a thumbs-up) on top of the flat palm. Lift both hands up together. 👍 flat on 🫱",
        "mnemonic": "Your flat hand is a platform lifting up and supporting (helping) the other hand.",
        "category": "verbs",
    },
}

# ─────────────────────────────────────────────────────────
# Tool 1 — Get Gesture Description
# ─────────────────────────────────────────────────────────
@mcp.tool()
async def get_gesture_description(term: str) -> str:
    """Get the step-by-step description of how to perform a sign/gesture for a specific letter or word.

    Args:
        term: The letter or word to look up (e.g. 'a', 'hello', 'please').

    Returns:
        Detailed step-by-step description of the gesture.
    """
    clean_term = term.strip().lower()
    if clean_term in SIGN_DATABASE:
        data = SIGN_DATABASE[clean_term]
        visual_str = f"\n\n**Visual Reference:**\n{data['visual']}" if "visual" in data else ""
        return (
            f"🤟 **Sign Description for '{term.upper()}'** ({data['category']}):\n"
            f"{data['description']}{visual_str}"
        )
    else:
        return (
            f"Sorry, I don't have a specific description for '{term}' in my local database. "
            f"Try checking letters like 'A', 'B', 'C', or words like 'hello', 'please', 'thank you', 'friend', 'family', 'help'."
        )

# ─────────────────────────────────────────────────────────
# Tool 2 — Sign Dictionary Search
# ─────────────────────────────────────────────────────────
@mcp.tool()
async def sign_dictionary_search(query: str) -> str:
    """Search the sign language dictionary for terms matching a query.

    Args:
        query: The search term or category to search for (e.g. 'greet', 'noun', 'a').

    Returns:
        A list of matching terms with short summaries.
    """
    clean_query = query.strip().lower()
    matches = []
    for term, data in SIGN_DATABASE.items():
        if (
            clean_query in term
            or clean_query in data["category"]
            or clean_query in data["description"].lower()
        ):
            matches.append(term)

    if matches:
        lines = [f"🔍 Found {len(matches)} matching term(s) in dictionary:"]
        for match in sorted(matches):
            data = SIGN_DATABASE[match]
            lines.append(f"  • **{match.upper()}** ({data['category']}): {data['description'][:80]}...")
        return "\n".join(lines)
    else:
        return f"No matches found for '{query}' in the sign dictionary. Try searching for 'alphabet', 'greetings', or 'nouns'."

# ─────────────────────────────────────────────────────────
# Tool 3 — Mnemonic Generator
# ─────────────────────────────────────────────────────────
@mcp.tool()
async def mnemonic_generator(term: str) -> str:
    """Generate a helpful memory association rule (mnemonic) for remembering a specific sign.

    Args:
        term: The letter or word to generate a mnemonic for (e.g. 'b', 'please').

    Returns:
        A creative memory association tip.
    """
    clean_term = term.strip().lower()
    if clean_term in SIGN_DATABASE:
        data = SIGN_DATABASE[clean_term]
        return f"💡 **Mnemonic for '{term.upper()}':**\n{data['mnemonic']}"
    else:
        return (
            f"I don't have a saved mnemonic for '{term}', but here is a general tip: "
            f"Try to associate the physical hand shape with a visual object that starts with that letter, "
            f"or the action of the sign with the feeling of the word."
        )

# ─────────────────────────────────────────────────────────
# Tool 4 — Practice Quiz Generator
# ─────────────────────────────────────────────────────────
@mcp.tool()
async def practice_quiz(difficulty: str, category: str = "general") -> str:
    """Generate a interactive practice quiz with questions.

    Args:
        difficulty: 'beginner' or 'intermediate'.
        category: 'alphabet', 'greetings', 'grammar', or 'general'.

    Returns:
        A formatted practice quiz with questions and a hidden answer key.
    """
    diff = difficulty.strip().lower()
    cat = category.strip().lower()

    if diff == "beginner":
        if cat == "alphabet":
            return (
                "📝 **Beginner Fingerspelling Quiz**\n\n"
                "1. Which letter is represented by a closed fist with the thumb straight up against the side? (Hint: Flagpole against building)\n"
                "2. When forming the letter 'B', where should your thumb be tucked?\n"
                "3. True or False: To form the letter 'C', your palm should face directly toward yourself.\n\n"
                "--- ANSWER KEY ---\n"
                "1. Letter 'A'\n"
                "2. Across the palm, near the base of the little finger\n"
                "3. False (it faces to the side so the C-shape is visible from the side)"
            )
        elif cat == "greetings":
            return (
                "📝 **Beginner Greetings Quiz**\n\n"
                "1. Which greeting is signed by touching your chin with your flat hand and moving it forward?\n"
                "2. To sign 'PLEASE', do you move your hand in a circle or back and forth?\n"
                "3. What facial expression should accompany the sign for a greeting?\n\n"
                "--- ANSWER KEY ---\n"
                "1. 'Thank you'\n"
                "2. In a circular motion clockwise\n"
                "3. A warm, welcoming smile (non-manual marker)"
            )
        else:
            return (
                "📝 **Beginner General Sign Language Quiz**\n\n"
                "1. How do you sign 'HELP' using your two hands?\n"
                "2. What is the fingerspelling sign for the letter 'C'?\n"
                "3. When signing 'FRIEND', how do your index fingers interact?\n\n"
                "--- ANSWER KEY ---\n"
                "1. Place a thumbs-up (dominant hand) on your flat open palm (non-dominant hand) and lift them together.\n"
                "2. Curve your four fingers and thumb into a C-shape.\n"
                "3. They hook over each other, first dominant over non-dominant, then reverse."
            )
    else:
        # Intermediate / Grammar
        return (
            "📝 **Intermediate ASL Grammar Quiz**\n\n"
            "1. In ASL, do you typically place time signs (like 'YESTERDAY' or 'TOMORROW') at the beginning or at the end of a sentence?\n"
            "2. Explain the difference between English word order and ASL Topic-Comment structure.\n"
            "3. How do you show a yes/no question using your eyebrows in ASL?\n\n"
            "--- ANSWER KEY ---\n"
            "1. At the beginning of the sentence (time-first rule).\n"
            "2. English uses Subject-Verb-Object (e.g. 'I bought a car'). ASL often uses Topic-Comment (e.g., 'Car, I bought').\n"
            "3. Raise your eyebrows and lean slightly forward."
        )

def main() -> None:
    mcp.run()

if __name__ == "__main__":
    main()
