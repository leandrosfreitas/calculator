print("selecione o número da operação desejada:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisáo")
operacao = int(input("Digite sua opção(1/2/3/4): "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if operacao == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif operacao == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif operacao == 3:
    print(num1, "*", num2, "=", num1 * num2)
elif operacao == 4:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Opção inválida")