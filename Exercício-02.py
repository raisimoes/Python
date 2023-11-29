import csv

funcionario_keys = ['nome', 'sobrenome', 'ano_nascimento', 'RG', 'ano_admissao', 'salario']
funcionarios = []

def ler_informacoes(nome_arquivo):
    with open(nome_arquivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            funcionarios.append(row)

def reajusta_dez_porcento(lista_funcionarios):
    for funcionario in lista_funcionarios:
        salario_atual = float(funcionario['salario'])
        novo_salario = salario_atual * 1.1
        funcionario['salario'] = str(novo_salario)

def exibir_dados(lista_funcionarios):
    for funcionario in lista_funcionarios:
        print(funcionario)

arquivo_funcionarios = 'funcionarios.csv'

ler_informacoes(arquivo_funcionarios)

print("Dados antes do reajuste:")
exibir_dados(funcionarios)

reajusta_dez_porcento(funcionarios)

print("\nDados após o reajuste:")
exibir_dados(funcionarios)
