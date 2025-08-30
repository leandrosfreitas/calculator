import sys
sys.path.append('src')  # Adiciona o diretório 'src' ao path para permitir importações locais

from model.calculator import Calculator
from view.gui import Gui
from controller.controller import Controller

def main():
    """
    Função principal que inicializa e executa a aplicação da calculadora.

    Passos:
        1. Cria a instância do modelo (Calculator).
        2. Cria o controlador (Controller) passando apenas o modelo.
        3. Cria a interface gráfica (GUI) passando o controlador.
        4. Conecta a GUI ao controlador.
        5. Inicia o loop principal da interface gráfica.
    """
    # Cria a instância do modelo da calculadora
    calculator = Calculator()

    # Cria o controlador da aplicação, responsável por ligar a lógica do modelo à GUI
    controller = Controller(calculator)  # Passa apenas o modelo

    # Cria a interface gráfica, passando o controlador para receber os eventos
    gui = Gui(controller)                

    # Conecta a GUI ao controlador, permitindo que o controlador atualize o display
    controller.set_gui(gui)              

    # Inicia o loop principal da interface gráfica (Tkinter)
    gui.start()                          

if __name__ == "__main__":
    # Executa a função principal apenas se o script for rodado diretamente
    main()
