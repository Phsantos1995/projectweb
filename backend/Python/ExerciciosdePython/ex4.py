
def tabuada(x):

    for cont in range(1,11):
        print('{0} x {1} = {2}'.format(x,cont,x*cont))




def tabuadasoma(x):

    for cont in range(1,11):
        print('{0} + {1} = {2}'.format(x,cont,x+cont))

             

def tabuadasub(x):

    for cont in range(1,11):
        print('{0} - {1} = {2}'.format(x,cont,x-cont))


def tabuadadiv(x):
    for cont in range (1,11):
        print('{0} / {1} = {2}'.format(x,cont,x/cont))
        



numero= int(input("Informe o numero para o calculo da tabuada:"))
tabuada(numero)
print("//////////////////////////////")
tabuadasoma(numero)
print("//////////////////////////////")
tabuadasub(numero)
print("//////////////////////////////")
tabuadadiv(numero)


