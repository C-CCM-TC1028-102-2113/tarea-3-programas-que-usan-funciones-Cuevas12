def areabase(base, altura):
    área= base*altura
    return área
def main():
    #escribe tu código abajo de esta línea
    base=float(input('Dame la base: '))
    altura=float(input('Dame la altura: '))
    profundidad=float(input('Dame la profundidad: '))
    volumen= areabase(base, altura)*profundidad
    print('El volumen del prisma es: ', volumen)

if __name__ == '__main__':
    main()
