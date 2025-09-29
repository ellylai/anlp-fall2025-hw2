from bs4 import BeautifulSoup
import requests


def validate_links(child_links, base_url, all_links):
    pdfs = []
    htmls = []
    levels = base_url.count("/")
    print("validating child links")
    if "wikipedia" in base_url:
        return pdfs, htmls, all_links
    elif "britannica" in base_url:
        return pdfs, htmls, all_links
    
    for link in child_links:
        if link is None:
            continue
        elif len(link) == 0:
            continue
        elif "oc_lang" in link:
            continue
        elif "instagram" in link or "/x.com" in link or "twitter" in link:
            continue
        elif link in all_links:
            continue
        if link[:4] == "http":
            if base_url not in link:
                continue
            n = len(link)
            if link[(n - 3) :] == "pdf":
                pdfs.append(link)
            elif link.count("/") > (levels+1):
                continue
            else:
                htmls.append(link)
        elif link[0] == "/":
            n = len(link)
            if link[(n - 3) :] == "pdf":
                if "pittsburghpa.gov" in base_url:
                    link = "https://www.pittsburghpa.gov" + link
                elif "cmu.edu" in base_url:
                    link = "https://www.cmu.edu" + link
                pdfs.append(link)
            link = base_url + link[1:]
            if link.count("/") > (levels+1):
                continue
            else:
                htmls.append(link)
        all_links.append(link)
    return pdfs, htmls, all_links


def parse_child_links(page_id, child_links):
    child_id = 1
    for link in child_links:
        html = requests.get(link, timeout=10).text
        soup = BeautifulSoup("<html>" + html + "</html>", "html.parser")
        txt = soup.get_text(separator=" ", strip=True)
        with open(f"pdfs_and_html_links/html/doc{page_id}-{child_id}.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        child_id += 1
    print("Child html links parsed.")


def parse_html_links(parent_links):
    all_links = []
    pdfs = []
    page_id = 1
    for link in parent_links:
        print(link)
        n = len(link)
        if link[(n - 3) :] == "pdf":
                pdfs.append(link)
                continue
        all_links.append(link)
        html = requests.get(link, timeout=10).text
        soup = BeautifulSoup("<html>" + html + "</html>", "html.parser")
        txt = soup.get_text(strip=True)
        with open(f"pdfs_and_html_links/html/doc{page_id}-0.txt", "w", encoding="utf-8") as f:
            f.write(txt)
        child_links = [child_link.get("href") for child_link in soup.find_all("a")]
        pdf_links, html_links, all_links = validate_links(child_links, link, all_links)
        pdfs += pdf_links
        parse_child_links(page_id, html_links)
        page_id += 1
    print("All links parsed. Dumping pdf links.")
    return pdfs, all_links
