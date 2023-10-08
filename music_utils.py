import random
from datetime import datetime

title_words = ["Love", "Sunset", "Dream", "Ocean", "Sky", "Heart", "Moon", "Stars"]
artist_names = ["HarmonyWeaver", "MelodyForge", "RhythmCraft", "MusicMaker", "TuneMaster"]
genres = ["Pop", "Rock", "Electronic", "Hip Hop", "Jazz", "Classical"]

class Song:

    def __init__(self, title, artist, genre, release_date, rating):
        self.title = title
        self.artist = artist
        self.genre = genre

        # Converte a data de lançamento em um objeto datetime
        release_date_obj = datetime.strptime(release_date, "%Y-%m-%d")
        
        # Formata a data no formato de dia/mês/ano
        self.release_date = release_date_obj.strftime("%d/%m/%Y")
        
        self.rating = rating

    def __str__(self):
        return f"{self.title} by {self.artist}"

    @staticmethod
    def generate_random_songs(num_songs=1):
        random_songs = []
        for _ in range(num_songs):
            title = random.choice(title_words) + " " + random.choice(title_words)
            artist = random.choice(artist_names)
            genre = random.choice(genres)
            release_date = f"{random.randint(2000, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            rating = round(random.uniform(0, 5), 1)
            random_songs.append(Song(title, artist, genre, release_date, rating))

        return random_songs

# # Exemplo de uso
# random_songs = Song.generate_random_songs(10)

# # Imprime as músicas aleatórias
# for song in random_songs:
#     print(f"Title: {song.title}")
#     print(f"Artist: {song.artist}")
#     print(f"Genre: {song.genre}")
#     print(f"Release Date: {song.release_date}")
#     print(f"Rating: {song.rating}")
#     print()
