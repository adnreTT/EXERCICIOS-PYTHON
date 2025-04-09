# Solicita os dados
km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

# Calculo
custo_dias = dias_aluguel * 60
custo_km = km_percorridos * 0.15
total = custo_dias + custo_km

#Resultado
print("O preço total a pagar é: R$%.2f" % total)





print("---------------------------------------------------------------------------------")



# Solicita os dados
preco = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

# Calculo
valor_desconto = preco * (percentual_desconto / 100)
preco_final = preco - valor_desconto

# Resultado
print("Valor do desconto: R$" , valor_desconto)
print("Preço a pagar: R$" ,  preco_final)




print("------------------------------------------------------------------------------------")


# Dados
C = float(input("Digite a temperatura em Celsius: "))

#Calculo
F = (9 * C + 160) / 5

#Resultado
print("A temperatura em celsius equivalem a:" , F ,"F")



print("------------------------------------------------------------------------------------")


# Solicita os dados
salario_atual = float(input("Digite o valor do salário atual: R$ "))
percentual_aumento = float(input("Digite o percentual de aumento (%): "))

# Calculo
valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

# Resusltados
print("Valor do aumento: R$", valor_aumento)
print("Novo salário: R$", novo_salario)



print("------------------------------------------------------------------------------------")





# Solicita os dados
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um segundo numero: "))


res = numero1 + numero2

print("A soma dos dois numeros interios é:", res)




print("------------------------------------------------------------------------------------")


# SOLICITA OS DADOS
distancia = float(input("Digite a distância a percorrer (km): "))
velocidade_media = float(input("Digite a velocidade média esperada (km/h): "))

# CALCULO
tempo_horas = distancia / velocidade_media

# CONVERTE
horas = int(tempo_horas)
minutos = int((tempo_horas - horas) * 60)
segundos = int((((tempo_horas - horas) * 60) - minutos) * 60)

# RESULTADOS
print("Tempo estimado de viagem:", horas,"h",minutos, "min", segundos ,"s")
print("(Ou aproximadamente", tempo_horas ,"horas")




print("------------------------------------------------------------------------------------")

# Solicita os dados
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# CalculO
total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

# RESULTADO
print("O total em segundos é:", total_segundos, "segundos")

print("------------------------------------------------------------------------------------")

# Solicita os dados
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

# Calculo
total_cigarros = cigarros_por_dia * (anos_fumando * 365)

# Calcula o tempo perdido em minutos e converte para dias
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (24 * 60)  # 1440 minutos em um dia

# resultado
print("Você já perdeu aproximadamente",dias_perdidos, "dias de vida por fumar.")



print("------------------------------------------------------------------------------------")


# Dados
C = float(input("Digite a temperatura em Celsius: "))

#Calculo
F = (9 * C ) / 5 + 32

#Resultado
print("A temperatura em celsius equivalem a:" , F ,"F")


print("------------------------------------------------------------------------------------")

# Dados
cm = float(input("Digite uma medida em CM: "))

#Calculo
mm = cm * 10

#Resultado
print("A medida em centimetros convertida para milimetro é:" , mm ,"mm")



print("------------------------------------------*EXERCICIOS  LISTA 7*------------------------------------------------------")


# Solicita os valores iniciais
a = input("Digite o valor de A: ")
b = input("Digite o valor de B: ")

# Exibe os valores antes da troca
print("Valores originais: A =",a, "B =",b)

# Efetua a troca usando uma variável temporária
temp = a
a = b
b = temp

# Exibe os valores após a troca
print("Valores trocados: A =",a, "B =",b)



print("-------------------------------------------------------------------------------------------------------")

# Solicita os dados
cotacao_dolar = float(input("Digite a cotação atual do dólar (US$ 1 = R$ ): "))
quantidade_dolar = float(input("Digite a quantidade de dólares disponíveis: US$ "))

# Calculo
valor_reais = quantidade_dolar * cotacao_dolar

# Resultados
print("US$ ", quantidade_dolar , "dólares equivalem a R$ ", valor_reais, "reais")
print("Cotação utilizada: US$ 1 = R$" ,cotacao_dolar)


print("-------------------------------------------------------------------------------------------------------")



A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


diferenca = A - B
quadrado_diferenca = diferenca ** 2


