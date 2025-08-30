import unittest
from src.model.calculator import Calculator
from src.controller.controller import Controller

class MockGui:
    """
    Mock da GUI para testar o Controller sem abrir a interface gráfica.
    
    Simula apenas a atualização do display.
    """
    def __init__(self):
        self.display_var = type('', (), {})()  # cria um objeto vazio para display_var
        self.display_var.get = lambda: "0"
        self.display_var.set = lambda x: setattr(self, "_last_value", x)
        self._last_value = None

    def update_display(self, text):
        """Simula o método da GUI que atualiza o display."""
        self._last_value = text


class TestController(unittest.TestCase):
    """
    Conjunto de testes unitários para a classe Controller.

    Verifica se o Controller processa números, operadores e
    atualiza corretamente o display da GUI.
    """

    def setUp(self):
        """Configura um novo Controller com Calculator e MockGui antes de cada teste."""
        self.calc = Calculator()
        self.controller = Controller(self.calc)
        self.gui = MockGui()
        self.controller.set_gui(self.gui)

    def test_process_number(self):
        """Testa se o Controller processa a entrada de um número corretamente."""
        self.gui.display_var.get = lambda: "0"
        self.controller._process_number("5")
        self.assertEqual(self.gui._last_value, "5")

    def test_process_addition(self):
        """Testa a operação de adição pelo Controller."""
        self.gui.display_var.get = lambda: "10"
        self.controller._process_operator("+")
        self.gui.display_var.get = lambda: "20"
        self.controller._process_equals()
        self.assertEqual(self.calc.current_value, 30)

    def test_process_subtraction(self):
        """Testa a operação de subtração pelo Controller."""
        self.gui.display_var.get = lambda: "50"
        self.controller._process_operator("-")
        self.gui.display_var.get = lambda: "20"
        self.controller._process_equals()
        self.assertEqual(self.calc.current_value, 30)

if __name__ == "__main__":
    unittest.main()
