def match_documents(source, target, comparable_field="index"):
    matched_documents = list()
    for document in source:
        for target_document in target:
            if str(document[comparable_field]) == str(target_document[comparable_field]):
                matched_documents.append(target_document)
                break
    return matched_documents
