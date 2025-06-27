from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
stored_docs = []  # Store (text, embedding) pairs

def add_document(text: str):
    emb = model.encode(text)
    stored_docs.append((text, emb))

def semantic_search(query: str, top_k: int = 3):
    query_emb = model.encode(query)
    results = sorted(
        stored_docs,
        key=lambda x: util.cos_sim(x[1], query_emb),
        reverse=True
    )
    return [doc[0] for doc in results[:top_k]]
