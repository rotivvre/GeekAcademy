"""Crie uma funcao que recebe como parametro um numero inteiro e devolve seu dobro"""

def dobro_do_inteiro(num, *args):
    if type(num) == int or type(num) == float:
        return num * 2
    

    