import networkx as nx


def detect_smurfing (G, n_branch, n_layer, threshold):
    P = nx.reverse_view(nx.balanced_tree(n_branch,n_layer,nx.DiGraph))
    #array a ser retornado ao finao do metodo
    smurfing_cases = []
      
    #Criando instancias para verificar o isomorfismo entre os grafos P e um grafo recebido G.
    GM = nx.isomorphism.GraphMatcher(G.subgraph(node), P)
    
    for node in G.nodes:
        #Se P esta incorporado em G. 
        if GM.is_isomorphic(): 
        # m = next(GM.subgraph_isomorphisms_iter())
         nodes = list(P.nodes)
         soma_inicial = sum(G.nodes[node])
         soma_final = sum(G.nodes[node])

        #diferenca entre as somas
        diferenca = soma_inicial - soma_final

        #calculo da perda percentual
        perda_percentual = (diferenca/soma_inicial) * 100

        #Verificar se a perda esta abaixo do threshold
        if(perda_percentual <= threshold):
           destino = node
           smurfing_cases.append(soma_inicial,soma_final, destino, nodes)

    return smurfing_cases
