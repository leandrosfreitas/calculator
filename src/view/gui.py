import tkinter as tk

class Gui:
    """
    Representa a camada de visualização (View) da calculadora.

    Responsável por criar a interface gráfica, exibir o display,
    criar os botões e enviar os eventos de clique para o controlador.
    """
    def __init__(self, controller):
        """
        Inicializa a interface gráfica da calculadora.

        Configura a janela principal, o display e cria os botões.

        Args:
            controller: Instância do controlador (Controller) que lidará com os eventos
                        disparados pelos botões da interface.
        """
        self.controller = controller
        self.window = tk.Tk()
        self.display_var = tk.StringVar(value=0)  # Variável que controla o texto exibido no display
        self.window.title("Calculator")
        self.window.geometry("300x400")  # Define o tamanho da janela

        self._create_widgets()  # Cria o display e os botões

    def _create_widgets(self):
        """Cria e organiza o display e os botões da calculadora na interface gráfica."""

        # Cria e posiciona o display na parte superior da janela
        display = tk.Label(
            self.window,
            textvariable=self.display_var,
            font=("Arial", 24),
            anchor="e",  # Alinha o texto à direita
            padx=10,
            relief="sunken",
            bg="lightgray"
        )
        display.pack(fill="x", padx=10, pady=10)

        # Cria um frame para organizar os botões em uma grade
        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack()

        # Lista de botões da calculadora, organizada em ordem de criação
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            '%', 'sqrt', '='
        ]

        row = 0
        column = 0

        # Cria os botões dinamicamente e associa cada um ao método process_input do controlador
        for text_button in buttons:
            button = tk.Button(
                buttons_frame,
                text=text_button,
                font=("Arial", 18),
                command=lambda text=text_button: self.controller.process_input(text)
            )
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

            column += 1
            if column > 3:  # Limita 4 colunas por linha
                column = 0
                row += 1

        # Configura pesos para linhas e colunas para que os botões expandam proporcionalmente
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)

    def update_display(self, text: str):
        """
        Atualiza o texto do display da calculadora.

        Este método é chamado pelo controlador sempre que o valor
        mostrado no display deve ser alterado.

        Args:
            text: Novo texto a ser exibido no display.
        """
        self.display_var.set(text)

    def start(self):
        """
        Inicia o loop principal da interface gráfica.

        Este método mantém a janela aberta e processa eventos
        até que o usuário feche a aplicação.
        """
        self.window.mainloop()
