import graphviz #pip install graphviz

# -------------------- Ejemplo 1: Grafo No Dirigido --------------------
grafo = graphviz.Graph(format='png')  #Se puede cambiar el formato a 'pdf', 'svg'
grafo.node('A', 'Nodo A')
grafo.node('B', 'Nodo B')
grafo.node('C', 'Nodo C')

# Agregar aristas (conexiones) entre los nodos
grafo.edge('A', 'B')
grafo.edge('B', 'C')
grafo.edge('A', 'C')

grafo.render('grafo_no_dirigido', view=True)

# -------------------- Ejemplo 2: Grafo Dirigido --------------------
grafo_dirigido = graphviz.Digraph(format='png')
grafo_dirigido.node('A', 'Inicio')
grafo_dirigido.node('B', 'Proceso')
grafo_dirigido.node('C', 'Fin')

grafo_dirigido.edge('A', 'B')
grafo_dirigido.edge('B', 'C')
grafo_dirigido.edge('A', 'C')

grafo_dirigido.render('grafo_dirigido', view=True)

# -------------------- Ejemplo 3: Grafo Personalizado --------------------
grafo_personalizado = graphviz.Digraph(format='png')
grafo_personalizado.node('A', 'Nodo A', shape='box', color='red')
grafo_personalizado.node('B', 'Nodo B', shape='ellipse', color='blue')
grafo_personalizado.node('C', 'Nodo C', shape='diamond', color='green', style='filled', fillcolor='lightgreen')

grafo_personalizado.edge('A', 'B', label='Arista 1', color='purple')
grafo_personalizado.edge('B', 'C', label='Arista 2', style='dashed')
grafo_personalizado.edge('A', 'C', label='Arista 3', style='dotted')

grafo_personalizado.render('grafo_personalizado', view=True)
