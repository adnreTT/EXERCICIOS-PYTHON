print("1. Soma: 25 + 15 =", 25 + 15)
print("2. Subtração: 50 - 30 =", 50 - 30)
print("3. Multiplicação: 6 * 8 =", 6 * 8)
print("4. Divisão: 144 / 12 =", 144 / 12)
print("5. Exponenciação: 3 ** 4 =", 3 ** 4)
print("6. Módulo (resto da divisão): 29 % 5 =", 29 % 5)
print("7. Divisão inteira: 100 // 7 =", 100 // 7)
print("8. Ordem de prioridade: 10 + 5 * 2 =", 10 + 5 * 2)
print("9. Uso de parênteses: (10 + 5) * 2 =", (10 + 5) * 2)
print("10. Exponenciação antes da multiplicação: 2 ** 3 * 3 =", 2 ** 3 * 3)
print("11. Multiplicação antes da adição: 4 + 6 * 2 =", 4 + 6 * 2)
print("12. Módulo antes da subtração: 50 - 10 % 4 =", 50 - 10 % 4)
print("13. Soma e divisão: (20 + 10) / 5 =", (20 + 10) / 5)
print("14. Soma e multiplicação: 5 + 3 * 4 =", 5 + 3 * 4)
print("15. Dupla exponenciação: 2 ** (3 ** 2) =", 2 ** (3 ** 2))
print("16. Negação antes da soma: -10 + 5 =", -10 + 5)
print("17. Uso de float: 7.5 * 2.2 =", 7.5 * 2.2)
print("18. Divisão com float: 10 / 3 =", 10 / 3)
print("19. Mistura de inteiros e float: 5 * 2.5 =", 5 * 2.5)
print("20. Expressão complexa: (100 / 4) + (3 ** 2) * 2 - 5 =", (100 / 4) + (3 ** 2) * 2 - 5)




print("----------------------------------------------------------")


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\nResultados das comparações entre {num1} e {num2}:")
print(f"\n{num1} é maior que {num2}? {num1 > num2}")
print(f"{num1} é menor que {num2}? {num1 < num2}")
print(f"{num1} é maior ou igual a {num2}? {num1 >= num2}")
print(f"{num1} é menor ou igual a {num2}? {num1 <= num2}")
print(f"{num1} é igual a {num2}? {num1 == num2}")
print(f"{num1} é diferente de {num2}? {num1 != num2}")

print("----------------------------------------------------------")

import  math

print("21. Raiz quadrada de 49:", math.sqrt(49))
print("22. Raiz quadrada de 81:", math.sqrt(81))
print("23. Logaritmo natural (base e) de 10:", math.log(10))
print("24. Logaritmo base 10 de 1000:", math.log10(1000))
print("25. Seno de 30 graus:", math.sin(math.radians(30)))
print("26. Cosseno de 60 graus:", math.cos(math.radians(60)))
print("27. Tangente de 45 graus:", math.tan(math.radians(45)))
print("28. Fatorial de 5:", math.factorial(5))
print("29. Valor absoluto de -15:", abs(-15))
print("30. Arredondamento de 7.89 para baixo:", math.floor(7.89))
print("31. Arredondamento de 7.12 para cima:", math.ceil(7.12))

print("----------------------------------------------------------")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


print(f"\nResultados das comparações entre {num1}, {num2} e {num3}:")
print(f"\n{num1} é maior que {num2} e {num3}? {num1 > num2 and num1 > num3}")
print(f"{num2} é maior que {num1} e {num3}? {num2 > num1 and num2 > num3}")
print(f"{num3} é maior que {num1} e {num2}? {num3 > num1 and num3 > num2}")
print(f"\n{num1} é o menor entre os três? {num1 < num2 and num1 < num3}")
print(f"{num2} é o menor entre os três? {num2 < num1 and num2 < num3}")
print(f"{num3} é o menor entre os três? {num3 < num1 and num3 < num2}")
print(f"\nOs três números são iguais? {num1 == num2 == num3}")
print(f"Pelo menos dois números são iguais? {num1 == num2 or num1 == num3 or num2 == num3}")
