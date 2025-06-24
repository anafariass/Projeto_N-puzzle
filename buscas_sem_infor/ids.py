import sys

def busca_com_limite_de_profundidade(problema, limite):
    no_inicial = {'estado': problema.obter_estado_inicial(),
                  'pai': None,
                  'acao': None,
                  'custo': 0}
    
    fronteira = [no_inicial] 
    explorados = {}
    nos_expandidos = 0
    ocorreu_cutoff = False

    while fronteira:
        no_atual = fronteira.pop()
        nos_expandidos += 1

        if problema.estado_objetivo(no_atual['estado']):
            return no_atual, nos_expandidos, False

     
        if no_atual['estado'] in explorados and no_atual['custo'] >= explorados[no_atual['estado']]:
            continue
        
        explorados[no_atual['estado']] = no_atual['custo']

        
        if no_atual['custo'] < limite:
            for estado_sucessor, acao, custo in reversed(problema.expandir(no_atual['estado'])):
                no_filho = {'estado': estado_sucessor, 'pai': no_atual, 'acao': acao, 'custo': no_atual['custo'] + custo}
                fronteira.append(no_filho)
        else:
           
            ocorreu_cutoff = True

    return None, nos_expandidos, ocorreu_cutoff

def busca_em_aprofundamento_iterativo(problema):
    nos_expandidos_total = 0
    for profundidade in range(sys.maxsize):
        resultado_no, nos_expandidos_iter, houve_cutoff = busca_com_limite_de_profundidade(problema, profundidade)
        
        nos_expandidos_total += nos_expandidos_iter
        if resultado_no is not None:
            return resultado_no, nos_expandidos_total
      
        elif not houve_cutoff:
            return None, nos_expandidos_total
            
    return None, nos_expandidos_total