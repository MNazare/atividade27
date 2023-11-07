# Exercício Python 27: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. DICA: VEJA SOBRE FUNÇÃO REPLACE(), LOWER() E UMA FORMA DE INVERTER OS CARACTERES. 

frase = str(input("gigite a palavvra: "))
frase = frase.upper().replace(" ", "")
invertido = frase.upper()[::-1]

invertido = invertido.replace(" ","")

if frase == invertido:
    print("polidromo!")
else:
    print("não é polidromo")