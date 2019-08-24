#92446 David Alexandre Barreiro Baptista


#converte_tuplo: tuplo -> lista
def converte_tuplo(tuplo):
    """Recebe um tuplo, converte os seus elementos para lista e devolve uma lista contento esses elementos"""

    lista = []

    for t in tuplo:
        lista.append(list(t))

    return lista

#converte_lista: lista -> tuplo
def converte_lista(lista):
    """ Recebe uma lista, converte os seus elementos para tuplo e devolve um tuplo contento esses elementos"""
    tuplo = []

    for l in lista:
        tuplo.append(tuple(l))

    return tuple(tuplo)

#troca_bits: lista n p -> None
def troca_bits(lista, n, p):
    """ Recebe uma lista e os indices dos elementos a trocar (n - indice do tuplo, p - indice do elemento) e altera
    os valores de 1 para 0 e 0 para 1 (troca o estado do bit)"""
    if lista[n][p] == 0:
        lista[n][p] = 1
    elif lista[n][p] == 1:
        lista[n][p] = 0

#porta_startup: tabuleiro x type -> lista
def porta_startup(tabuleiro, x, type):
    """Recebe o tabuleiro, a direcao da porta (x) a executar e o tipo da porta (type). Executa a funcao eh_tabuleiro() e valida o valor
    de input da direcao, fazendo raise do erro caso estes sejam invalidos
    Caso o input seja valido, devolve o tabuleiro em lista, ao executar a funcao converte_tuplo()"""
    if not eh_tabuleiro(tabuleiro) or (x != 'E' and x != 'D'):
        raise ValueError("porta_" + type + ": um dos argumentos e invalido")

    lista = converte_tuplo(tabuleiro)

    return lista

#seleciona_bits: tabuleiro x type -> None
def seleciona_bits(tabuleiro, x, type):
    """Recebe como input o tabuleiro a alterar, a direcao da porta (x) e o tipo da porta (type).
    Seleciona os bits a alterar e executa a funcao troca_bits() que procede a troca dos valores dos mesmos"""

    # Variaveis usadas para selecionar os indices corretos a alterar
    c = 1
    p = 1

    # Caso seja a porta Z a ser executada, as variaveis sao alteradas de modo a alterar as "linhas" de bits exteriores
    if type == 'z':
        c += 1
        p = 0

    # Caso tenham sido escolhidos os bits da direita para ser alterados. A variavel n circula por todos os tuplos
    # exceto caso x = 'e' onde esta circula pelos elementos do tuplo 0
    if x == 'D':
        n = 0
        while n <= 2:
            if n != 2:
                troca_bits(tabuleiro, n, c)
            else:
                troca_bits(tabuleiro, n, c - 1)
            n += 1
    # Caso tenham sido escolhidos os bits da esquerda para ser alterados
    elif x == 'E':
        n = 0
        while n <= 2:
            troca_bits(tabuleiro, p, n)

            n += 1

#eh_tabuleiro: tuplo -> booleano
def eh_tabuleiro(tuplo):
    """ Recebe uma variavel de qualquer tipo, verifica se e um tuplo com 3 elementos, que tambem sao tuplos onde os 2
     primeiros tuplos tem 3 elementos e o ultimo tuplo tem 2 elementos"""

    # Recebe um valor e devolve True ou False caso seja do tipo tuple ou nao
    def is_tuplo(valor):
        if isinstance(valor, tuple):
            return True
        else:
            return False

    if not is_tuplo(tuplo):
        return False

    if len(tuplo) != 3:
        return False

    n = 1

    for t in tuplo:
        if not is_tuplo(t):
            return False
        if n <= 2:
            if len(t) != 3:
                return False
            for e in t:
                if isinstance(e, int):
                    if e not in (-1,0,1) :
                        return False
                else:
                    return False
        elif n == 3:
            if len(t) != 2:
                return False
            for e in t:
                if isinstance(e, int):
                    if e not in (-1,0,1):
                        return False
                else:
                    return False
        n += 1

    return True

