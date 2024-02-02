import networkx as nx
from matplotlib import colors
from gtufcg.util.networkx_util import draw_graph, read_multiple_CSV
from src.Q01 import warning_groups

# Exemplo de uso da função
lines = [ # Descrição do Grafo exemplo
    "0 3 {'amount' : 1000}",
    "0 2 {'amount' : 300}",
    "0 1 {'amount' : 2000}",
    "3 6 {'amount' : 500}",
    "3 4 {'amount' : 800}",
    "4 5 {'amount' : 100}",
    "1 6 {'amount' : 995}",
    "1 5 {'amount' : 996}",
    "5 0 {'amount' : 400}",
    "5 3 {'amount' : 1000}",
    "10 9 {'amount' : 150}",
    "7 8 {'amount' : 5000}",
    "8 9 {'amount' : 200}"
]
G1 = nx.parse_edgelist(lines, create_using=nx.DiGraph)
w_groups = warning_groups(G1, 5000, 3)
print(f"Grupos suspeitos: {w_groups}") # Saída esperada (em qualquer ordem): [['7', '9', '8', '10']]
draw_graph(G1, layoutid='kamada_kawai_layout', title="G1",
           nset=w_groups,
           nsetcolor=list(colors.TABLEAU_COLORS.keys())[0:len(w_groups)] + ["white"],
           nsetlabel=[f"Suspeito {i}" for i in range(1, len(w_groups) + 1)] + ["Demais pessoas"],
           edge_labels=nx.get_edge_attributes(G1, 'amount'))
