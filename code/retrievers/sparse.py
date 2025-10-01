"""
Sparse Retrieval: Integrate BM25 into your pipeline. You can use existing BM25 implementations,
limited to bm25s or rank-bm25, or build your own implementation if you wish to do so.

Citation: used https://github.com/xhluca/bm25s
"""

import bm25s

# INCOMPLETE


def sparse_retriever_corpus(corpus):
    corpus_tokens = bm25s.tokenize(corpus, stopwords="en")
    retriever = bm25s.BM25()
    retriever.index(corpus_tokens)
    retriever.save("retriever")


def sparse_retriever(query):
    query_tokens = bm25s.tokenize(query)

    retriever = bm25s.BM25.load("retriever", load_corpus=True)

    results, scores = retriever.retrieve(query_tokens, k=2)
    for i in range(results.shape[1]):
        doc, score = results[0, i], scores[0, i]
        print(f"Rank {i+1} (score: {score:.2f}): {doc}")
