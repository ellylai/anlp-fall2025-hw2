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
import faiss

def embedding(encoder, docs):
    return encoder.encode(docs, convert_to_numpy=True)

def process_data(docs):
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedding(encoder, docs)
    idxs = faiss(embeddings)
    return idxs, encoder

def build_database(embs):
    d = embs[0].shape
    database = faiss.IndexFlatL2(d)
    database.add(embs)
    return database

def search_data(q_emb, data, k):
    docs = data.search(q_emb, k)
    return docs

def dense_retriever(query, data, encoder):
    q_emb = embedding(encoder, [query])
    docs = search_data(q_emb, data, k=60)
    return docs