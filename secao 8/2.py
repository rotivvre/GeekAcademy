"""Faça uma função que receba a data atual(dia, mês ano em inteiro) e 
    exiba na tela o formato textual por extenso. Exemplo: Data: 01/01/2000, imprimir 1 de janeiro de 2000"""
    
def data_por_extenso(dia, mes, ano):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    print(f"{dia} de {meses[mes-1]} de {ano}")
    
data_por_extenso(11,10,2020)
