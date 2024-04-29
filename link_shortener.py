import uuid 
from json_manager import JsonManager

class LinkShortener:
    @classmethod
    def get_link_by_id(self,  id: str):
        url_entities = JsonManager.read()
        for url_entity in url_entities:
            if url_entity["id"] == id:
                return url_entity["url"]
        
        raise Exception("Your ID is not found")

    @classmethod
    def shorten(self, url: str):
        id_exists=self.url_exists(url) 
        if id_exists:
            return id_exists
        unique_id = str(uuid.uuid4())[:8]
        new_url_entity = {"id": unique_id, "url": url}
        url_entities = JsonManager.read()
        url_entities.append(new_url_entity)
        JsonManager.write(url_entities)
        return unique_id
    
    @classmethod
    def url_exists(self,url: str):
        url_entities = JsonManager.read()
        for url_entity in url_entities:
            if url_entity["url"] == url:
                return id
        return None
        
        



























