from dense import dense_retriever
from sparse import sparse_retriever
'''
Combination Strategy: Implement at least one established method for combining dense and sparse 
retrieval results. Common approaches include score normalization and weighted averaging, rank-based 
fusion methods (like Reciprocal Rank Fusion), using one method to filter or re-rank results from the 
other, or other ensemble techniques found in the literature. Experiment with different combination 
strategies to see which works best for your dataset.
'''

def retrieve(query):
    dense = dense_retriever(query)
    sparse = sparse_retriever(query)
    return dense, sparse

def preprocess(d_rank, s_rank):
    pass

def rrf_fusion(ranks, k):
    scores = {}
    for d, r in ranks:
        scores[d] = 1.0 / (k+r)
    return scores

def rankings(scores):
    docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [d for (d, r) in docs]

def hybrid_retriever(query):
    d, s = retrieve(query)
    ranked = preprocess(d, s)
    scores = rrf_fusion(ranked, k=60)
    docs = rankings(scores)
    return docs