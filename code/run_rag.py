import argparse
from parsing_pipeline import main as doc_parser
from retrieving_pipeline import retrieval

def terminal_io():
    parser = argparse.ArgumentParser()
    parser.add_argument('--retrieval_type', type=str, default="dense", help="dense, sparse, or hybrid")
    args = parser.parse_args()
    return args.retrieval_type

def main():
    retrieval_type = terminal_io()
    doc_parser()
    retrieval(retrieval_type)
    # TODO: CONTINUE