print("O quadrado da diferença entre A e B é:" ,quadrado_diferenca)


print("-------------------------------------------------------------------------------")


tempo = float(input("Digite o tempo gasto na viagem (horas): "))
velocidade_media = float(input("Digite a velocidade média (km/h): "))


distancia = tempo * velocidade_media
litros_usados = distancia / 12


print("Velocidade média:" , velocidade_media, "km/h")
print("Tempo gasto:" ,tempo, " horas")
print("Distância percorrida:" , distancia," km")
print("Litros de combustível utilizados:", litros_usados, "L")




print("-------------------------------------------------------------------------------")

comprimento = float(input("Digite o comprimento da caixa (em metros): "))
largura = float(input("Digite a largura da caixa (em metros): "))
altura = float(input("Digite a altura da caixa (em metros): "))


volume = comprimento * largura * altura

print("O volume da caixa retangular é: ", volume, "m³")


print("-------------------------------------------------------------------------------")

# Entrada do valor inteiro
numero = int(input("Digite um número inteiro: "))

# Cálculo do quadrado
quadrado = numero ** 2

# Saída do resultado
print("O quadrado de ",numero," é:", quadrado)


# Entrada dos quatro valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Combinações de adições
soma_AB = A + B
soma_AC = A + C
soma_AD = A + D
soma_BC = B + C
soma_BD = B + D
soma_CD = C + D

# Combinações de multiplicações
mult_AB = A * B
mult_AC = A * C
mult_AD = A * D
mult_BC = B * C
mult_BD = B * D
mult_CD = C * D

# Saída dos resultados
print("\n--- Resultados das Adições ---")
print(f"A + B = ", soma_AB)
print(f"A + C = ", soma_AC)
print(f"A + D = ", soma_AD)
print(f"B + C = ", soma_BC)
print(f"B + D = ", soma_BD)
print(f"C + D = ", soma_CD)

print("\n--- Resultados das Multiplicações ---")
print(f"A * B = ", mult_AB)
print(f"A * C = ", mult_AC)
print(f"A * D = ", mult_AD)
print(f"B * C = ", mult_BC)
print(f"B * D = ", mult_BD)
print(f"C * D = ", mult_CD)


print("-------------------------------------------------------------------------------")

# Entrada dos dados
raio = float(input("Digite o raio da lata (em centímetros): "))
altura = float(input("Digite a altura da lata (em centímetros): "))

# Cálculo do volume
pi = 3.14159
volume = pi * (raio ** 2) * altura

# Saída do resultado
print(f"O volume da lata de óleo é: ",volume ,"cm³")



print("-------------------------------------------------------------------------------")


# Entrada da temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Conversão para Celsius
celsius = ((fahrenheit - 32) * 5) / 9

# Saída do resultado
print(fahrenheit,"°F equivalem a ",celsius, "°C")


print("-------------------------------------------------------------------------------")

# Entrada dos dados
valor = float(input("Digite o valor original da prestação: R$ "))
taxa = float(input("Digite a taxa de juros (%): "))
tempo = float(input("Digite o tempo de atraso (em meses): "))

# Cálculo da prestação em atraso
prestacao = valor + (valor * (taxa / 100) * tempo)

# Saída do resultado
print("O valor da prestação em atraso é: R$ ",prestacao)


