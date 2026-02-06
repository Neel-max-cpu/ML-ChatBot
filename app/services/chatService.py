from app.core.intentClassifier import detect_intent
from app.core.vectorStore import search_similar, KNOWLEDGE, extract_code, get_value
from app.services.actionRouter import route_action
from app.store.contextStore import get_context, update_context


def return_message(message: str, session_id="default"):
    intent = detect_intent(message)
    code = extract_code(message)

    # for in memory context --- TODO -- HERE ALL USER SHARE SAME MEMORY(CHANGE IT)
    context = get_context(session_id)

    if code:
        match = get_value(code)
    else:
        matches = search_similar(message)
        match = matches[0] if matches else None

    # if the chatbot doesn't understand what the user said fall back to the previous one ---
    if not match and "entity" in context:
        match = context["entity"]

    if not match:
        return {
            "reply": "I couldn't identify what you are referring to!"
        }

    # update context
    update_context(session_id, entity=match, intent=intent)
    reply = route_action(intent, match)

    return {
        "intent": intent.value if hasattr(intent, "value") else intent,
        "entity": match["entity_type"],
        "entityCode": match["entity_code"],
        "reply": reply
    }
