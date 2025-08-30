from model.calculator import Calculator
from view.gui import Gui
from model.exceptions import DivisionByZeroError, NegativeNumberSqrtError

class Controller:
    """
    Controlador da aplicação da calculadora.

    Faz a ponte entre a lógica de negócio (Calculator) e a interface gráfica (GUI),
    processando entradas do usuário e atualizando o display.
    """
    def __init__(self, calculator: Calculator) -> None:
        """
        Inicializa o controlador com a instância da calculadora.

        Args:
            calculator: Instância da classe Calculator, que contém a lógica da calculadora.
        """
        self.calculator: Calculator = calculator
        self.first_number: float | None = None        # Armazena o primeiro número de uma operação
        self.pending_operator: str | None = None      # Armazena o operador pendente
        self.new_number_started: bool = False         # Indica se o usuário começou a digitar um novo número

    def set_gui(self, gui: Gui) -> None:
        """
        Conecta a interface gráfica (GUI) ao controlador após sua criação.

        Args:
            gui: Instância da classe Gui.
        """
        self.gui: Gui = gui

    def process_input(self, value: str) -> None:
        """
        Processa a entrada do usuário vinda da interface gráfica.

        Dependendo do valor, chama os métodos internos para processar números,
        operadores, igual ou limpar a calculadora.

        Args:
            value: Valor do botão clicado pelo usuário.
        """
        try:
            if value.isdigit() or value == '.':
                self._process_number(value)
            elif value in ['+', '-', '*', '/', 'sqrt', '%']:
                self._process_operator(value)
            elif value == "=":
                self._process_equals()
            elif value == "C":
                self._process_clear()
        except (DivisionByZeroError, NegativeNumberSqrtError) as e:
            # Exibe mensagem de erro no display e reseta a calculadora
            self.gui.update_display(str(e))
            self.calculator.clear()
            self.first_number = None
            self.pending_operator = None
            self.new_number_started = True

    def _process_number(self, number: str) -> None:
        """
        Atualiza o display com o número digitado.

        Se um novo número está sendo iniciado, substitui o display atual.
        Impede múltiplos zeros à esquerda e múltiplos pontos decimais.

        Args:
            number: Número ou ponto digitado pelo usuário.
        """
        current_display = self.gui.display_var.get()

        if self.new_number_started:
            self.gui.update_display(number)
            self.new_number_started = False
            return

        if current_display in ("0", "0.0"):
            current_display = ""

        if number == '.' and '.' in current_display:
            return

        self.gui.update_display(current_display + number)

    def _process_operator(self, operator: str) -> None:
        """
        Processa um operador ou operação especial.

        Operadores suportados: +, -, *, /  
        Operações especiais: sqrt (raiz quadrada), % (porcentagem)

        Args:
            operator: Operador clicado pelo usuário.
        """
        display_value = float(self.gui.display_var.get())
        
        # Operação de raiz quadrada: aplica ao valor atual e atualiza display
        if operator == 'sqrt':
            self.calculator.current_value = display_value
            self.calculator.sqrt()
            self.gui.update_display(str(self.calculator.current_value))
            self.new_number_started = True
            return
        
        # Operação de porcentagem
        elif operator == '%':
            self.calculator.current_value = display_value

            if self.pending_operator in ['+', '-']:
                # Percentual relativo ao primeiro número da operação
                base = self.first_number if self.first_number is not None else display_value
                self.calculator.percent(base)
            elif self.pending_operator in ['*', '/']:
                # Percentual como fração (divide por 100)
                self.calculator.current_value /= 100

            self.gui.update_display(str(self.calculator.current_value))
            self.new_number_started = True
            return

        # Se for a primeira operação, armazena número e operador
        if self.first_number is None:
            self.first_number = display_value
            self.pending_operator = operator
        else:
            # Executa operação pendente e atualiza o primeiro número
            self._execute_operation(self.first_number, self.pending_operator, display_value)
            self.first_number = self.calculator.current_value
            self.pending_operator = operator
            
        self.new_number_started = True

    def _process_equals(self) -> None:
        """
        Executa a operação pendente quando o botão de igual é pressionado.

        Atualiza o display com o resultado e reseta operadores pendentes.
        """
        if self.pending_operator is None:
            return
            
        second_number = float(self.gui.display_var.get())
        self._execute_operation(self.first_number, self.pending_operator, second_number)
        
        # Resetando estados após operação
        self.first_number = None
        self.pending_operator = None
        self.new_number_started = True

    def _process_clear(self) -> None:
        """
        Limpa a calculadora e reseta todos os estados.

        Atualiza o display para "0".
        """
        self.calculator.clear()
        self.first_number = None
        self.pending_operator = None
        self.new_number_started = False
        self.gui.update_display("0")

    def _execute_operation(self, a: float, operator: str, b: float) -> None:
        """
        Executa a operação selecionada na instância Calculator e atualiza o display.

        Args:
            a: Primeiro número da operação.
            operator: Operador a ser aplicado.
            b: Segundo número da operação.
        """
        if operator == '+':
            self.calculator.current_value = a
            self.calculator.add(b)
        elif operator == '-':
            self.calculator.current_value = a
            self.calculator.subtract(b)
        elif operator == '*':
            self.calculator.current_value = a
            self.calculator.multiply(b)
        elif operator == '/':
            self.calculator.current_value = a
            self.calculator.divide(b)
        
        self.gui.update_display(str(self.calculator.current_value))
