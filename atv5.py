lista1 = ['Felipe', 'Leonardo', 'Vinicyus', 'Caio', 'Luana' ]
print(type(lista1))
print(len(lista1))
print(lista1[4])
lista2 = lista1 *2
print(lista2)
lista1.append('sempre') #adiciona itens ao fim da lista
print(lista1)
lista1.remove("Caio")
print(lista1)
lista1.pop(3)
print(lista1)

for listageral in lista1:
    print(listageral)