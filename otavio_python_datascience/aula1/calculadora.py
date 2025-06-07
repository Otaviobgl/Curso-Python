
print("calculadora do SENAI")
print("Digite a operação a realizar")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("###################")

opcao = int(input(""))

#SOMA
if opcao== 1:
    num1= float(input("digite o primeiro numero:"))
    num2= float(input("digite o segundo numero:"))
    
    # executando a operação de soma
    resultado = num1 + num2
    # exibir na tela com o texto -> f' (variavel)
    print(f'O seu resultado é: {resultado}')
    
#SUBTRAÇÃO
elif opcao==2:
    num1= float(input("digite o primeiro numero:"))
    num2= float(input("digite o segundo numero:"))
    
    resultado = num1 - num2
     
    print(f'O seu resultado é: {resultado}')
    
#MULTIPLICAÇÃO
elif opcao==3:
    num1= float(input("digite o primeiro numero:"))
    num2= float(input("digite o segundo numero:"))
    
    resultado = num1 * num2
    
    print(f'O seu resultado é: {resultado}')
#DIVISÃO
elif opcao==4:
    num1= float(input("digite o primeiro numero:"))
    num2= float(input("digite o segundo numero:"))
    
    resultado = num1 / num2
    
    print(f'O seu resultado é: {resultado}')
    
