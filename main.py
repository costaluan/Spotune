from music_utils import Song 

def insertion_sort_titulo(musicas):
    for i in range(1, len(musicas)):
        chave = musicas[i]
        j = i - 1
        while j >= 0 and musicas[j].title > chave.title:
            musicas[j + 1] = musicas[j]
            j -= 1
        musicas[j + 1] = chave

def insertion_sort_avaliacao(musicas):
    for i in range(1, len(musicas)):
        chave = musicas[i]
        j = i - 1
        while j >= 0 and musicas[j].rating < chave.rating:
            musicas[j + 1] = musicas[j]
            j -= 1
        musicas[j + 1] = chave

def classifica_avaliacao(musicas):
    buckets = [[] for _ in range(6)]  
    for musica in musicas:
        avaliacao_musica = int(musica.rating)
        buckets[avaliacao_musica].append(musica)
    
    organiza_musicas = []
    for bucket in reversed(buckets):
        insertion_sort_titulo(bucket)  
        organiza_musicas.extend(bucket)
    return organiza_musicas

def classifica_titulo(musicas):
    buckets = [[] for _ in range(26)]  
    for musica in musicas:
        primeira_letra = musica.title[0].upper()
        index_bucket = ord(primeira_letra) - ord("A")
        buckets[index_bucket].append(musica)
    organiza_musicas = []
    for bucket in buckets:
        insertion_sort_titulo(bucket)  
        organiza_musicas.extend(bucket)
    return organiza_musicas


random_songs = Song.generate_random_songs(50)  

ordena_musicas = classifica_titulo(classifica_avaliacao(random_songs))

musicas_por_genero = {}

for musica in ordena_musicas:
    genero = musica.genre
    if genero not in musicas_por_genero:
        musicas_por_genero[genero] = []
    musicas_por_genero[genero].append(musica)

for genero, musicas_genero in musicas_por_genero.items():
     insertion_sort_avaliacao(musicas_genero)

for genero, musicas_genero in musicas_por_genero.items():
    print(f"Gênero: {genero}")
    for musica in musicas_genero:
        print(f"Avaliação: {musica.rating}, Título: {musica.title}")
    print()
