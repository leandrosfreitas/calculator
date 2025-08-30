import unittest
from src.model.calculator import Calculator
from src.model.exceptions import DivisionByZeroError, NegativeNumberSqrtError

class TestCalculator(unittest.TestCase):
    """
    Conjunto de testes unitários para a classe Calculator.

    Verifica se as operações matemáticas básicas, percentuais,
    raiz quadrada e tratamento de exceções funcionam corretamente.
    """

    def setUp(self):
        """Configura um novo objeto Calculator antes de cada teste."""
        self.calc = Calculator()

    def test_add(self):
        """Testa a operação de adição."""
        self.calc.current_value = 5
        result = self.calc.add(3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        """Testa a operação de subtração."""
        self.calc.current_value = 10
        result = self.calc.subtract(4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        """Testa a operação de multiplicação."""
        self.calc.current_value = 7
        result = self.calc.multiply(3)
        self.assertEqual(result, 21)

    def test_divide(self):
        """Testa a operação de divisão."""
        self.calc.current_value = 20
        result = self.calc.divide(4)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        """Verifica se a divisão por zero lança a exceção correta."""
        self.calc.current_value = 10
        with self.assertRaises(DivisionByZeroError):
            self.calc.divide(0)

    def test_sqrt(self):
        """Testa o cálculo da raiz quadrada de um número positivo."""
        self.calc.current_value = 16
        result = self.calc.sqrt()
        self.assertEqual(result, 4)

    def test_sqrt_negative(self):
        """Verifica se calcular a raiz quadrada de número negativo lança a exceção correta."""
        self.calc.current_value = -9
        with self.assertRaises(NegativeNumberSqrtError):
            self.calc.sqrt()

    def test_percent(self):
        """Testa o cálculo de porcentagem em relação a uma base."""
        self.calc.current_value = 10
        result = self.calc.percent(200)  # 10% de 200
        self.assertEqual(result, 20)

    def test_clear(self):
        """Verifica se o método clear reseta o valor atual para 0.0."""
        self.calc.current_value = 50
        self.calc.clear()
        self.assertEqual(self.calc.current_value, 0.0)

if __name__ == "__main__":
    unittest.main()
