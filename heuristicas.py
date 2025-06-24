
def pecas_fora_do_lugar(estado, problema):
    pecas_deslocadas = 0
    estado_objetivo = problema.estado_objetivo
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
                pos_obj_linha, pos_obj_coluna = posicoes_objetivo[peca]
                distancia_total += abs(i - pos_obj_linha) + abs(j - pos_obj_coluna)
    return distancia_total