# Some code Adapted from the CMU 11-711 Advanced NLP Fall 2025 reference implementation:
# https://github.com/cmu-l3/anlp-fall2025-code/blob/main/10_rag/rag.ipynb

import os


def chunk_documents(data_folder, chunk_size):
    documents = []

    for file_name in os.listdir(data_folder):
        if file_name.endswith(".txt"):
            with open(os.path.join(data_folder, file_name), "r", encoding="utf-8") as f:
                documents.append(f.read())

    print(f"Loaded {len(documents)} documents")
    print("Example document:", documents[0][:300])

    def chunk_text(text, chunk_size, overlap):
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i : i + chunk_size])
            if chunk:
                chunks.append(chunk)
        return chunks

    all_chunks = []
    for doc in documents:
        chunks = chunk_text(doc, chunk_size=chunk_size, overlap=10)
        all_chunks.extend(chunks)

    print(f"Created {len(all_chunks)} chunks")
    print(f"\nExample chunk:\n{all_chunks[0]}")
    print(f"\nExample chunk:\n{all_chunks[-1]}")

    chunk_folder = "data"
    folder_name = data_folder.split("/")[-1]
    chunk_file_path = os.path.join(
        chunk_folder, f"all_chunks_{folder_name}_size{chunk_size}.txt"
    )

    # Save chunks
    with open(chunk_file_path, "w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(chunk.strip() + "\n")

    print(f"Saved {len(all_chunks)} chunks to {chunk_file_path}")


if __name__ == "__main__":
    for chunk_size in [30, 50, 100, 150, 200]:
        chunk_documents("pdfs_and_html_links/pdfs", chunk_size)
        chunk_documents("pdfs_and_html_links/html", chunk_size)
