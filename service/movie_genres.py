from models.movie_genres import MovieGenres as MovieGenresModel 

class MovieGenresService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movie_genres (self) -> MovieGenresModel:
        result = self.db.query(MovieGenresModel).all()
        return result
    
    def create_movie_genres (self, moviegenres: MovieGenresModel):
        new_movie_genres = MovieGenresModel(
            movie_id= moviegenres.movie_id,
            gen_id= moviegenres.gen_id
        )
        self.db.add(new_movie_genres)
        self.db.commit()
        return