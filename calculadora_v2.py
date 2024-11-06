saida = ' '

#Função que recebe dois parâmetros e retorna a soma entre ambos
def adicao(a, b):
    return  a + b

#Função que recebe dois parâmetros e retorna a subtração entre ambos
def subtracao(a, b):
    return a - b

#Função que recebe dois parâmetros e retorna a multiplicação entre ambos
def multiplicacao(a, b):
    return a * b

#Função que recebe dois parâmetros e retorna a divisão entre ambos
#Verifica se um deles e 0, caso isso aconteça retorna uma mensagem de erro
def divisao(a, b):
    try: 
        return a / b   
    except ZeroDivisionError:
        print('Não foi possivel realizar a divisão por 0')

#Função que recebe três parâmetros: os dois números que serão usados para os cálculos e a operação matemática que se deseja realizar   
#Utilizo estruturas de condição, para verificar qual a operação desejada pelo usuário      
def calculadora(num1, num2, operacao):
    if operacao == '+':
        resultado = adicao(num1, num2)
    elif operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/':
        resultado = divisao(num1, num2)
    return resultado

#Laço while, que verifica se a variável saida é diferente de n
while saida != "n":
    #Pede ao usuário para digitar o primero número e armazena seu valor na variável
    numero1 = eval(input('Digite o primeiro número: '))
    #Pede ao usuário para digitar o segundo número e armazena seu valor na variável
    numero2 = eval(input('Digite o segundo número: '))
    #Pede ao usuário para digitar a escolha de uma operação matemática e armazena seu valor na variável
    operacao = str(input('Digite a operação metemática desejada: '))
    #Passa as variáveis para o método calculadora, armazenando o retorno dessa chamada na variável 
    resultado = calculadora(numero1, numero2, operacao)
    print(f'Resultado da Operação: {resultado}')
    #Variável que pergunta ao usuário si deseja continuar ou sair do programa
    #Utiliza o método lower() para converter a string para minúscula
    saida = str(input('Deseja continuar o programa? Digite S para continuar ou N para sair (S/N): ')).lower()
#Imprimi na tela que escolheu sair do programa
print('Você escolheu sair do programa!')
       