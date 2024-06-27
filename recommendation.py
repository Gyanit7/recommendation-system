import random
from collections import defaultdict

# Sample dataset of real movies with detailed features
movies = {
    'Inception': {'genres': ['Action', 'Sci-Fi'], 'director': 'Christopher Nolan',
                  'actors': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt'], 'year': 2010},
    'The Godfather': {'genres': ['Crime', 'Drama'], 'director': 'Francis Ford Coppola',
                      'actors': ['Marlon Brando', 'Al Pacino'], 'year': 1972},
    'Pulp Fiction': {'genres': ['Crime', 'Drama'], 'director': 'Quentin Tarantino',
                     'actors': ['John Travolta', 'Uma Thurman'], 'year': 1994},
    'The Dark Knight': {'genres': ['Action', 'Crime'], 'director': 'Christopher Nolan',
                        'actors': ['Christian Bale', 'Heath Ledger'], 'year': 2008},
    'Forrest Gump': {'genres': ['Drama', 'Romance'], 'director': 'Robert Zemeckis',
                     'actors': ['Tom Hanks', 'Robin Wright'], 'year': 1994},
    'The Matrix': {'genres': ['Action', 'Sci-Fi'], 'director': 'Lana Wachowski',
                   'actors': ['Keanu Reeves', 'Laurence Fishburne'], 'year': 1999},
    'The Shawshank Redemption': {'genres': ['Drama'], 'director': 'Frank Darabont',
                                 'actors': ['Tim Robbins', 'Morgan Freeman'], 'year': 1994},
    'The Lord of the Rings: The Fellowship of the Ring': {'genres': ['Action', 'Adventure'],
                                                          'director': 'Peter Jackson',
                                                          'actors': ['Elijah Wood', 'Ian McKellen'], 'year': 2001},
    'Fight Club': {'genres': ['Drama'], 'director': 'David Fincher', 'actors': ['Brad Pitt', 'Edward Norton'],
                   'year': 1999},
    'Titanic': {'genres': ['Drama', 'Romance'], 'director': 'James Cameron',
                'actors': ['Leonardo DiCaprio', 'Kate Winslet'], 'year': 1997}
}


def recommend_movies(user_preferences):
    scores = defaultdict(int)

    for movie, details in movies.items():
        # Compute genre similarity score
        if user_preferences['genres']:
            genre_score = len(
                set(genre.lower() for genre in details['genres']).intersection(user_preferences['genres']))
            if genre_score == 0:
                continue  # Skip movies that don't match any preferred genres
            scores[movie] += genre_score

        # Compute director similarity score
        if user_preferences['director']:
            director_parts = user_preferences['director'].split()
            if any(part in details['director'].lower() for part in director_parts):
                scores[movie] += 1

        # Compute actor similarity score
        for actor_preference in user_preferences['actors']:
            actor_parts = actor_preference.split()
            if any(part in actor.lower() for actor in details['actors'] for part in actor_parts):
                scores[movie] += 1

    # Sort movies based on similarity scores in descending order
    recommended_movies = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return [movie for movie, score in recommended_movies]


def get_user_preferences():
    genres = input("Enter your preferred genres (comma separated, or leave empty for no preference): ").lower().split(
        ',')
    genres = [genre.strip() for genre in genres if genre.strip()]

    director = input("Enter your preferred director (or leave empty for no preference): ").strip().lower()

    actors = input("Enter your preferred actors (comma separated, or leave empty for no preference): ").lower().split(
        ',')
    actors = [actor.strip() for actor in actors if actor.strip()]

    return {
        'genres': genres,
        'director': director,
        'actors': actors
    }


user_preferences = get_user_preferences()
recommended_movies = recommend_movies(user_preferences)

print(f"Recommended movies based on your preferences: {recommended_movies}")
