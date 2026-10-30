import chromadb
from llm import chat
from client_docs import DOCS

client = chromadb.Client()  # in memory; use chromadb.PersistentClient(path='db') to keep data
col = client.get_or_create_collection('client_kb')

def chunk(text, size=500, overlap=100):
    out, start = [], 0
    while start < len(text):
        out.append(text[start:start + size])
        if start + size >= len(text):
            break
        start += size - overlap
    return out

def ingest():
    for doc_id, text in DOCS.items():
        parts = chunk(text)
        col.add(documents=parts,
                ids=[f'{doc_id}-{i}' for i in range(len(parts))],
                metadatas=[{'source': doc_id}] * len(parts))

SYSTEM = (
    'Answer using only the context. If the context does not contain the answer, '
    'reply exactly: I do not have that information. Keep answers short.'
)

def answer(question, k=2):
    res = col.query(query_texts=[question], n_results=k)
    passages = res['documents'][0]
    sources = [m['source'] for m in res['metadatas'][0]]
    context = '\n---\n'.join(passages)
    user = f'Context:\n{context}\n\nQuestion: {question}'
    reply = chat([{'role': 'system', 'content': SYSTEM},
                  {'role': 'user', 'content': user}]).choices[0].message.content
    return reply, sources

if __name__ == '__main__':
    ingest()
    for q in ['When are you open?', 'What is the late cancellation fee?',
              'Do you do home visits?', 'Who is the manager?']:
        print(q, '->', answer(q))
