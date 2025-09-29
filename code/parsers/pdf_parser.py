from pypdf import PdfReader


def convert_pdf_to_plaintext(pdf_links: list[str], write: bool = False):
    print(f"Parsing {len(pdf_links)} pdf links.")
    for i, link in enumerate(pdf_links):
        link = pdf_links[i]
        reader = PdfReader(link)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            full_text += text
        if write:
            with open(
                f"pdfs_and_html_links/pdfs/doc{i}.txt", "w", encoding="utf-8"
            ) as f:
                f.write(full_text)