# Entrada dos dados
votos_a = int(input("Digite a quantidade de votos válidos para o candidato A: "))
votos_b = int(input("Digite a quantidade de votos válidos para o candidato B: "))
votos_c = int(input("Digite a quantidade de votos válidos para o candidato C: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_branco = int(input("Digite a quantidade de votos em branco: "))

# Cálculo do total de eleitores
total_eleitores = votos_a + votos_b + votos_c + votos_nulos + votos_branco

# Cálculos dos percentuais
percentual_validos = ((votos_a + votos_b + votos_c) / total_eleitores) * 100
percentual_a = (votos_a / total_eleitores) * 100
percentual_b = (votos_b / total_eleitores) * 100
percentual_c = (votos_c / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_branco = (votos_branco / total_eleitores) * 100

# Saída dos resultados
print("\n--- Resultados da Eleição ---")
print(f"Total de eleitores: " ,total_eleitores)
print(f"Percentual de votos válidos:" ,percentual_validos, "%")
print(f"Percentual do candidato A: " , percentual_a , "%")
print(f"Percentual do candidato B: " , percentual_b, "%")
print(f"Percentual do candidato C: ", percentual_c, "%")
print(f"Percentual de votos nulos: " , percentual_nulos, "%")
print(f"Percentual de votos em branco: " , percentual_branco, "%")



print("-------------------------------------------------------------------------------")

# Entrada do raio da esfera
raio = float(input("Digite o raio da esfera (em metros): "))

# Cálculo do volume
pi = 3.14159
volume = (4 / 3) * pi * (raio ** 3)

# Saída do resultado
print("O volume da esfera é: " , volume, "m³")



print("-------------------------------------------------------------------------------")


# Entrada dos três valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

# Cálculo da soma dos quadrados
soma_quadrados = (A ** 2) + (B ** 2) + (C ** 2)

# Saída do resultado
print("A soma dos quadrados de ",A, B ,"e", C ,"é: " , soma_quadrados)



print("-------------------------------------------------------------------------------")

# Entrada dos quatro valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Cálculos
P = A * C  # Produto de A e C
S = B + D  # Soma de B e D

# Saída dos resultados
print("Produto de A e C (P): ", P)
print("Soma de B e D (S): ", S)


print("-------------------------------------------------------------------------------")


# Entrada dos dados
cotacao_dolar = float(input("Digite a cotação do dólar (US$): "))
valor_reais = float(input("Digite o valor em Reais (R$): "))

# Cálculo da conversão
valor_dolar = valor_reais / cotacao_dolar

# Saída do resultado
print("O valor de R$" ,valor_reais," equivale a US$" ,valor_dolar)


print("-------------------------------------------------------------------------------")


# Entrada dos dados
distancia_km = float(input("Digite a distância percorrida (km): "))
tempo_min = float(input("Digite o tempo gasto (minutos): "))

# Cálculo da velocidade em m/s
velocidade_ms = (distancia_km * 1000) / (tempo_min * 60)

# Saída do resultado
print("A velocidade do projétil é: ", velocidade_ms, "m/s")


print("-------------------------------------------------------------------------------")

# entrada dos dois valores
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))

# operações
soma = A + B
subtracao = A - B
multiplicacao = A * B
divisao = A / B \
    if B != 0\
    else "Indefinido (divisão por zero)"

# resultados
print("\n--- Resultados das Operações ---")
print("Adição (A + B): ",soma)
print("Subtração (A - B): ",subtracao)
print("Multiplicação (A × B): ",multiplicacao)
print(f"Divisão (A ÷ B):", divisao if isinstance(divisao, str) else divisao)


print("-------------------------------------------------------------------------------")

# Entrada dos três valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

# Cálculo do quadrado da soma
soma = A + B + C
quadrado_soma = soma ** 2

# Saída do resultado
print("O quadrado da soma de ", A , B, "e", C, "é:", quadrado_soma)


print("-------------------------------------------------------------------------------")

# Entrada dos dados
salario_atual = float(input("Digite o salário atual (R$): "))
percentual_reajuste = float(input("Digite o percentual de reajuste (%): "))

# Cálculo do novo salário
novo_salario = salario_atual * (1 + percentual_reajuste / 100)

# Saída do resultado
print("Novo salário após reajuste: R$ ",novo_salario)



print("-------------------------------------------------------------------------------")


# Entrada do valor do raio
raio = float(input("Digite o valor do raio da circunferência: "))

# Cálculo da área
pi = 3.14159265
area = pi * (raio ** 2)

# Saída do resultado
print("A área da circunferência é: ",area)

print("-------------------------------------------------------------------------------")

# Entrada dos dois valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verifica se B é zero para evitar divisão por zero
if B == 0:
    print("\nErro: Divisão por zero não é permitida!")
else:
    # Cálculo do quadrado da divisão
    divisao = A / B
    quadrado_divisao = divisao ** 2

    # Saída do resultado
    print("O quadrado da divisão de ",A, "por", B, "é:", quadrado_divisao)


    print("-------------------------------------------------------------------------------")


    # Entrada da medida em pés
    pes = float(input("Digite a medida em pés: "))

    # Cálculo da conversão para metros
    metros = pes * 0.3048

    # Saída do resultado
    print(pes, "pés equivalem a ",metros, "metros")

