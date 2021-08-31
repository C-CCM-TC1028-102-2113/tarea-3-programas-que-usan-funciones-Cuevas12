def es_bisiesto(año):
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False 

def main():
    #escribe tu código abajo de esta línea
    año= float(input())
    esbisiesto= es_bisiesto(año)
    print(esbisiesto)
    
if __name__ == '__main__':
    main()
