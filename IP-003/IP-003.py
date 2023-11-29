import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_product(products):
    product_code = input("Forneça o código do produto (13 caracteres): ")
    while len(product_code) != 13 or not product_code.isdigit():
        print("Código inválido, precisar ter 13 caracteres numéricos.")
        product_code = input("Forneça o código do produto (13 caracteres): ")

    name = input("Forneça o nome do produto: ")
    while not name or not name[0].isupper():
        print("Nome inválido, é preciso começar com letra maiúscula.")
        name = input("Forneça o nome do produto: ")

    price = input("Forneça o preço do produto (xx.xx): ")
    while not price.replace('.', '').isdigit():
        print("Preço inválido, é preciso ter duas casas decimais.")
        price = input("Forneça o preço do produto (xx.xx): ")

    product = {'codigo': product_code, 'nome': name, 'preco': float(price)}
    products.append(product)
    print("----- Produto cadastrado -----")

def delete_product(products):
    code = input("Forneça o código do produto que deseja excluir: ")
    for product in products:
        if product['codigo'] == code:
            products.remove(product)
            print("----- Produto excluído -----")
            return
    print("Produto não encontrado.")

def list_products(products):
    if not products:
        print("----- Não existem produtos cadastrados -----")
        return
    
    print("---------- Lista de produtos ----------")
    for i, product in enumerate(products, start=1):
        print(f"{i}. Código: {product['codigo']}, Nome: {product['nome']}, Preço: R${product['preco']:.2f}")

def consult_price(products):
    codigo = input("Forneça o código do produto que deseja consultar o preço: ")
    for product in products:
        if product['codigo'] == codigo:
            print(f"O preço do produto {product['nome']} é R${product['preco']:.2f}")
            return
    print("----- Produto não encontrado -----")

def main():
    products = []

    while True: 
        clear_screen()
        print("---------- Supermercado ----------")
        print("1. Inserir novo produto")
        print("2. Listar produtos")
        print("3. Excluir produto")
        print("4. Consultar preço de um produto")
        print("5. Sair")

        choice = input("Escolha a opção desejada: ")

        if choice == '1':
            insert_product(products)
        elif choice == '2':
            list_products(products)
        elif choice == '3':
            delete_product(products)
        elif choice == '4':
            consult_price(products)
        elif choice == '5':
            print("----- Programa encerrado -----")
            break
        else:
            print("Opção inválida, tente novamente.")

        input("\nPressione enter para continuar")

if __name__ == '_main_':
    main()