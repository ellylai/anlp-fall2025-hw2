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

def get_ranking(doc, type):
    pass

def rrf_fusion(d_rank, s_rank, k):
    docs = {}
    for d, rd in d_rank:
        if (d, rs) in s_rank:
            docs[d] = 1.0 / (k + rd) + 1.0 / (k + rs)
        else:
            docs[d] = 1.0 / (k + rd) + 1.0 / (k + get_ranking(d, "sparse"))
    for d, rs in s_rank:
        if d not in docs:
            docs[d] = 1.0 / (k + rs) + 1.0 / (k + get_ranking(d, "dense"))
    return docs

def rankings(scores):
    docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [d for (d, _) in docs]

def hybrid_retriever(query):
    d, s = retrieve(query)
    scores = rrf_fusion(d, s, k=60)
    docs = rankings(scores)
    return docs