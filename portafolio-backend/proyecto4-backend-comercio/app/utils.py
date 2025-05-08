from bson import ObjectId

def serialize_mongo_document(document):
    """
    Convierte un documento de MongoDB en un formato serializable por JSON.
    """
    if isinstance(document, list):
        return [serialize_mongo_document(doc) for doc in document]
    if isinstance(document, dict):
        return {key: serialize_mongo_document(value) for key, value in document.items()}
    if isinstance(document, ObjectId):
        return str(document)
    return document