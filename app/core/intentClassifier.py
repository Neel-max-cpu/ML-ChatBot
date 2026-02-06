import numpy as np
import faiss
from app.core.embeddings import embed_text
from app.core.intent import Intent

INTENT_EXAMPLES = {
    Intent.VIEW:[
        "what is LAB001",
        "show labour details",
        "explain this labour",
        "tell me about this"
    ],
    Intent.CREATE: [
        "create new labour",
        "add a labour",
        "new labour entry"
    ],
    Intent.EDIT: [
        "edit LAB001",
        "update labour",
        "modify this record"
    ],
    Intent.LIST: [
        "show all labours",
        "list labour records",
        "search labour"
    ],
    Intent.HELP: [
        "how do I do this",
        "where can I find",
        "help me"
    ]
}

texts = []
intent_map = []

for intent, examples in INTENT_EXAMPLES.items():
    for ex in examples:
        texts.append(ex)
        intent_map.append(intent)

embeddings = np.array([embed_text(t) for t in texts]).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def detect_intent(message: str) -> Intent:
    query_vector = np.array([embed_text(message)]).astype("float32")
    _, indices = index.search(query_vector, 1)
    return intent_map[indices[0][0]]