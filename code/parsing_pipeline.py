# 1. html_parser: use links in google doc to scrape for all subpages and pdfs
# parent page and subpage links go in html_links.json
# pdfs go in a folder in pdfs_and_html_links
# use links in html_links.json to convert to plain text (put in a folder)
# 2. pdf_parser: use downloaded pdf files to convert to plain text (put in a folder)
# 3. document chunking
# 4. embedding: sentenceBERT
from parsers.html_parser import parse_html_links
from parsers.pdf_parser import convert_pdf_to_plaintext


def main():
    links = []
    with open("pdfs_and_html_links/html_links_parent.txt", "r", encoding="utf-8") as f:
        for line in f:
            links.append(line.strip("\n"))
    # parse links + html pages
    pdf_links = parse_html_links(links)
    print(pdf_links)
    # parse pdfs
    convert_pdf_to_plaintext(pdf_links, write=True)
    # chunk docs
    # embed docs + store in vector database
    # pass off to retriever


if __name__ == "__main__":
    main()
