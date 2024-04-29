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
        id_exists=self.url_exists(url) 
        if id_exists:
            return id_exists
        unique_id=None
        while not self.id_exists(unique_id):
            print(self.id_exists(unique_id))
            unique_id = str(uuid.uuid4())[:8]
        new_url_entity = {"id": unique_id, "url": url}
        self.url_entities.append(new_url_entity)
        JsonManager.write(self.url_entities)
        return unique_id

    def url_exists(self,url: str):
        for url_entity in self.url_entities:
            if url_entity["url"] == url:
                return url_entity["id"]
        return None
    
    
    def id_exists(self,id: str):
        if not id:
            return False
        for url_entity in self.url_entities:
            if url_entity["id"] == id:
                return False
        return True
        
        



























