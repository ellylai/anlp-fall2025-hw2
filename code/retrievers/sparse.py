'''
Sparse Retrieval: Integrate BM25 into your pipeline. You can use existing BM25 implementations, 
limited to bm25s or rank-bm25, or build your own implementation if you wish to do so.

Citation: used https://github.com/xhluca/bm25s 
'''

import bm25s

def sparse_retriever(corpus):
    corpus_tokens = bm25s.tokenize(corpus, stopwords = "en")
    
    retriever = bm25s.BM25()
    retriever.index(corpus_tokens)
    
    retriever.save("retriever")
    
    