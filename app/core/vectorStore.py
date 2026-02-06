from typing import Dict, List
import faiss
import numpy as np
import re

from app.core.embeddings import embed_text
from app.services.knowledgeService import fetch_knowledge

# Demo domain knowledge
"""
KNOWLEDGE = [
    {
        "id": "LAB001",
        "type": "LABOUR",
        "text": "LAB001 Brake inspection labour task"
    },
    {
        "id": "VIN001",
        "type": "VEHICLE",
        "text": "VIN001 Tata Nexon vehicle"
    },
    {
        "id": "WB001",
        "type": "WASHING_BAY",
        "text": "WB001 Washing bay for vehicle cleaning"
    },
    {
        "id": "IB001",
        "type": "INSPECTION_BAY",
        "text": "IB001 Inspection bay for diagnostics"
    }
]

# Build index
embeddings = np.array([embed_text(item["text"]) for item in KNOWLEDGE]).astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

"""
#
# index = None
# KNOWLEDGE: List[Dict]=[]
#
# def build_index():
#     global index, KNOWLEDGE
#
#     # Step 1: fetch from MSSQL
#     KNOWLEDGE = get_chat_knowledge()
#
#     if not KNOWLEDGE:
#         print("⚠️ No chat knowledge found in DB")
#         return
#
#     # Step 2: embed all texts
#     texts = [item["text"] for item in KNOWLEDGE]
#     embeddings = np.array([embed_text(t) for t in texts]).astype("float32")
#
#     # Step 3: build FAISS index
#     index = faiss.IndexFlatL2(embeddings.shape[1])
#     index.add(embeddings)
#
#     print(f"✅ FAISS index built with {len(KNOWLEDGE)} records")
#
#
#
# # query - what use said , and top_k = how many similar things we want back (currently 1 best match)
# def search_similar(query: str, top_k=1):
#     if index is None:
#         raise RuntimeError("Vector index not initialized")
#     """
#     query = "show me LAB001"  and embed_text(query) return [0.023, -0.112, 0.998, ...]  ← 384 numbers
#     but we wrap it in [embed_text(query)] since FAISS(Fast vector search) expects 2d array so becomes
#     [[0.023, -0.112, 0.998, ...]] 1 vector 384 dimensions and .astype("float32") cause FAISS need float32 not python 32
#     """
#
#     # Step 1: embed query
#     query_vector = np.array([embed_text(query)]).astype("float32")
#     # Step 2: search top_k closest embeddings
#     distances, indices = index.search(query_vector, top_k)
#
#     # Step 3: fetch original knowledge
#     results = []
#     for idx in indices[0]:
#         results.append(KNOWLEDGE[idx])
#
#     return results



KNOWLEDGE: List[Dict]=[]
index = None
def build_index():
    global index, KNOWLEDGE
    # Load knowledge from DB
    KNOWLEDGE = fetch_knowledge()
    print("KNOWLEDGE: ", KNOWLEDGE)

    if not KNOWLEDGE:
        raise RuntimeError("No knowledge loaded from database")


    # Create embeddings
    # Build index
    embeddings = np.array([
        embed_text(item["text"]) for item in KNOWLEDGE
    ]).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

def extract_code(message: str):
    match = re.search(r"\bLAB\d{4}\b", message.upper())
    return match.group(0) if match else None

def get_value(code):
    for item in KNOWLEDGE:
        if item["entity_code"] == code:
            return item
    return None


def search_similar(query: str, top_k=1, max_distance=1.2):
    query_vector = np.array([embed_text(query)]).astype("float32")
    distances, indices = index.search(query_vector, top_k)

    results = []
    for i,idx in enumerate(indices[0]):
        dist = distances[0][i]

        # distance check confidence threshold 0.8
        if dist > max_distance:
            continue
        results.append(KNOWLEDGE[idx])

    return results