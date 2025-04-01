import unittest

import main

class TestMain(unittest.TestCase):
  def test_verificar_aprovacao(self):
    casos_de_teste = [
      (0, "reprovado"),
      (1, "reprovado"),
      (2, "reprovado"),
      (3, "reprovado"),
      (4, "reprovado"),
      (5, "recuperação"),
      (6, "recuperação"),
      (7, "aprovado"),
      (8, "aprovado"),
      (9, "aprovado"),
      (10, "aprovado"),
    ]

    for nota, expected in casos_de_teste:
      result = main.verificar_aprovacao(nota)

      self.assertEqual(
        result, 
        expected, 
        msg=f"O resultado para nota '{nota}' está errado",
      )

if __name__ == '__main__':
  unittest.main()
