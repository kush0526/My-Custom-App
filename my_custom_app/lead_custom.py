def set_lead_title(doc, method=None):
    if doc.first_name:
        doc.title = doc.first_name
        doc.lead_name = doc.first_name
