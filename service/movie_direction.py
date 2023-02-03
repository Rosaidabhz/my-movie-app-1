from models.movie_direction import Direction as DirectionModel
from schemas.movie_direction import Movie_direction 

class DirectionMovieService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_direction_movie (self) -> DirectionModel:
        result = self.db.query(DirectionModel).all()
        return result
    
    def create_direction_movie (self, direction: DirectionModel):
        new_direction = DirectionModel(
            dir_id = Movie_direction.dir_id,
            mov_id = Movie_direction.mov.id,
        )
        self.db.add(new_direction)
        self.db.commit()
        return