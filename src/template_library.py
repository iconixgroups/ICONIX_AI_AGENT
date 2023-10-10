from src.shared_dependencies import MongoClient, ObjectId, templates

def browse_templates(category=None):
    if category:
        return list(templates.find({"category": category}))
    else:
        return list(templates.find())

def get_template(template_id):
    return templates.find_one({"_id": ObjectId(template_id)})

def add_template(template_data):
    return templates.insert_one(template_data)

def update_template(template_id, template_data):
    return templates.update_one({"_id": ObjectId(template_id)}, {"$set": template_data})

def delete_template(template_id):
    return templates.delete_one({"_id": ObjectId(template_id)})