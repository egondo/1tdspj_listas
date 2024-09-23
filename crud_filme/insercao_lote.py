import banco
import datetime

lista = [
    ["ET", "Steven Spielberg", "01-05-1986", 9, 120, 'Extraterrestre chega à Terra', "livre", "drama"],
    ["O Jogo da Imitação", "Morten Tyldum", "06-08-2010", 8.8, 134, 'Conta a vida de Alan Turing', "12 anos", "drama"],
    ["Uma mente brilhante", "Ron Howard", "04-10-2001", 9.2, 127, 'Narra a história de Jonh Nash, vencedor do Nobel de economia', '10 anos', 'drama'],
    ["Os caça-fantasmas", "Ivan Reitman", "08-06-1984", 7.6, 115, 'Caçadore de fantasmas', "10 anos", "comédia"]
];

for registro in lista:
    movie = {}
    movie['titulo'] = registro[0]
    movie['diretor'] = registro[1]
    movie['data_lancamento'] = registro[2]
    movie['avaliacao'] = registro[3]
    movie['duracao'] = registro[4]
    movie['sinopse'] = registro[5]
    movie['classificacao'] = registro[6]
    movie['genero'] = registro[7]

    #banco.insere_filme(movie)

#ex 3
filmes = banco.consulta_genero('com')
if not filmes:
    print("Nenhum filme retornado")
for f in filmes:
    print(f)

#ex 4
reg = ("E.T. O Extraterrestre", 'Steven Spielberg', datetime.datetime(1982, 12, 25), 7.9, 130, '''O garoto Elliott faz amizade com um pequeno alienígena inofensivo que está bem longe do seu planeta. Ele decide manter a adorável criatura em segredo e em casa após apresentá-la aos irmãos.''', 'livre', 'Ficção científica')
movie = {"titulo": reg[0]}
movie['diretor'] = reg[1]
movie['data_lancamento'] = reg[2]
movie['avaliacao'] = reg[3]
movie['duracao'] = reg[4]
movie['sinopse'] = reg[5]
movie['classificacao'] = reg[6]
movie['genero'] = reg[7]
movie['id'] = 6

banco.altera_filme(movie)

#lista = banco.consulta_genero("cien")
#print(lista)

banco.apaga_filme(9)
lista = banco.consulta_genero("comé")
print(lista)

