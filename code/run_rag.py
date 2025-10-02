import argparse
from parsing_pipeline import main as doc_parser
from retrieving_pipeline import retrieval
from generating_pipeline import reader

def terminal_io():
    parser = argparse.ArgumentParser()
    parser.add_argument('--retrieval_type', type=str, default="dense", help="dense, sparse, or hybrid")
    parser.add_argument('--query', type=str, default="dense", help="dense, sparse, or hybrid")
    args = parser.parse_args()
    return args.retrieval_type, args.query

def main():
    retrieval_type, query = terminal_io()
    doc_parser()
    docs = retrieval(query, retrieval_type)
    response = reader(query, docs)
    # TODO: output response