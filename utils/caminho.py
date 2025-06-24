def obter_sequencia_de_acoes(no_final):
    caminho = []
    no_atual = no_final
    while no_atual['pai'] is not None:
        caminho.append(no_atual['acao'])
        no_atual = no_atual['pai']
    return caminho[::-1]

def obter_caminho_com_estados(no_final):

    caminho = []
    no_atual = no_final
    while no_atual is not None:
        caminho.append(no_atual['estado'])
        no_atual = no_atual['pai']
    return caminho[::-1]
