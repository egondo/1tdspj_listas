import banco
import datetime

if __name__ == "__main__":
    movie = {}
    movie['titulo'] = "Beetlejuice 2"
    movie['diretor'] = "Tim Burton"
    movie['data_lancamento'] = datetime.datetime(2024, 9, 15)
    movie['avaliacao'] = 8.7
    movie['duracao'] = 104
    movie['sinopse'] = "Retornamos à casa em Winter River, onde três gerações da família Deetz se unem após uma tragédia familiar inesperada."
    movie['classificacao'] = "14 anos"
    movie['genero'] = "comédia"
    print(movie)
    banco.insere_filme(movie)
