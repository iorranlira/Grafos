import networkx as nx

def warning_groups(g, t, m):

# Analisando especificidades
    if g is None or t is None or m is None or not validEntry(g, t, m):
        return None

# Encontra os componentes fracamente conectadas no grafo
    lista_componentes = list(nx.weakly_connected_components(g))
    grupos_suspeitos = []

    for grupos in lista_componentes:
        # Verifica se o tamanho do grupo é maior ou igual a m
        if len(grupos) >= m:
            transacoes_suspeitas = False

            # Verifica se o nó está envolvido em transações suspeitas
            for u in grupos:
                for v in g[u]:
                    if v in grupos and g[u][v]['amount'] >= t:
                        transacoes_suspeitas = True
                        break
                # Se encontra transações suspeitas, adiciona ao Array de retorno e encerra a execução   
                if transacoes_suspeitas:
                    grupos_suspeitos.append(list(grupos))
                    break

    return grupos_suspeitos
 

# Método que verifica se o Grafo passado de parâmetro tem atributos em seus arcos
def has_edge_attributes(g):
    for u, v, data in g.edges(data=True):
        if not data:
            return False
    return True

# Método que verifica os parâmetros de entrada
def validEntry(g, t, m):
    exit = True

    if not nx.is_directed(g):
        exit = False
    if not has_edge_attributes(g):
        exit = False
    if t < 0:
        exit = False 
    if m < 0:
        exit = False
    return exit