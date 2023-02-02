from models.genres import Genres as GenresModel
from schemas.genres  import Genres

class GenresService():

    def init (self,db) -> None:
        self.db = db

    def get_genres(self):
        result = self.db.query(GenresModel).all()
        return result

    def get_genres(self,id:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id).first()
        return result

    def get_genres(self,title:str):
        result = self.db.query(GenresModel).filter(GenresModel.title == title).last()
        return result
