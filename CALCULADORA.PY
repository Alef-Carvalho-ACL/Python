print("\n##### CALCULADORA #####")

print("\nSELECIONE UM NUMERO CORRESPONDENTE A OPERAÇÃO\n")

print("#1 - SOMA  #2 - SUBTRAÇÃO  #3 - MULTIPLICAÇÃO  #4 - DIVISÃO")

def ADD(nS1, nS2):
    tot = nS1 + nS2
    print("\nA SOMA DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

def SUB(nS1, nS2):
    tot = nS1 - nS2
    print("\nA SUBTRAÇÃO DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

def MUL(nS1, nS2):
    tot = nS1 * nS2
    print("\nA MULTIPLICAÇÃO DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

def DIV(nS1, nS2):
    tot = nS1 / nS2
    print("\nA DIVISÃO DOS NÚMEROS ({} E {}) É: {}".format(nS1, nS2, tot))

nOpe = int(input("\nDIGITE UM NÚMERO CORRESPONDENTE A OPERAÇÃO ( 1 / 2 / 3 / 4 ): "))
nS1 = int(input("\nDIGITE UM NÚMERO: "))
nS2 = int(input("\nDIGITE OUTRO NÚMERO: "))

if nOpe == 1:
    ADD(nS1, nS2)
elif nOpe == 2:
    SUB(nS1, nS2)
elif nOpe == 3:
    MUL(nS1, nS2)
elif nOpe == 4:
    DIV(nS1, nS2)
else:
    print("\nOPÇÃO INVÁLIDA, INICIE NOVAMENTE")
