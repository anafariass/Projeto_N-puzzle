

def busca_em_profundidade(problema):
    no_inicial = {'estado': problema.obter_estado_inicial(),
                  'pai': None,
                  'acao': None,
                  'custo': 0}
    
    fronteira = [no_inicial]
    explorados = set()
    nos_expandidos = 0

    while fronteira:
        no_atual = fronteira.pop() 
        nos_expandidos += 1
        
        estado_atual = no_atual['estado']
        
        if problema.estado_objetivo(estado_atual):
            return no_atual
        
        if estado_atual not in explorados:
            explorados.add(estado_atual)
            for estado_sucessor, acao, custo in reversed(problema.expandir(estado_atual)):
                no_filho = {'estado': estado_sucessor,
                            'pai': no_atual,
                            'acao': acao,
                            'custo': no_atual['custo'] + custo}
                
                fronteira.append(no_filho)
                
    return None, nos_expandidos 