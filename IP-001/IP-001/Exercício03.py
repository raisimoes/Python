def imprimir_caracteres_numericos():
    print("Imprimindo caracteres numéricos e seus códigos:")
    for i in range(10):
        print(f"'{str(i)}' - {ord(str(i))}")

def imprimir_caracteres_numericos_octal_hexadecimal():
    print("\nImprimindo caracteres numéricos e seus códigos em octal e hexadecimal:")
    for i in range(10):
        print(f"'{str(i)}' - {ord(str(i))} (octal: {oct(ord(str(i)))}, hexadecimal: {hex(ord(str(i)))})")

def imprimir_caractere_informado():
    caractere = input("\nDigite um caractere: ")
    print(f"'{caractere}' - {ord(caractere)} (octal: {oct(ord(caractere))}, hexadecimal: {hex(ord(caractere))})")

def caracteres_especiais():
    print("\nExemplo de caracteres especiais:")
    print("Caractere 'ç' -", ord('ç'))
    print("Caractere 'ã' -", ord('ã'))

# Chamando as funções
imprimir_caracteres_numericos()
imprimir_caracteres_numericos_octal_hexadecimal()
imprimir_caractere_informado()
caracteres_especiais()
