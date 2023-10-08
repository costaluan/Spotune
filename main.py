import time
from datetime import datetime
from music_utils import Song 

tempo_inicio = (time.time())

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

def insertion_sort_data_lancamento(musicas):
    for i in range(1, len(musicas)):
        chave = musicas[i]
        j = i - 1
        while j >= 0 and datetime.strptime(musicas[j].release_date, "%d/%m/%Y") > datetime.strptime(chave.release_date, "%d/%m/%Y"):
            musicas[j + 1] = musicas[j]
            j -= 1
        musicas[j + 1] = chave

def insertion_sort_titulo_igual_avaliacao(musicas):
    for i in range(1, len(musicas)):
        chave = musicas[i]
        j = i - 1
        while j >= 0 and musicas[j].rating == chave.rating and musicas[j].title > chave.title:
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

def ordena_musicas(genero, musicas, ordenar_por_data=False):
    if ordenar_por_data:
        insertion_sort_data_lancamento(musicas)
    else:
        insertion_sort_avaliacao(musicas)
        insertion_sort_titulo_igual_avaliacao(musicas)

# Flag para ordenar por data ou não
valor = input("Ordenar musicas por data de lançamento? (Sim [1]/Não [2]): ")
if valor == "1":
    ordenar_por_data = True
else:
    ordenar_por_data = False

random_songs = Song.generate_random_songs(50)  

musicas_por_genero = {}
for musica in random_songs:
    genero = musica.genre
    if genero not in musicas_por_genero:
        musicas_por_genero[genero] = []
    musicas_por_genero[genero].append(musica)

for genero, musicas_genero in musicas_por_genero.items():
    ordena_musicas(genero, musicas_genero, ordenar_por_data)

for genero, musicas_genero in musicas_por_genero.items():
    print(f"Gênero: {genero}")
    for musica in musicas_genero:
        print(f"Avaliação: {musica.rating}, Título: {musica.title}, Data de Lançamento: {musica.release_date}")
    print()
   
tempo_final = (time.time())
print({tempo_final - tempo_inicio})
