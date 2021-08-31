def tarjeta(alb, plu):
    if alb < plu:
        print ("El número máximo de tarjetas que se pueden hacer es:",alb)
    elif plu < alb:
        print("El número máximo de tarjetas que se pueden hacer es:",plu)
        
def cant(PapelAlbanene, Plumones):
    alb = PapelAlbanene * 12
    plu= Plumones * 35
    tarjeta(alb, plu)

def main():
    #escribe tu código abajo de esta línea
    PapelAlbanene = int(input("Dame la cantidad de pliegos de papel albanene: "))
    Plumones = int(input("Dame la cantidad de plumones: "))
    cant(PapelAlbanene, Plumones)
    main()

if __name__ == '__main__':
    main()