#tabuleiro_str: tabuleiro -> string
def tabuleiro_str(tabuleiro):
    """Recebe um tuplo (tabuleiro) com os valores do tabuleiro, executa a funcao converte_tuplo para ter o seu valor
    numa variavel do tipo lista de modo a alterar os valores desta, de -1 para x que corresponde a representacao
    grafica de um bit incerto. Apos trocar os valores, devolve uma string com o desenho do tabuleiro e os valores
    correspondentes nas posicoes corretas"""

    # Executa a validacao do tuplo
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("tabuleiro_str: argumento invalido")

    lista = converte_tuplo(tabuleiro)
    n = 0

    # Ciclo destinado a troca do valor -1 pela letra 'x'
    while n <= 2:
        c = 0

        if n == 0 or n == 1:
            while c <= 2:
                if lista[n][c] == -1:
                    lista [n][c] = 'x'
                c += 1
        else:
            while c <= 1:
                if lista[n][c] == -1:
                    lista [n][c] = 'x'
                c += 1
        n += 1

    return '+-------+\n|...' + str(lista[0][2]) + '...|\n|..' + str(lista[0][1]) + '.' + str(lista[1][2]) + '..|\n|.' +\
           str(lista[0][0]) +'.' + str(lista[1][1]) + '.' + str(lista[2][1]) + '.|\n|..' + str(lista[1][0]) + '.' \
           + str(lista[2][0]) +'..|\n+-------+'


#tabuleiros_iguais: tab1 tab2 -> booleano
def tabuleiros_iguais(tab1, tab2):
    """ Recebe dois tuplos com valroes de tabuleiros (tab1, tab2), executa a validacao dos mesmos
    com a funcao eh_tabuleiro() e devolve True ou False caso sejam iguais ou diferentes respetivamente"""
    if not eh_tabuleiro(tab1) or not eh_tabuleiro(tab2):
        raise ValueError("tabuleiros_iguais: um dos argumentos nao e tabuleiro")

    if tab1 == tab2:
        return True
    else:
        return False

#porta_x: tabuleiro x -> lista
def porta_x(tabuleiro, x):
    """Recebe um tuplo com os valores do tabuleiro a executar a troca e o lado(x) esquerda ('E') ou direita ('D')
    Executa a funcao porta_startup e fornece a lista recebida a funcao seleciona_bits() efetuando a troca, isto e
    trocar o estado dos bits das linhas diagonais interiores (sem alterar os bits incertos)
    Devolve o tabuleiro com as trocas efetuadas"""
    lista = porta_startup(tabuleiro, x, 'x')

    seleciona_bits(lista, x, 'x')

    return converte_lista(lista)

#porta_z: tabuleiro x -> lista
def porta_z(tabuleiro, x):
    """Recebe um tuplo com os valores do tabuleiro a executar a troca e o lado(x) esquerda ('E') ou direita ('D')
     Executa a funcao porta_startup e fornece a lista recebida a funcao seleciona_bits() efetuando a troca, isto e
     trocar o estado dos bits das linhas diagonais exteriores (sem alterar os bits incertos)
     Devolve o tabuleiro com as trocas efetuadas"""

    lista = porta_startup(tabuleiro, x, 'z')

    seleciona_bits(lista, x, 'z')

    return converte_lista(lista)

# porta_h: tabuleiro x -> lista
def porta_h(tabuleiro, x):
    """Recebe um tuplo com os valores do tabuleiro a executar a troca e o lado(x) esquerda ('E') ou direita ('D')
    Executa a funcao porta_startup e fornece a lista recebida a funcao seleciona_bits() efetuando a troca, isto e
    trocar as linhas exterior e interior do lado escolhido. Devolve o tabuleiro com as trocas efetuadas"""

    lista = porta_startup(tabuleiro, x, 'h')

    if x == 'D':
        n = 0
        while n <= 2:
            if n != 2:
                lista[n][1], lista[n][2] = lista[n][2], lista[n][1]
            else:
                lista[n][0], lista[n][1] = lista[n][1], lista[n][0]
            n += 1
    elif x == 'E':
        lista[0][0], lista[0][1], lista[0][2], lista[1][0], lista[1][1], lista[1][2] \
            = lista[1][0], lista[1][1], lista[1][2],  lista[0][0], lista[0][1], lista[0][2]

    return converte_lista(lista)