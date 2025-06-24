import time

from problema import ProblemaNPuzzle
from heuristicas import pecas_fora_do_lugar, distancia_manhattan
from buscas_sem_infor.bfs import busca_em_largura
from buscas_sem_infor.dfs import busca_em_profundidade
from buscas_sem_infor.ids import busca_em_aprofundamento_iterativo
from buscas_com_info.gulosa import busca_gulosa
from buscas_com_info.a_estrela import busca_a_estrela
from utils.caminho import obter_caminho_com_estados, obter_sequencia_de_acoes


def imprimir_tabuleiro(estado):
    tamanho = len(estado)
    for i in range(tamanho):
        linha_str = " | ".join(f"{num:2}" for num in estado[i]).replace(' 0', '  ')
        print(f"[{linha_str}]")
    print()

def imprimir_resultado(algoritmo_nome, resultado_no, nos_expandidos, tempo_exec):    
    print(f"\n--- Resultado para {algoritmo_nome} ---")
    
    if resultado_no:
        caminho_estados = obter_caminho_com_estados(resultado_no)
        
        print(f" Solução encontrada com {len(caminho_estados) - 1} passos.")
        print(f" Nós expandidos: {nos_expandidos}")
        print(f" Tempo de execução: {tempo_exec:.4f} segundos.")
        ver_caminho = input("Deseja exibir o caminho completo estado por estado? (s/n): ").lower()
        if ver_caminho == 's':
            print("\n Exibindo caminho da solução:")
            for i, estado in enumerate(caminho_estados):
                print(f"\n--- Passo {i} ---")
                imprimir_tabuleiro(estado)
                time.sleep(0.5) 
    else:
        print(" Nenhuma solução foi encontrada.")
    
    print("-" * 35)


def principal():
    
    # 8-Puzzle
    estado_inicial_8 = ((1, 2, 3), (4, 0, 5), (6, 7, 8))
    estado_objetivo_8 = ((0, 1, 2), (3, 4, 5), (6, 7, 8))

    # 15-Puzzle
    estado_inicial_15 = ((1, 3,2, 4), (5, 6, 0, 8), (9, 10, 7, 12), (13, 14, 11, 15))
    estado_objetivo_15 = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0))

    # 24
    estado_inicial_24 = ((1, 2, 3, 4, 5), (6, 7, 8, 0, 9), (10, 11, 12, 13, 14), (16, 17, 18, 19, 15), (21, 22, 23, 24, 20))
    estado_objetivo_24 = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15), (16, 17, 18, 19, 20), (21, 22, 23, 24, 0))
    
    puzzles_disponiveis = {
        '1': ("Puzzle 8", estado_inicial_8, estado_objetivo_8),
        '2': ("Puzzle 15", estado_inicial_15, estado_objetivo_15),
        '3': ("Puzzle 24", estado_inicial_24, estado_objetivo_24)
    }

    
    problema = None
    while problema is None:
        print("\n===== RESOLUÇÃO DO N-PUZZLE =====")
        print("\nEscolha o tamanho do puzzle para resolver:\n")
        for chave, (nome, _, _) in puzzles_disponiveis.items():
            print(f"{chave} - {nome}")
        
        escolha_puzzle = input("\nDigite o número da opção: ")

        if escolha_puzzle in puzzles_disponiveis:
            nome_puzzle, estado_inicial, estado_objetivo = puzzles_disponiveis[escolha_puzzle]
            problema = ProblemaNPuzzle(estado_inicial, estado_objetivo)
            print(f"\nVocê escolheu o {nome_puzzle}.")
            print("Estado Inicial:")
            imprimir_tabuleiro(estado_inicial)
            print("Estado Objetivo:")
            imprimir_tabuleiro(estado_objetivo)
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(1)

    mapa_algoritmos = {
        '1': ("Busca em Largura", busca_em_largura, None),
        '2': ("Busca em Profundidade", busca_em_profundidade, None),
        '3': ("Aprofundamento Iterativo", busca_em_aprofundamento_iterativo, None),
        '4': ("Busca Gulosa (Peças Fora do Lugar)", busca_gulosa, pecas_fora_do_lugar),
        '5': ("Busca Gulosa (Manhattan)", busca_gulosa, distancia_manhattan),
        '6': ("Busca A* (Peças Fora do Lugar)", busca_a_estrela, pecas_fora_do_lugar),
        '7': ("Busca A* (Manhattan)", busca_a_estrela, distancia_manhattan)
    }

    while True:
        print("\nQual algoritmo de busca você deseja usar?\n")
        for chave, (nome, _, _) in mapa_algoritmos.items():
            print(f"{chave} - {nome}")
        print("0 - Sair do programa")
        
        escolha_algo = input("\nDigite o número da opção: ")

        if escolha_algo == '0':
            print("Encerrando o programa. Até mais!")
            break

        if escolha_algo in mapa_algoritmos:
            nome_algo, funcao_algo, heuristica = mapa_algoritmos[escolha_algo]
            
            inicio_tempo = time.time()
            
            if heuristica:
                resultado, nos_expandidos = funcao_algo(problema, heuristica)
            else:
                resultado, nos_expandidos = funcao_algo(problema)
                
            fim_tempo = time.time()
            
            imprimir_resultado(nome_algo, resultado, nos_expandidos, fim_tempo - inicio_tempo)
            
            input("\nPressione Enter para voltar ao menu de algoritmos...")
        else:
            print("\nOpção inválida! Por favor, escolha um número do menu.")
            time.sleep(1)

if __name__ == "__main__":
    principal()