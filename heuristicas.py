
def pecas_fora_do_lugar(estado, problema):
    pecas_deslocadas = 0
    estado_objetivo = problema._estado_objetivo  
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j] != estado_objetivo[i][j] and estado[i][j] != 0:
                pecas_deslocadas += 1
    return pecas_deslocadas

def distancia_manhattan(estado, problema):
    distancia_total = 0
    posicoes_objetivo = problema.posicoes_objetivo
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            peca = estado[i][j]
            if peca != 0:
                posicao_objeto_linha, posicao_objeto_coluna = posicoes_objetivo[peca]
                distancia_total += abs(i - posicao_objeto_linha) + abs(j - posicao_objeto_coluna)
    return distancia_total