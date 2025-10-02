import argparse
from parsing_pipeline import main as doc_parser
from retrieving_pipeline import retrieval
from generating_pipeline import reader
from retrievers.dense import build_database
from output import write_outfile

def terminal_io():
    parser = argparse.ArgumentParser()
    parser.add_argument('--retrieval_type', type=str, default="dense", help="dense, sparse, or hybrid")
    parser.add_argument('--queries', type=str, help="Path to queries file")
    parser.add_argument('--outfile', type=str, default="Path to outfile")
    args = parser.parse_args()
    return args.retrieval_type, args.queries, args.outfile

def main():
    retrieval_type, queries, outfile = terminal_io()
    doc_parser()
    doc_chunks = None   # TODO: import doc chunks
    vec_data = build_database(doc_chunks)
    responses = []
    for query in queries:
        docs = retrieval(retrieval_type, query, vec_data)
        response = reader(query, docs)
        responses.append(response)
    write_outfile(outfile, responses)