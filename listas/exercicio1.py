lista = []

def adicionar_nome_na_lista():
    nome = input('Digite um nome: ')
    lista.append(nome)

while True:
    adicionar_nome_na_lista()
    if len(lista) > 5:
        break;
    
print(lista)