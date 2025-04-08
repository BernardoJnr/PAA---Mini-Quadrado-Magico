def checa_validade(matriz, soma_magico=15):
    
    # 1. Verifica as somas das linhas
    for linha in range(3):
        if sum(matriz[linha]) != soma_magico:
            return False

    # 2. Verifica as somas das colunas
    for coluna in range(3):
        column_sum = matriz[0][coluna] + matriz[1][coluna] + matriz[2][coluna]
        if column_sum != soma_magico:
            return False

    # 3. Verifica a soma da diagonal principal 
    if matriz[0][0] + matriz[1][1] + matriz[2][2] != soma_magico:
        return False

    # 4. Verifica a soma da diagonal secundária 
    if matriz[0][2] + matriz[1][1] + matriz[2][0] != soma_magico:
        return False

    # Se passou por todas as verificações, a matriz é um quadrado mágico válido
    return True

def resolve_quadrado(matriz, num_usado, index):
    
    # Se o índice é 9, significa que todas as 9 células foram preenchidas.
    if index == 9:
        return checa_validade(matriz) 
        """
        DESCOMENTE o if para imprimir todas as soluções possíveis 
        if checa_validade(matriz):
            print("\nSolução encontrada:")
            for row in matriz:
                print(f"[{row[0]:^3} {row[1]:^3} {row[2]:^3}]")
        return 
        """

    # --- Passo Recursivo ---
    linha = index // 3  # Divisão inteira dá a linha (0, 1 ou 2)
    coluna = index % 3   # Resto da divisão dá a coluna (0, 1 ou 2)

    # Tenta colocar cada número de 1 a 9 na célula atual 
    for num in range(1, 10):
        # Verifica se o número 'num' ainda NÃO foi usado
        if not num_usado[num]:
            # Coloca o número 'num' na célula atual da matriz
            matriz[linha][coluna] = num
            # Marca o número 'num' como usado
            num_usado[num] = True

            # Chama recursivamente a função para preencher a PRÓXIMA célula (index + 1)
            if resolve_quadrado(matriz, num_usado, index + 1):
                return True  # Solução encontrada! Propaga o True para cima na pilha de chamadas.

            #Desfazer (Backtrack)
            # Se a chamada recursiva retornou False, significa que colocar 'num'
            # nesta posição não levou a uma solução válida.
            matriz[linha][coluna] = 0          # Limpa a célula, voltando ao estado anterior
            num_usado[num] = False # Marca o número como não usado novamente
    return False


# 1. Inicializa a matriz 3x3 com zeros 
matriz = [[0 for _ in range(3)] for _ in range(3)]

# 2. Inicializa a lista para rastrear os números usados (1 a 9)
#    Todos começam como False (não usados).
used = [False] * 10

# 3. Chama a função de backtracking começando da primeira célula (índice 0)
resolve_quadrado(matriz, used, 0)

#COMENTE QUANDO FOR EXIBIR TODAS AS SOLUÇÕES POSSIVEIS
for row in matriz:
    print(f"[{row[0]:^3} {row[1]:^3} {row[2]:^3}]")