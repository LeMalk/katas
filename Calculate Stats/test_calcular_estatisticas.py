import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calcular_estatisticas import calcular_estatisticas

class TestCalcularEstatisticas(unittest.TestCase):
    def test_sequencia_vazia(self):
        self.assertEqual(calcular_estatisticas([]), "A sequência está vazia")

    def test_sequencia_exemplo(self):
        sequencia = [6, 9, 15, -2, 92, 11]
        resultado_esperado = {
            "valor_minimo": -2,
            "valor_maximo": 92,
            "numero_elementos": 6,
            "valor_medio": 21.833333333333332
        }
        self.assertEqual(calcular_estatisticas(sequencia), resultado_esperado)

if __name__ == '__main__':
    unittest.main()