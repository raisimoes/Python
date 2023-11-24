# Operadores aritméticos
a = 7
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# Operadores ariméticos compostos
a += 3 --> é igual a a = a + 1
b *= 3 --> é igual a b = b * 3

# Representação de números inteiros grandes
import math

fatorial_30 = math.factorial(30)
print(f"Fatorial de 30: {fatorial_30}")

# Variáveis numéricas imutáveis
x = 5
y = x
x = 10

print(y) # y = 5, não sofrerá alteração

# Métodos disponíveis para variáveis inteiras
num = 42
--> Convertendo inteiro em string
num_str = str(num)

--> Calculando valor absoluto
abs_num = abs(num)

--> Verificando se o número é par
is_even = num % 2 == 0

--> Convertendo string em inteiro
str_num = int("123")

--> Convertendo inteiro em representação binária
bin_num = bin(num)