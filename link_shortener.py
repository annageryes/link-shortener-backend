import uuid 
from json_manager import JsonManager

class LinkShortener:
    def __init__(self):
        self.url_entities = JsonManager.read()
        
    def get_link_by_id(self,  id: str):
        for url_entity in self.url_entities:
            if url_entity["id"] == id:
                return url_entity["url"]
        
        raise Exception("Your ID is not found")

    def shorten(self, url: str):
        # creates a list with the ids
        ids = [entity["id"] for entity in self.url_entities]
        unique_id = generate_id()
        while not is_unique(unique_id,ids):
            unique_id = generate_id()
        new_url_entity = {"id": unique_id, "url": url}
        self.url_entities.append(new_url_entity)
        JsonManager.write(self.url_entities)
        return unique_id

    def url_exists(self,url: str):
        for url_entity in self.url_entities:
            if url_entity["url"] == url:
                return url_entity["id"]
        return None
    
def generate_id():
    return str(uuid.uuid4())[:8]
    
    
def is_unique(self,id: str,list_ids:list):
        return id not in list_ids
        
        



























