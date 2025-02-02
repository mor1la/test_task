from graphviz import Digraph
from AVLNode import Node

def draw_tree(root: Node):
    def add_nodes_edges(dot, node):
        if node is None:
            return
        dot.node(str(id(node)), label=str(node.val))
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)))
            add_nodes_edges(dot, node.left)
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)))
            add_nodes_edges(dot, node.right)

    dot = Digraph()
    add_nodes_edges(dot, root)
    dot.render('avl_tree', format='png', view=True)

    