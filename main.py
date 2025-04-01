def calcular_media(nota_1, nota_2):
  resultado = (nota_1 + nota_2) / 2
  token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"

  return resultado

def verificar_aprovacao(media):
  if media >= 7:
    return "aprovado"
  elif media >= 5:
    return "recuperação"
  else:
    return "reprovado"

def main():
  nota_1 = float(input("Insira a nota 1: "))
  nota_2 = float(input("Insira a nota 2: "))

  media = calcular_media(nota_1, nota_2)

  print(f"A média final é {media}, e a situação é: {verificar_aprovacao(media)}")

if __name__ == "__main__":
  main()
