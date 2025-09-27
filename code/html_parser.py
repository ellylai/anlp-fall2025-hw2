from bs4 import BeautifulSoup
import requests


def validate_links(child_links, base_url):
    pdfs = []
    htmls = []
    print("validating child links")
    for link in child_links:
        if link[:4] == "http":
            n = len(link)
            if link[(n-3):] == "pdf":
                pdfs.append(link)
            else:
                htmls.append(link)
        elif link[0] == "/":
            link = base_url + link
            n = len(link)
            if link[(n-3):] == "pdf":
                pdfs.append(link)
            else:
                htmls.append(link)
    return pdfs, htmls

def parse_child_links(page_id, child_links):
    child_id = 1
    for link in child_links:
        html = requests.get(link).text
        soup = BeautifulSoup("<html>" + html + "</html>", 'html.parser')
        txt = soup.get_text(separator=" ", strip=True)
        # with open(f"pdfs_and_html_links/html/doc{page_id}-{child_id}.txt", "w", encoding="utf-8") as f:
        #     f.write(txt)
        child_id += 1
    print("Child html links parsed.")

def parse_html_links(parent_links):
    pdfs = []
    page_id = 1
    for link in parent_links:
        html = requests.get(link).text
        soup = BeautifulSoup("<html>" + html + "</html>", 'html.parser')
        txt = soup.get_text(strip=True)
        with open(f"pdfs_and_html_links/html/doc{page_id}-0.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        child_links = [child_link.get('href') for child_link in soup.find_all('a')]
        pdf_links, html_links = validate_links(child_links, link)
        pdfs += pdf_links
        parse_child_links(page_id, html_links)
    print("All links parsed. Dumping pdf links.")
    return pdfs