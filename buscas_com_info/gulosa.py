import heapq

def busca_gulosa(problema, heuristica):
    no_inicial = {'estado': problema.obter_estado_inicial(), 'pai': None, 'acao': None, 'custo': 0} # eh como o no eh representado
     
    fronteira = []
    prioridade = heuristica(no_inicial['estado'], problema)
    contador = 0
    heapq.heappush(fronteira, (prioridade, contador, no_inicial))
    
    explorados = {no_inicial['estado']}
    nos_expandidos = 0

    while fronteira:
        _, _, no_atual = heapq.heappop(fronteira)
        nos_expandidos += 1

        if problema.estado_objetivo(no_atual['estado']):
            return no_atual, nos_expandidos

        for estado_sucessor, acao, custo in problema.expandir(no_atual['estado']):
            if estado_sucessor not in explorados:
                no_filho = {'estado': estado_sucessor,
                            'pai': no_atual, 
                            'acao': acao, 
                            'custo': no_atual['custo'] + custo}
                
                explorados.add(estado_sucessor)
                
                prioridade = heuristica(estado_sucessor, problema)
                contador += 1
                heapq.heappush(fronteira, (prioridade, contador, no_filho))
                
    return None, nos_expandidos