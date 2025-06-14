"""
O sistema deve pedir um numero
E deve dizer se ele é impar ou par 

* multiplicação
/ divisão
!= diferente
>= maior igual
<= menor igual
< menor
>maior

"""

parouimpar = int(input("Digite um número: "))

if parouimpar % 2 != 0:
    print(f"O número {parouimpar} é ímpar.")
    
if parouimpar % 2 == 0:
    print(f"O número {parouimpar} é par.")
    