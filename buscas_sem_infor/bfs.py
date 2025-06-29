from collections import deque 

def busca_em_largura(problema):
    no_inicial = {
        'estado': problema.obter_estado_inicial(),
        'pai': None,
        'acao': None,
        'custo': 0,
        'profundidade': 0  
    }

    if problema.estado_objetivo(no_inicial['estado']):
        return no_inicial, 0, 0  

    fronteira = deque([no_inicial])
    explorados = {no_inicial['estado']}
    nos_expandidos = 0
    profundidade_maxima = 0  

    while fronteira:
        atual = fronteira.popleft()
        nos_expandidos += 1
        
        profundidade_maxima = max(profundidade_maxima, atual['profundidade'])

        for sucessor, acao, custo in problema.expandir(atual['estado']):
            if sucessor not in explorados:
                filho = {
                    'estado': sucessor,
                    'pai': atual,
                    'acao': acao,
                    'custo': atual['custo'] + custo,
                    'profundidade': atual['profundidade'] + 1 
                }

                if problema.estado_objetivo(sucessor):
                    profundidade_maxima = max(profundidade_maxima, filho['profundidade'])
                    return filho, nos_expandidos, profundidade_maxima

                fronteira.append(filho)
                explorados.add(sucessor)

    return None, nos_expandidos, profundidade_maxima
