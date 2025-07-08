import heapq

def busca_gulosa(problema, heuristica):
    no_inicial = {'estado': problema.obter_estado_inicial(),
                  'pai': None,
                  'acao': None,
                  'custo': 0} 
     
    fronteira = []
    prioridade = heuristica(no_inicial['estado'], problema) #1
    contador = 0
    heapq.heappush(fronteira, (prioridade, contador, no_inicial))
    
    explorados = {no_inicial['estado']} #2
    nos_expandidos = 0

    while fronteira:
        _, _, no_atual = heapq.heappop(fronteira) #3
        nos_expandidos += 1

        if problema.estado_objetivo(no_atual['estado']):#3
            return no_atual, nos_expandidos

        for estado_sucessor, acao, custo in problema.expandir(no_atual['estado']): #4
            if estado_sucessor not in explorados:#5
                no_filho = {'estado': estado_sucessor,
                            'pai': no_atual, 
                            'acao': acao, 
                            'custo': no_atual['custo'] + custo}
                
                explorados.add(estado_sucessor) #6
                
                prioridade = heuristica(estado_sucessor, problema) #7
                contador += 1
                heapq.heappush(fronteira, (prioridade, contador, no_filho))#8
                
    return None, nos_expandidos