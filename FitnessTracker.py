nome_exercicios = []
tempo_gasto = []
calorias_queimadas = []
dia_da_semana = []

def cadastro_de_exercicios():
  while True:
    nome_exercicio = input("Digite o nome do exercício ou aperte a tecla 'Enter' para encerrar o cadastro: ")
    if nome_exercicio == "":
      break
    tempo_g = int(input("Digite o tempo gasto em minutos: "))
    calorias_q = int(input("Digite o número de calorias queimadas: "))
    dia_semana = input("Digite o dia da semana: ")
    nome_exercicios.append(nome_exercicio)
    tempo_gasto.append(tempo_g)
    calorias_queimadas.append(calorias_q)
    dia_da_semana.append(dia_semana)
    print("Exercício cadastrado com sucesso!")
  
def relatorio_diario():
  dia = input("Digite o dia da semana para o relatório: ")
  total_tempo = 0
  total_calorias = 0
  encontrou_exercicio = False

  print(f"\nExercícios realizados na {dia}:")
  for i in range(len(nome_exercicios)): 
      if dia_da_semana[i] == dia:  
          print(f"- {nome_exercicios[i]} | {tempo_gasto[i]} min | {calorias_queimadas[i]} kcal")
          total_tempo += tempo_gasto[i]
          total_calorias += calorias_queimadas[i]
          encontrou_exercicio = True

  if encontrou_exercicio:
      print(f"\nTotal de tempo gasto: {total_tempo} minutos")
      print(f"Total de calorias queimadas: {total_calorias} kcal\n")
  else:
      print("\nNenhum exercício realizado neste dia.\n")

def calculo_imc():
  p = float(input("Digite seu peso(kg): "))
  h = float(input("Digite sua altura(m): "))
  imc = p / (h * h)
  print(f"Seu IMC é: {imc:.2f}")
  if imc < 18.5:
    print("Você está abaixo do peso.\n")
  elif 18.5 <= imc < 24.9:
    print("Seu peso está normal.\n")
  elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.\n")
  elif 30 <= imc:
    print("Você está com obesidade.\n")

def meta_semanal():
  if len(calorias_queimadas) == 0:
    print("\nNenhum exercício cadastrado ainda.\n")
  meta = int(input("Digite a meta de calorias queimadas na semana: "))
  total = 0

  for i in range(len(calorias_queimadas)):
      total += calorias_queimadas[i]

  print(f"\nTotal de calorias queimadas na semana: {total} calorias")

  if total >= meta:
      print("Parabéns! Meta semanal atingida!")
  else:
      print(f"Meta não atingida. Faltam {meta - total} calorias para alcançar sua meta.")



def frase_motivacional():
  frases = ["Você consegue!", "Acredite em si mesmo!", "Siga em frente!", "Você é capaz de tudo!", "Não desista!", "Cada treino te deixa mais forte. Continue!", "Você é capaz de superar qualquer desafio!", "O esforço de hoje é a vitória de amanhã!", "Não desista! Pequenos passos levam ao sucesso.", "Sua única competição é com você mesmo!"]
  import random
  frase = random.choice(frases)
  print("\n", frase, "\n")

def media_calorias():
  if len(calorias_queimadas) == 0:
    print("\nNenhum exercício cadastrado ainda.\n")
    return
  soma = 0
  for i in range(len(calorias_queimadas)):
    soma += calorias_queimadas[i]
  media = soma / len(calorias_queimadas)
  print(f"\nA média de calorias queimadas é: {media:.2f}\n")

def codigo_de_barras():
  if len(nome_exercicios) == 0:
    print("\nNenhum exercício cadastrado ainda.\n")
    return
  print("\nGráfico de calorias queimadas:")
  for i in range(len(nome_exercicios)):
      grafico = '|' * (calorias_queimadas[i] // 10)
      print(f"{grafico} {nome_exercicios[i]}: {calorias_queimadas[i]} cal")

def menu():
  while True:
    print("\nMenu:")
    print("1 - Cadastrar exercício")
    print("2 - Relatório diário")
    print("3 - Meta semanal")
    print("4 - Cálculo de imc")
    print("5 - Frase motivacional")
    print("6 - Média de calorias queimadas")
    print("7 - Gráfico de calorias queimadas")
    print("8 - Sair")
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
      cadastro_de_exercicios()
    elif opcao == 2:
      relatorio_diario()
    elif opcao == 3:
      meta_semanal()
    elif opcao == 4:
      calculo_imc()
    elif opcao == 5:
      frase_motivacional()
    elif opcao == 6:
      media_calorias()
    elif opcao == 7:
      codigo_de_barras()
    elif opcao == 8:
      break
    else:
      print("Opção inválida!")


menu()
