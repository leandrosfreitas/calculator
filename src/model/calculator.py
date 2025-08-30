import math
from .exceptions import DivisionByZeroError, NegativeNumberSqrtError

class Calculator:
    """
    Classe que representa a lógica de uma calculadora básica.

    Gerencia o estado do valor atual e permite operações matemáticas
    como adição, subtração, multiplicação, divisão, raiz quadrada e porcentagem.
    """

    def __init__(self):
        """
        Inicializa a calculadora.

        O valor inicial é 0.0 e não há operador armazenado.
        """
        self.current_value = 0.0  # Valor atual da calculadora
        self.operator = None       # Operador pendente (não utilizado nesta classe, mas mantido para compatibilidade)

    def add(self, value: float) -> float:
        """
        Adiciona um valor ao valor atual da calculadora.

        Args:
            value: Número a ser somado ao valor atual.

        Returns:
            float: O novo valor atual após a operação.
        """
        self.current_value += value
        return self.current_value

    def subtract(self, value: float) -> float:
        """
        Subtrai um valor do valor atual da calculadora.

        Args:
            value: Número a ser subtraído do valor atual.

        Returns:
            float: O novo valor atual após a operação.
        """
        self.current_value -= value
        return self.current_value

    def multiply(self, value: float) -> float:
        """
        Multiplica o valor atual da calculadora por um valor.

        Args:
            value: Número pelo qual multiplicar o valor atual.

        Returns:
            float: O novo valor atual após a multiplicação.
        """
        self.current_value *= value
        return self.current_value

    def divide(self, value: float) -> float:
        """
        Divide o valor atual da calculadora por um valor.

        Args:
            value: Número pelo qual dividir o valor atual.

        Returns:
            float: O novo valor atual após a divisão.

        Raises:
            DivisionByZeroError: Se o valor for zero, não é possível dividir.
        """
        if value == 0:
            raise DivisionByZeroError("Não é possível dividir por zero.")
        self.current_value /= value
        return self.current_value

    def sqrt(self) -> float:
        """
        Calcula a raiz quadrada do valor atual da calculadora.

        Returns:
            float: O valor atual atualizado com a raiz quadrada.

        Raises:
            NegativeNumberSqrtError: Se o valor atual for negativo.
        """
        if self.current_value < 0:
            raise NegativeNumberSqrtError("Não é possível calcular a raiz quadrada de um número negativo.")
        self.current_value = math.sqrt(self.current_value)
        return self.current_value

    def percent(self, base: float) -> float:
        """
        Calcula a porcentagem do valor atual em relação a um valor base.

        Fórmula: (current_value / 100) * base

        Args:
            base: Número em relação ao qual calcular a porcentagem.

        Returns:
            float: O valor atual atualizado com a porcentagem.
        """
        self.current_value = base * self.current_value / 100
        return self.current_value

    def clear(self):
        """
        Limpa o valor atual da calculadora, resetando para 0.0.

        Útil para iniciar um novo cálculo.
        """
        self.current_value = 0.0

    def __str__(self):
        """
        Retorna uma representação em string do valor atual da calculadora.

        Returns:
            str: Valor atual convertido para string.
        """
        return str(self.current_value)
