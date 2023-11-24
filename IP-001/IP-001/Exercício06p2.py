def determinar_signo(ano_nascimento):
    # Mapeando os signos
    signos = {
        0: "Macaco",
        1: "Galo",
        2: "Cão",
        3: "Porco",
        4: "Rato",
        5: "Boi",
        6: "Tigre",
        7: "Coelho",
        8: "Dragão",
        9: "Serpente",
        10: "Cavalo",
        11: "Carneiro"
    }

    resto = ano_nascimento % 12

    return signos.get(resto, "Ano de nascimento inváido")

ano_nascimento = int(input("Digite o ano de nascimento: "))

signo = determinar_signo(ano_nascimento)
print(f"Seu signo do zodíaco chinês é: {signo}")