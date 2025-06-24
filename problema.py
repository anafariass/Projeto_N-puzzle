
class ProblemaNPuzzle:
    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.posicoes_objetivo = self._calcular_posicoes_objetivo()

    def obter_estado_inicial(self):
        return self.estado_inicial

    def estado_objetivo(self, estado):
        return estado == self.estado_objetivo

    def expandir(self, estado):
        sucessores = []
        linha, coluna = self._encontrar_posicao(estado, 0)
        direcoes = {
            'Cima': (linha - 1, coluna),
            'Baixo': (linha + 1, coluna),
            'Esquerda': (linha, coluna - 1),
            'Direita': (linha, coluna + 1)
        }

        for acao, (nova_linha, nova_coluna) in direcoes.items():
            if 0 <= nova_linha < len(estado) and 0 <= nova_coluna < len(estado[0]):
                novo_estado = [list(l) for l in estado] 
                novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = \
                    novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
                novo_estado_tupla = tuple(tuple(l) for l in novo_estado)
                sucessores.append((novo_estado_tupla, acao, 1)) 

        return sucessores

    def _encontrar_posicao(self, estado, peca):
        for linha_atual, linha in enumerate(estado):
            for coluna_atual, valor in enumerate(linha):
                if valor == peca:
                    return (linha_atual, coluna_atual)
        return None

    def _calcular_posicoes_objetivo(self):
        posicoes = {}
        for linha_atual, linha in enumerate(self.estado_objetivo):
            for coluna_atual, peca in enumerate(linha):
                if peca != 0:
                    posicoes[peca] = (linha_atual, coluna_atual)
        return posicoes
