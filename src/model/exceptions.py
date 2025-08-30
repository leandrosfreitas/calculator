class DivisionByZeroError(Exception):
    """
    Exceção personalizada para erros de divisão por zero.

    Esta exceção é levantada quando uma operação de divisão
    tenta dividir um número por zero, o que é matematicamente indefinido.

    Uso:
        raise DivisionByZeroError("Mensagem de erro")
    """
    pass


class NegativeNumberSqrtError(Exception):
    """
    Exceção personalizada para erros ao calcular a raiz quadrada de um número negativo.

    Esta exceção é levantada quando uma operação de raiz quadrada
    é chamada com um valor negativo, pois não é possível calcular
    a raiz quadrada de números negativos no conjunto dos números reais.

    Uso:
        raise NegativeNumberSqrtError("Mensagem de erro")
    """
    pass
