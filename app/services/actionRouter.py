from app.core.intent import Intent
from app.services.responseGenerator import human_reply

"""
def route_action(intent: Intent, entity: dict) -> str:
    # entity = {
    #     'entity_type': 'LABOUR',
    #     'entity_code': 'LAB001',
    #     'text': 'LAB001 is a brake inspection labour task'
    # }
   
    if intent == Intent.VIEW:
        return handle_view(entity)

    if intent == Intent.EDIT:
        return handle_edit(entity)

    if intent == Intent.CREATE:
        return handle_create(entity)

    if intent == Intent.LIST:
        return handle_list(entity)

    if intent == Intent.HELP:
        return handle_help(entity)

    return "I'm not sure what you want to do. Can you rephrase?"

def handle_view(entity: dict) -> str:
    return (
        f"{entity['text']}.\n\n"
        f"You can:\n"
        f"• Edit this {entity['entity_type'].lower()}\n"
        f"• View related records\n"
        f"• Go back to the list"
    )


def handle_edit(entity: dict) -> str:
    return (
        f"To edit {entity['entity_code']}:\n\n"
        f"Go to:\n"
        f"Home → {entity['entity_type'].title()} → Search → "
        f"Select {entity['entity_code']} → Edit"
    )


def handle_create(entity: dict) -> str:
    return (
        f"To create a new {entity['entity_type'].lower()}:\n\n"
        f"Go to:\n"
        f"Home → {entity['entity_type'].title()} → Create\n\n"
        f"Fill the required details and save."
    )


def handle_list(entity: dict) -> str:
    return (
        f"To view the list of {entity['entity_type'].lower()} records:\n\n"
        f"Go to:\n"
        f"Home → {entity['entity_type'].title()} → Search"
    )


def handle_help(entity: dict) -> str:
    return (
        "You can ask things like:\n"
        "• What is LAB001?\n"
        "• Edit LAB001\n"
        "• Create new labour\n"
        "• Show labour list"
    )
"""
def route_action(intent, match):
    intro = human_reply(intent, match)
    code = match["entity_code"]
    etype = match["entity_type"]

    if intent == "EDIT":
        return (
            f"{intro}\n\n"
            f"Go to:\n"
            f"Home → {etype.title()} → Search → Select {code} → Edit"
        )

    if intent == "VIEW":
        return (
            f"{intro}\n\n"
            f"{match['text']}"
        )

    if intent == "CREATE":
        return (
            f"{intro}\n\n"
            f"Go to:\n"
            f"Home → {etype.title()} → Create New"
        )

    if intent == "LIST":
        return (
            f"{intro}\n\n"
            f"Go to:\n"
            f"Home → {etype.title()} → Search"
        )

    return "I’m not sure what action to take."
