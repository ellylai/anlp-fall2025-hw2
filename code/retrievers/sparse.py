"""
Sparse Retrieval: Integrate BM25 into your pipeline. You can use existing BM25 implementations,
limited to bm25s or rank-bm25, or build your own implementation if you wish to do so.

Citation: used https://github.com/xhluca/bm25s
"""

import bm25s


def sparse_retriever_corpus(path: str, chunk_size: int):
    with open(path, "r", encoding="utf-8") as f:
        corpus = [line.strip() for line in f if line.strip()]

    corpus_tokens = bm25s.tokenize(corpus, stopwords="en")
    retriever = bm25s.BM25()
    retriever.index(corpus_tokens)

    type = path.split("_")[-2]
    retriever.save(
        f"sparse_retriever_indexes/retriever_index_{type}_size{chunk_size}",
        corpus=corpus,
    )


def sparse_retriever(query, doctype, chunk_size, k=2):
    query_tokens = bm25s.tokenize(query, stopwords="en")
    retriever = bm25s.BM25.load(
        f"sparse_retriever_indexes/retriever_index_{doctype}_size{chunk_size}",
        load_corpus=True,
    )

    results, scores = retriever.retrieve(query_tokens, k=k)
    print(results, scores)
    return results


def load_corpus_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        corpus = [line.strip() for line in f if line.strip()]
    return corpus


if __name__ == "__main__":
    print("TEST SPARSE RETRIEVER: embedding with sparse_retriever")

    # run this from anlp-fall2025-hw2 folder
    for chunk_size in [30, 50, 100, 150, 200]:
        sparse_retriever_corpus(
            path=f"data/all_chunks_html_size{chunk_size}.txt", chunk_size=chunk_size
        )
        sparse_retriever_corpus(
            path=f"data/all_chunks_pdfs_size{chunk_size}.txt", chunk_size=chunk_size
        )

        query = "What year was CMU founded?"
        sparse_retriever(query, doctype="html", chunk_size=chunk_size, k=2)

        query = "What is Pittsburgh's football team named?"
        sparse_retriever(query, doctype="pdfs", chunk_size=chunk_size, k=2)
