#!/usr/bin/python
# coding: UTF-8

def soma(a, b):
    '''
    Função que soma a e b.
    '''
    return a + b

def main():
    '''
    Programa que lê um inteiro positivo A e soma com o interio positivo B.
    '''

    print("Calculo da soma de A + B")

    # leia o valor de n
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de A: "))

    # calcule a soma
    ab = soma(a, b)

    # imprima a soma
    print(u"A soma de A + B:", ab)

if __name__ == '__main__':
    main()
