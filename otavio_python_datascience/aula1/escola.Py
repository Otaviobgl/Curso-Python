"""
Solictar 4 notas para o usuario
realizar calculo da média
se a nota for maior que 7
usuario aprovado
menor que 7 
usuario reprovado
    """
    
nota1 = int(input("calculo de 1 "))
nota2 = int(input("calculo de 2 "))
nota3 = int(input("calculo de 3 "))
nota4 = int(input("calculo de 4"))

Média = (nota1 + nota2 + nota3 + nota4) / 4

if Média >= 7:
    print(f"Usuário aprovado com média: {Média}")
else:
    print(f"Usuário reprovado com média: {Média}")
    