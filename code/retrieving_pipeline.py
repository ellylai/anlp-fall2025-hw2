"""
Document retriever (implement sparse, dense and hybrid retrieval)
Hybrid Retrieval: Implement a system that combines dense (vector-based) and sparse (keyword-based) 
retrieval
"""
from retrievers.dense import dense_retriever as dense
from retrievers.sparse import sparse_retriever as sparse
from retrievers.hybrid import hybrid_retriever as hybrid

def main():
    pass

def retrieval(type, query):
    if type == "dense":
        data = None # TODO: get appropriate database
        dense(query, data)
    elif type == "sparse":
        sparse(query)
    else:
        hybrid(query)