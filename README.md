# 🧩 N-Puzzle 

Um sistema completo para resolução do **N-Puzzle** utilizando diferentes algoritmos de busca em Inteligência Artificial.

## 📋 Sobre o Projeto

O N-Puzzle é um quebra-cabeça clássico que consiste em um tabuleiro com peças numeradas e um espaço vazio. O objetivo é reorganizar as peças deslizando-as para alcançar uma configuração objetivo específica.

Este projeto implementa **5 algoritmos diferentes** para resolver o N-Puzzle:

### 🔍 Algoritmos de Busca sem Informação (Busca Cega)
- **BFS (Busca em Largura)**: Explora nível por nível, garantindo solução ótima
- **DFS (Busca em Profundidade)**: Vai fundo primeiro, eficiente em memória
- **IDS (Aprofundamento Iterativo)**: Combina vantagens do BFS e DFS

### 🎯 Algoritmos de Busca com Informação (Busca Heurística)
- **Busca Gulosa**: Usa apenas heurística para guiar a busca
- **A*** (A-Estrela): Combina custo real + heurística, garantindo solução ótima

## 🚀 Características

- ✅ Suporte para puzzles de diferentes tamanhos (8, 15, 24)
- ✅ Duas heurísticas implementadas (Peças Fora do Lugar e Distância Manhattan)
- ✅ Interface interativa de linha de comando
- ✅ Métricas detalhadas de performance
- ✅ Visualização do caminho da solução
- ✅ Comparação entre algoritmos

## 📊 Saídas do Sistema

Para cada execução, o programa fornece:

- 🔄 **Sequência de movimentos realizados**
- 📈 **Número total de passos**
- ⏱️ **Tempo de execução**
- 🌳 **Caminho de busca encontrado**
- 📊 **Nós expandidos** (métrica de eficiência)
- 🎯 **Profundidade máxima atingida**

## 🏗️ Estrutura do Projeto

```
Projeto_N-puzzle/
│
├── main.py                     # Interface principal e execução
├── problema.py                 # Modelagem do problema N-Puzzle
├── heuristicas.py             # Funções heurísticas
│
├── buscas_sem_infor/          # Algoritmos de busca cega
│   ├── bfs.py                 # Busca em Largura
│   ├── dfs.py                 # Busca em Profundidade
│   └── ids.py                 # Aprofundamento Iterativo
│
├── buscas_com_info/           # Algoritmos de busca heurística
│   ├── gulosa.py              # Busca Gulosa
│   └── a_estrela.py           # Algoritmo A*
│
├── utils/                     # Utilitários
│   └── caminho.py             # Funções para reconstrução do caminho
│
├── teste_ids_debug.py         # Testes comparativos
└── ROTEIRO_APRESENTACAO.txt   # Roteiro para apresentação
```

## 🔧 Instalação e Execução

### Pré-requisitos
- Python 3.7 ou superior
- Bibliotecas padrão do Python (não requer instalação adicional)

### Como executar

1. **Clone ou baixe o projeto**
2. **Navegue até o diretório do projeto**
3. **Execute o programa principal**:
   ```bash
   python main.py
   ```

### Exemplo de uso

```bash
$ python main.py

===== RESOLUÇÃO DO N-PUZZLE =====

Escolha o tamanho do puzzle para resolver:

1 - Puzzle 8
2 - Puzzle 15
3 - Puzzle 24

Digite o número da opção: 1

Estado Inicial:
[ 1 |  2 |  3]
[ 4 |    |  5]
[ 6 |  7 |  8]

Estado Objetivo:
[ 1 |  2 |  3]
[ 4 |  5 |  6]
[ 7 |  8 |   ]

Qual algoritmo de busca você deseja usar?

1 - Busca em Largura
2 - Busca em Profundidade
3 - Aprofundamento Iterativo
4 - Busca Gulosa (Peças Fora do Lugar)
5 - Busca Gulosa (Manhattan)
6 - Busca A* (Peças Fora do Lugar)
7 - Busca A* (Manhattan)
0 - Sair do programa

Digite o número da opção: 7

--- Resultado para Busca A* (Manhattan) ---
 Solução encontrada com 2 passos.
 Nós expandidos: 2
 Tempo de execução: 0.0001 segundos.
```

## 📚 Algoritmos Implementados

### 🔄 BFS (Busca em Largura)
- **Garantia**: Solução ótima
- **Estrutura**: Fila (FIFO)
- **Vantagem**: Menor número de passos
- **Desvantagem**: Alto consumo de memória

### ⬇️ DFS (Busca em Profundidade)
- **Garantia**: Encontra solução (não necessariamente ótima)
- **Estrutura**: Pilha (LIFO)
- **Vantagem**: Baixo consumo de memória
- **Desvantagem**: Pode encontrar soluções muito longas

### 🔄⬇️ IDS (Aprofundamento Iterativo)
- **Garantia**: Solução ótima
- **Estratégia**: Múltiplas buscas DFS com limite crescente
- **Vantagem**: Combina BFS + DFS
- **Conceito**: Cutoff para controlar profundidade

### 🎯 Busca Gulosa
- **Estratégia**: Usa apenas heurística h(n)
- **Vantagem**: Rápida
- **Desvantagem**: Não garante solução ótima

### ⭐ A* (A-Estrela)
- **Estratégia**: f(n) = g(n) + h(n)
- **Garantia**: Solução ótima (com heurística admissível)
- **Considerado**: Melhor algoritmo geral para este problema

## 🔍 Heurísticas

### 1. Peças Fora do Lugar
Conta quantas peças não estão em sua posição objetivo.

### 2. Distância Manhattan
Soma das distâncias Manhattan de cada peça até sua posição objetivo.
**Geralmente mais eficiente** que "Peças Fora do Lugar".

## 📈 Métricas de Performance

- **Nós Expandidos**: Quantidade de estados que geraram sucessores
- **Profundidade Máxima**: Maior profundidade explorada na árvore de busca
- **Tempo de Execução**: Tempo total para encontrar a solução
- **Número de Passos**: Quantidade de movimentos na solução

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte do estudo de **Algoritmos de Busca em Inteligência Artificial**, demonstrando na prática:

- Modelagem de problemas de busca
- Implementação de diferentes estratégias de busca
- Uso de heurísticas para otimização
- Análise comparativa de algoritmos
- Métricas de avaliação de performance

## 👥 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é desenvolvido para fins educacionais.

---

**Desenvolvido como projeto acadêmico para demonstração de algoritmos de busca em IA** 🤖