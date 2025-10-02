'''
Dense Retrieval: Use embedding models to create vector representations of documents and queries. 
We recommend starting with sentence-transformers models like all-MiniLM-L6-v2 for efficiency, 
though you can experiment with other models (For guidance on selecting high-performing embedding 
models, refer to the MTEB Leaderboard) to improve performance. Use FAISS 
(https://github.com/facebookresearch/faiss) for efficient vector storage and similarity search. 
You'll need to implement the pipeline for embedding documents, building the FAISS index, and 
retrieving similar documents for queries.
'''
from sentence_transformers import SentenceTransformer

def embedding(encoder, docs):
    return encoder.encode(docs, convert_to_numpy=True)

def faiss(q_emb, embs):
    pass

def build_database(docs):
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedding(encoder, docs)
    idxs = faiss(embeddings)
    return idxs, encoder

def dense_retriever(query, data, encoder):
    q_emb = embedding(encoder, [query])
    docs = faiss(q_emb, data)
    return docs