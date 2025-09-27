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

def retrieval(type):
    if type == "dense":
        dense()
    elif type == "sparse":
        sparse()
    else:
        hybrid()