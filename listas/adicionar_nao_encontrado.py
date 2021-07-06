# Do exercício anterior, caso não seja encontrado o nome,
# adicione o nome 'Paulo' à lista.
#reescreva a função anterior, para adicionar 'Paulo' caso ele não seja encontrado
# caso paulo já estiver na lista, printar 'Paulo já está na lista'

contatos = ['Abner', 'Angelica', 'Bruno', 'Carlos', 'Diego']

def lista_contem_o_nome_paulo(array):
    if 'Paulo' in array:
        print('Paulo já está na lista')
    else:
        array.append('Paulo')
        
lista_contem_o_nome_paulo(contatos)
print(contatos)