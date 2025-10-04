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
from sparse import load_corpus_from_file

def embedding(encoder, docs):
    embs = encoder.encode(docs, convert_to_numpy=True).astype("float32")
    ids = {i: docs[i] for i in range(len(docs))}
    return embs, ids

def process_data(path):
    docs = load_corpus_from_file(path)
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    print("Embedding data")
    embeddings, ids = embedding(encoder, docs)
    print("Building database")
    idxs = build_database(embeddings)
    return ids, idxs, encoder

def build_database(embs):
    d = embs.shape[1]
    database = faiss.IndexFlatL2(int(d))
    database.add(embs)
    return database

def search_data(q_emb, data, k):
    docs = data.search(q_emb, k)
    return docs

def dense_retriever(query, data, encoder, k):
    q_emb = encoder.encode([query], convert_to_numpy=True).astype("float32")
    docs = search_data(q_emb, data, k)
    return docs

def vec_to_text(v, ids):
    docs = []
    for i in v:
        docs.append(ids[i])
    return docs

if __name__ == "__main__":
    print("TEST DENSE RETRIEVER: embedding with sparse_retriever")

    # run this from anlp-fall2025-hw2 folder
    print("Processing data")
    ids, idxs, encoder = process_data(path="data/all_chunks.txt")
    # sparse_retriever_corpus(docs)

    query = "What year was CMU founded?"
    d, i = dense_retriever(query, idxs, encoder, k=2)
    print("i", i[0])
    print(vec_to_text(i[0], ids))

    query = "What is Pittsburgh's football team named?"
    d, i = dense_retriever(query, idxs, encoder, k=2)
    print("i", i[0])
    print(vec_to_text(i[0], ids))