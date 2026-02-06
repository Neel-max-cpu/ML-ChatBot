# contextStore.py
from typing import Dict

# key = session_id (for now: client IP or dummy)
SESSION_CONTEXT: Dict[str, Dict] = {}

def get_context(session_id: str) -> Dict:
    return SESSION_CONTEXT.get(session_id, {})

def update_context(session_id: str, entity=None, intent=None):
    ctx = SESSION_CONTEXT.get(session_id, {})
    if entity:
        ctx["entity"] = entity
    if intent:
        ctx["intent"] = intent
    SESSION_CONTEXT[session_id] = ctx
