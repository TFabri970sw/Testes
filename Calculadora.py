# Calculadora simples
def calculadora():
    operacao = input("5+5")
    num1 = float(input("5:"))
    num2 = float(input("5:"))
    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao =='-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        print("Operação invalida!") 
        return

    print("Reseultado:, resultado")               
