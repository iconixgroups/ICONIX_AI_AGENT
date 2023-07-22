from pymongo import MongoClient
from bson.objectid import ObjectId

class TemplateLibrary:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['iconix_ai_agent']
        self.templates = self.db['templates']

    def browse_templates(self, category=None):
        if category:
            return list(self.templates.find({"category": category}))
        else:
            return list(self.templates.find())

    def get_template(self, template_id):
        return self.templates.find_one({"_id": ObjectId(template_id)})

    def add_template(self, template_data):
        return self.templates.insert_one(template_data)

    def update_template(self, template_id, template_data):
        return self.templates.update_one({"_id": ObjectId(template_id)}, {"$set": template_data})

    def delete_template(self, template_id):
        return self.templates.delete_one({"_id": ObjectId(template_id)})

template_library = TemplateLibrary()