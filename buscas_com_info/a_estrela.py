import heapq

def busca_a_estrela(problema, heuristica):
    no_inicial = {'estado': problema.obter_estado_inicial(), 'pai': None, 'acao': None, 'custo': 0}
    
    fronteira = []
    prioridade = no_inicial['custo'] + heuristica(no_inicial['estado'], problema)
    contador = 0
    heapq.heappush(fronteira, (prioridade, contador, no_inicial))
    
    explorados = {no_inicial['estado']: 0}
    nos_expandidos = 0

    while fronteira:
        _, _, no_atual = heapq.heappop(fronteira)
        nos_expandidos += 1

        if problema.estado_objetivo(no_atual['estado']):
            return no_atual, nos_expandidos

        for estado_sucessor, acao, custo in problema.expandir(no_atual['estado']):
            novo_custo = no_atual['custo'] + custo
            if estado_sucessor not in explorados or novo_custo < explorados[estado_sucessor]:
                explorados[estado_sucessor] = novo_custo
                prioridade = novo_custo + heuristica(estado_sucessor, problema)
                no_filho = {'estado': estado_sucessor, 'pai': no_atual, 'acao': acao, 'custo': novo_custo}
                contador += 1
                heapq.heappush(fronteira, (prioridade, contador, no_filho))
                
    return None, nos_expandidos 