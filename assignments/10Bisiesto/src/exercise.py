def es_bisiesto(año):
    if año % 400 == 0:
        print('True', es_bisiesto(año))
    elif año % 100 == 0:
        print ('False', es_bisiesto(año))
    elif año % 4 == 0:
        print ('True', es_bisiesto(año))
    else:
        print ('False', es_bisiesto(año))
    return es_bisiesto(año)

def main():
    año=float(input(''))
    print(str(es_bisiesto(año)))
    

    if __name__ == '__main__':
        main()
