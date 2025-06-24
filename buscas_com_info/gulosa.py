import heapq

def busca_gulosa(problema, heuristica):
    no_inicial = {'ESTADO': problema.obter_estado_inicial(), 'PAI': None, 'ACAO': None, 'CUSTO': 0}
    
    fronteira = []
    prioridade = heuristica(no_inicial['ESTADO'], problema)
    contador = 0
    heapq.heappush(fronteira, (prioridade, contador, no_inicial))
    
    explorados = {no_inicial['ESTADO']}
    nos_expandidos = 0

    while fronteira:
        _, _, no_atual = heapq.heappop(fronteira)
        nos_expandidos += 1

        if problema.eh_estado_objetivo(no_atual['ESTADO']):
            return no_atual, nos_expandidos

        for estado_sucessor, acao, custo in problema.expandir(no_atual['ESTADO']):
            if estado_sucessor not in explorados:
                no_filho = {'ESTADO': estado_sucessor, 'PAI': no_atual, 'ACAO': acao, 'CUSTO': no_atual['CUSTO'] + custo}
                explorados.add(estado_sucessor)
                
                prioridade = heuristica(estado_sucessor, problema)
                contador += 1
                heapq.heappush(fronteira, (prioridade, contador, no_filho))
                
    return None, nos_expandidos