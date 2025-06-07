"""
    Solicitar o nome do veiculo
    Solicitat o preço do veiculo 
    
    Oferecer 3 tipos de desconto
 - 60% de desconto
 - 30% de desconto
 - 0% de desconto
"""
       
Nomedoveiculo = input("Qual o nome do veiculo? ")
Precodoveiculo = int(input("Qual o preço do veiculo? "))
Desconto = input("Qual o tipo de desconto? (1, 2 ou 3) ")

printi("1 - 60% de desconto")
print("2 - 30% de desconto")    
print("3 - 0% de desconto")

if opcao == "1":
    Desconto = Precodoveiculo * 0.6
    PrecoFinal = Precodoveiculo - Desconto
    print(f"O veiculo {Nomedoveiculo} com 60% de desconto custa: {PrecoFinal}") 
elif opcao == "2": 
    Desconto = Precodoveiculo * 0.3
    PrecoFinal = Precodoveiculo - Desconto
    print(f"O veiculo {Nomedoveiculo} com 30% de desconto custa: {PrecoFinal}")     
elif opcao == "3":
    Desconto = Precodoveiculo * 0.0
    PrecoFinal = Precodoveiculo - Desconto
    print(f"O veiculo {Nomedoveiculo} com 0% de desconto custa: {PrecoFinal}")