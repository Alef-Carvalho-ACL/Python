print("##### CALCULADORA #####")

print("SELECIONE UM NUMERO CORRESPONDENTE A OPERAÇÃO")

print("#1 - SOMA  #2 - SUBTRAÇÃO  #3 - MULTIPLICAÇÃO  #4 - DIVISÃO")

def ADD(nS1, nS2):
    tot = nS1 + nS2
    print("A SOMA DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

def SUB(nS1, nS2):
    tot = nS1 - nS2
    print("A SUBTRAÇÃO DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

def MUL(nS1, nS2):
    tot = nS1 * nS2
    print("A MULTIPLICAÇÃO DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

def DIV(nS1, nS2):
    tot = nS1 / nS2
    print("A DIVISÃO DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

nOpe = int(input("DIGITE UM NÚMERO CORRESPONDENTE A OPERAÇÃO: "))
nS1 = int(input("DIGITE UM NÚMERO: "))
nS2 = int(input("DIGITE OUTRO NÚMERO: "))

if nOpe == 1:
    ADD(nS1, nS2)
elif nOpe == 2:
    SUB(nS1, nS2)
elif nOpe == 3:
    MUL(nS1, nS2)
elif nOpe == 4:
    DIV(nS1, nS2)
else:
    print("OPÇÃO INVÁLIDA, INICIE NOVAMENTE")
