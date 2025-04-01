def calcular_media(nota_1, nota_2):
  resultado = (nota_1 + nota_2) / 2

  return resultado

def main():
  nota_1 = float(input("Insira a nota 1: "))
  nota_2 = float(input("Insira a nota 2: "))

  media = calcular_media(nota_1, nota_2)

  print(f"A média final é {media}")

if __name__ == "__main__":
  main()
