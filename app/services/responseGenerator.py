import random

def human_reply(intent, entity):
    code = entity["entity_code"]
    etype = entity["entity_type"]

    if intent == "VIEW":
        templates = [
            f"Here’s what I found about {code}.",
            f"{code} belongs to {etype}. Here are the details.",
            f"This is what {code} refers to."
        ]

    elif intent == "EDIT":
        templates = [
            f"Sure 👍 Let’s edit {code}.",
            f"You can update {code} by following these steps.",
            f"No problem — here’s how to modify {code}."
        ]

    elif intent == "CREATE":
        templates = [
            f"Let’s create a new {etype.lower()} 🚀",
            f"Alright, I’ll guide you through creating a {etype.lower()}.",
        ]

    elif intent == "LIST":
        templates = [
            f"Here’s how you can view all {etype.lower()}s.",
            f"You can find the list of {etype.lower()}s here.",
        ]

    else:
        templates = [
            "Got it 👍",
            "Alright!",
            "Here you go."
        ]

    return random.choice(templates)
