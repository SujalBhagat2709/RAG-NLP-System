from document_store import documents

def retrieve(query):
    return [doc for doc in documents if query.lower() in doc.lower()]