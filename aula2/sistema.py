
def menu():
    print("=========================")
    print("Sistema do café, chá e lasanha SENAI")
    print("==========================")
    print("1 - criar um café")
    print("2 - Listar os cafés")
    print("3 - Qual maior preço do café")
    print("4 - Criar um chá")
    print("5 - Listar os chás")
    print("6 - Qual maior preço do chá")
    print("0 - Sair do sistema")
    
    
    4
class café:   
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

cafes = []

    
class chá:   
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

chás = []


while True:
    menu()
    opcao = int(input("Digite a opção escolhida: "))
    
    if opcao == 1:
        nome = input("Digite o nome do café: ")
        preco = float(input("Digite o preço do café: "))
        
        novo_cafe = café(nome, preco)
        cafes.append(novo_cafe)
        
    elif opcao == 2:
        # Listar os cafés
        
        # len - > Length ->
    
        if len(café) == 0:
            print("Nenhum cafe cadastrado.")
        else:
            # \n -> Quebrar linha
            print( "\n---- Lista de cafés ----")
            
            
        #  for -> repita 
        for café in cafes:
            print(café)
            
    elif opcao == 3:
        
        # Verificar o maior preço do café
        # cafes {0} => primeiro café
        
        mais_caro = cafes[0] 
        for café in cafes:
            if café.preco > mais_caro.preco:
                mais_caro = cafes            
            
        print(f"\n\café mais caro é: {mais_caro.nome}")
        print(f"Preço do café {mais_caro.preco:.2f}")
        
        
    elif opcao == 4:
        nome = input("Digite o nome do chá: ")
        preco = float(input("Digite o preço do chá: "))
        
        novo_cha = chá(nome, preco)
        chás.append(novo_cha)
    elif opcao == 5:
        if len(chás) == 0:
            print("Nenhum chá cadastrado.")
        else:
            print("\n---- Lista de chás ----")
            for chá in chás:
                print(chá)
    elif opcao == 6:
        if len(chás) == 0:
            print("Nenhum chá cadastrado.")
        else:
            maior_preco = max(chás, key=lambda x: x.preco)
            print(f"O chá mais caro é: {maior_preco}")
