contatos = ['Abner', 'Angelica', 'Bruno', 'Carlos', 'Diego']

# Escreva a funcao lista_contem_o_nome_paulo(array)
# essa função recebe como parâmetro uma LISTA, não uma string
# essa função deve retornar ou True ou False
#ou seja, se 'Paulo' não for encontrado dentro da lista, ela retorna False
# se for encontrado, retornará True

def lista_contem_o_nome_paulo(array):
    if 'Paulo' in array:
        return True
    
    return False

resultado = lista_contem_o_nome_paulo(contatos)

print(resultado)