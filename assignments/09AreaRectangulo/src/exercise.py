def calc(b,a):
    área=b*a
    return área
def main():
  #escribe tu código abajo de esta línea
    b=float(input('Dame la altura: '))
    a=float(input('Dame la base: '))
    área = calc(b,a)
    print('El área del rectángulo es: ', área)
    

if __name__ == '__main__':
    main()
