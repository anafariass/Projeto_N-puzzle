def busca_em_profundidade(problema):
    no_inicial = {
        'estado': problema.obter_estado_inicial(),
        'pai': None,
        'acao': None,
        'custo': 0,
        'profundidade': 0 
    }
    
    if problema.estado_objetivo(no_inicial['estado']):
        return no_inicial, 0, 0  
    
    fronteira = [no_inicial] 
    explorados = set()
    nos_expandidos = 0
    profundidade_maxima = 0  

    while fronteira:
        no_atual = fronteira.pop() 
        
        estado_atual = no_atual['estado']
        
        if estado_atual in explorados:
            continue
            
        explorados.add(estado_atual)
        profundidade_maxima = max(profundidade_maxima, no_atual['profundidade'])
        
        if problema.estado_objetivo(estado_atual):
            return no_atual, nos_expandidos, profundidade_maxima
        
        nos_expandidos += 1
        
        for estado_sucessor, acao, custo in problema.expandir(estado_atual):
            if estado_sucessor not in explorados:
                no_filho = {
                    'estado': estado_sucessor,
                    'pai': no_atual,
                    'acao': acao,
                    'custo': no_atual['custo'] + custo,
                    'profundidade': no_atual['profundidade'] + 1  
                }
                fronteira.append(no_filho)
                
    return None, nos_expandidos, profundidade_maxima 