def calc(b,a):
    area=b*a
    return area
def main():
  #escribe tu código abajo de esta línea
    b=float(input('Dame la altura: '))
    a=float(input('Dame la base: '))
    area = calc(b,a)
    print('El área del rectángulo es: ',str(area))
    

if __name__ == '__main__':
    main()
