import heapq

def busca_a_estrela(problema, heuristica): #1
    no_inicial = {'estado': problema.obter_estado_inicial(),
                  'pai': None,
                  'acao': None,
                  'custo': 0}
    
    fronteira = [] #2
    prioridade = no_inicial['custo'] + heuristica(no_inicial['estado'], problema) # f(n) = g(n) + h(n)
    contador = 0 
    heapq.heappush(fronteira, (prioridade, contador, no_inicial)) #4
    explorados = {no_inicial['estado']: 0}#5
    nos_expandidos = 0

    while fronteira: #6
        _, _, no_atual = heapq.heappop(fronteira)#7
        nos_expandidos += 1

        if problema.estado_objetivo(no_atual['estado']):#8
            return no_atual, nos_expandidos

        for estado_sucessor, acao, custo in problema.expandir(no_atual['estado']): #9
            novo_custo = no_atual['custo'] + custo #10
            if estado_sucessor not in explorados or novo_custo < explorados[estado_sucessor]: #11
                explorados[estado_sucessor] = novo_custo #12
                prioridade = novo_custo + heuristica(estado_sucessor, problema)#13
                no_filho = {'estado': estado_sucessor, 'pai': no_atual, 'acao': acao, 'custo': novo_custo}#14
                contador += 1
                heapq.heappush(fronteira, (prioridade, contador, no_filho)) #15
                
    return None, nos_expandidos 