# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sign-speak-mcp")

# Complete database of ASL alphabet (A-Z) and basic vocabulary
SIGN_DATABASE = {
    "a": {
        "description": "Make a fist with your dominant hand. Keep your fingers curled tightly into your palm, and place your thumb straight up against the side of your index finger. ✊",
        "mnemonic": "Imagine your thumb is a flagpole resting against a closed building (fist).",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/a.png?v=3\" alt=\"Gesture A\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "b": {
        "description": "Open your hand with all four fingers pointing straight up, pressed close together. Tuck your thumb across your palm, resting near the base of your little finger. ✋",
        "mnemonic": "Think of a flat wall (4 fingers up) with a closed door latch (thumb tucked).",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/b.png?v=3\" alt=\"Gesture B\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "c": {
        "description": "Curve your four fingers and thumb into a C-shape. Your palm faces to the side, and your hand looks like the letter 'C' from the side view. 🫴",
        "mnemonic": "Simply form the shape of the letter 'C' with your hand.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/c.png?v=3\" alt=\"Gesture C\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "d": {
        "description": "Point your index finger straight up. Touch the tips of your thumb, middle, ring, and pinky fingers together to form a circle in front of it. ☝️",
        "mnemonic": "An index finger pointing up, looking like the stem of a lowercase 'd'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/d.png?v=3\" alt=\"Gesture D\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "e": {
        "description": "Curl all four fingers tightly down so their tips rest on top of your thumb, which is folded across your palm. ✊",
        "mnemonic": "An enclosed fist where fingers curl tightly, resembling the curves of an 'E'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/e.png?v=3\" alt=\"Gesture E\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "f": {
        "description": "Touch the tip of your index finger and thumb together to form a circle. Extend your middle, ring, and pinky fingers straight up and spread them apart. 👌",
        "mnemonic": "Like the 'OK' sign, with three fingers standing up representing 'F'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/f.png?v=3\" alt=\"Gesture F\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "g": {
        "description": "Extend your index finger and thumb horizontally, parallel to each other, pointing out to the side with a small gap between them. 🤏",
        "mnemonic": "Like you are indicating a tiny amount or preparing to pinch something horizontally.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/g.png?v=3\" alt=\"Gesture G\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "h": {
        "description": "Extend your index and middle fingers straight out horizontally, pressed close together. Tuck your thumb, ring, and pinky fingers into your palm. 🫵",
        "mnemonic": "Pointing two fingers horizontally to the side to form the crossbar of 'H'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/h.png?v=3\" alt=\"Gesture H\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "i": {
        "description": "Make a fist with your dominant hand, but extend your pinky finger straight up. Keep your thumb tucked across your curled fingers. 🤙",
        "mnemonic": "A single thin pinky finger standing up like the letter 'i'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/i.png?v=3\" alt=\"Gesture I\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "j": {
        "description": "Extend your pinky finger straight up (like letter 'I') and trace the shape of a 'J' curve in the air, swooping down and up. 🤙",
        "mnemonic": "Drawing the curved tail of the letter 'J' using your pinky.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/j.png?v=3\" alt=\"Gesture J\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "k": {
        "description": "Extend your index and middle fingers straight up in a 'V' shape. Place your thumb upright so it touches the middle joint of your index finger. ✌️",
        "mnemonic": "Like a peace sign, but the thumb is tucked upright against the index finger.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/k.png?v=3\" alt=\"Gesture K\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "l": {
        "description": "Extend your index finger straight up and your thumb straight out to the side horizontally, forming an 'L' shape. Curl your other fingers. ☝️",
        "mnemonic": "Your hand literally forms the shape of a capital 'L'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/l.png?v=3\" alt=\"Gesture L\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "m": {
        "description": "Fold your thumb across your palm, and tuck it under your index, middle, and ring fingers. Curl those three fingers down over your thumb. ✊",
        "mnemonic": "Three humps of fingers (index, middle, ring) resting over the thumb, like the letter 'M'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/m.png?v=3\" alt=\"Gesture M\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "n": {
        "description": "Fold your thumb across your palm, and tuck it under your index and middle fingers. Curl those two fingers down over your thumb. ✊",
        "mnemonic": "Two humps of fingers (index, middle) resting over the thumb, like the letter 'N'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/n.png?v=3\" alt=\"Gesture N\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "o": {
        "description": "Curve all four fingers and your thumb together so their tips touch, forming a clear circle shape. 👌",
        "mnemonic": "Forming the shape of the letter 'O' with your whole hand.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/o.png?v=3\" alt=\"Gesture O\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "p": {
        "description": "Point your index finger straight out and your middle finger downward. Place your thumb against the middle joint of your middle finger (downward 'K'). ✌️",
        "mnemonic": "Like a downward-pointing 'K' shape.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/p.png?v=3\" alt=\"Gesture P\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "q": {
        "description": "Point your index finger and thumb straight down, keeping a small gap between them, resembling a downward 'G'. 🤏",
        "mnemonic": "Like a downward-pointing pinch gesture.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/q.png?v=3\" alt=\"Gesture Q\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "r": {
        "description": "Extend your index and middle fingers straight up, crossing your middle finger closely behind your index finger. ✌️",
        "mnemonic": "Crossing your fingers for good luck.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/r.png?v=3\" alt=\"Gesture R\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "s": {
        "description": "Make a tight fist with your dominant hand, and place your thumb folded across the front of all four fingers. ✊",
        "mnemonic": "A standard tight fist, with the thumb wrapping over the fingers.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/s.png?v=3\" alt=\"Gesture S\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "t": {
        "description": "Make a fist, but tuck your thumb upright between your index and middle fingers. ✊",
        "mnemonic": "Your thumb is locked in a box, peeking out between the first two fingers.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/t.png?v=3\" alt=\"Gesture T\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "u": {
        "description": "Extend your index and middle fingers straight up, pressed close together. Curl your other fingers and thumb. ✌️",
        "mnemonic": "Two fingers standing up together, forming the two sides of 'U'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/u.png?v=3\" alt=\"Gesture U\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "v": {
        "description": "Extend your index and middle fingers straight up, spread apart in a 'V' shape. Curl your other fingers. ✌️",
        "mnemonic": "A peace sign, representing the letter 'V'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/v.png?v=3\" alt=\"Gesture V\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "w": {
        "description": "Extend your index, middle, and ring fingers straight up, spread apart. Touch the tips of your thumb and pinky together. 🖐️",
        "mnemonic": "Three extended fingers forming the three peaks of a 'W'.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/w.png?v=3\" alt=\"Gesture W\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "x": {
        "description": "Make a fist, but extend your index finger straight up and bend it at the joints to form a hook shape. ☝️",
        "mnemonic": "Like a pirate's hook, representing 'X' marks the spot.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/x.png?v=3\" alt=\"Gesture X\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "y": {
        "description": "Extend your thumb and pinky finger straight out, keeping your index, middle, and ring fingers folded flat. 🤙",
        "mnemonic": "Like the 'hang loose' hand gesture.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/y.png?v=3\" alt=\"Gesture Y\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "z": {
        "description": "Point your index finger straight up and trace the shape of the letter 'Z' in the air in front of you. ☝️",
        "mnemonic": "Simply write the letter 'Z' in the air with your pointer finger.",
        "category": "alphabet",
        "visual": "<img src=\"https://raw.githubusercontent.com/khushwantsahu/sign-speak/main/assets/gestures/z.png?v=3\" alt=\"Gesture Z\" width=\"320\" />",
        "video_link": "https://www.youtube.com/watch?v=ianCxd71xzA",
    },
    "hello": {
        "description": "Bring your dominant hand up near your forehead, palm facing down and slightly out. Move the hand outward and slightly down, similar to a military salute but friendlier. 👋",
        "mnemonic": "A polite forehead salute to greet someone.",
        "category": "greetings",
        "video_link": "https://www.youtube.com/watch?v=0FcwzMq4iWo",
    },
    "thank you": {
        "description": "Touch the fingertips of your open dominant hand to your chin. Move your hand outward and down toward the person you are thanking, palm facing up. 🫴",
        "mnemonic": "Sending a warm appreciation from your chin directly to the other person.",
        "category": "greetings",
        "video_link": "https://www.youtube.com/watch?v=0FcwzMq4iWo",
    },
    "please": {
        "description": "Place your flat dominant hand on the center of your chest. Move your hand in a circular motion clockwise (from your right to left, up, and around) several times. 🫱",
        "mnemonic": "Polishing your heart to show you are sincere and polite.",
        "category": "greetings",
        "video_link": "https://www.youtube.com/watch?v=0FcwzMq4iWo",
    },
    "family": {
        "description": "Form 'F' hands (thumb and index finger touching in a circle, other three fingers up) with both hands. Start with your thumbs/index fingers touching in front of you, then circle both hands outward and back until your pinky fingers touch. 👪",
        "mnemonic": "Creating a circle of 'F' (Family) members starting from the center out.",
        "category": "nouns",
        "video_link": "https://www.youtube.com/watch?v=0FcwzMq4iWo",
    },
    "friend": {
        "description": "Hook your dominant index finger over your non-dominant index finger. Then reverse the gesture, hooking your non-dominant index finger over your non-dominant index finger. 🤞",
        "mnemonic": "Two fingers locking together in a strong hug of mutual trust.",
        "category": "nouns",
        "video_link": "https://www.youtube.com/watch?v=0FcwzMq4iWo",
    },
    "help": {
        "description": "Place your closed non-dominant hand flat, palm facing up. Place your dominant hand in a fist with thumb up (like a thumbs-up) on top of the flat palm. Lift both hands up together. 👍 flat on 🫱",
        "mnemonic": "Your flat hand is a platform lifting up and supporting (helping) the other hand.",
        "category": "verbs",
        "video_link": "https://www.youtube.com/watch?v=0FcwzMq4iWo",
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
        video_str = f"\n\n📺 **Video Tutorial:** [Watch ASL Tutorial on YouTube]({data['video_link']})" if "video_link" in data else ""
        return (
            f"🤟 **Sign Description for '{term.upper()}'** ({data['category']}):\n"
            f"{data['description']}{visual_str}{video_str}"
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
            "2. English uses Subject-Verb-Object (SVO), while ASL often uses Topic-Comment structure where the topic is introduced first, followed by the comment or action.\n"
            "3. Raise your eyebrows and lean your head slightly forward."
        )
