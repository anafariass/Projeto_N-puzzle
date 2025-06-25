def busca_em_profundidade(problema):
    no_inicial = {
        'estado': problema.obter_estado_inicial(),
        'pai': None,
        'acao': None,
        'custo': 0
    }
    
    if problema.estado_objetivo(no_inicial['estado']):
        return no_inicial, 0
    
    fronteira = [no_inicial] 
    explorados = set()
    nos_expandidos = 0

    while fronteira:
        no_atual = fronteira.pop() 
        
        estado_atual = no_atual['estado']
        
        if estado_atual in explorados:
            continue
            
        explorados.add(estado_atual)
        nos_expandidos += 1
        
        if problema.estado_objetivo(estado_atual):
            return no_atual, nos_expandidos
        
        for estado_sucessor, acao, custo in reversed(problema.expandir(estado_atual)):
            if estado_sucessor not in explorados:
                no_filho = {
                    'estado': estado_sucessor,
                    'pai': no_atual,
                    'acao': acao,
                    'custo': no_atual['custo'] + custo
                }
                fronteira.append(no_filho)
                
    return None, nos_expandidos 