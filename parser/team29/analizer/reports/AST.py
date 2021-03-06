from graphviz import Digraph
from analizer.reports.Nodo import Nodo

dot = Digraph(comment="AST")

# dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
#'test-output/round-table.gv.jpg'


class AST:
    def __init__(self):
        self.count = 0

    def makeAst(self, root):
        self.defineTreeNodes(root)
        self.joinTreeNodes(root)
        self.drawGraph()

    def defineTreeNodes(self, root):
        root.setId(str(self.count))
        dot.node(str(self.count), root.getVal())
        self.count += 1
        for node in root.getLista():
            self.defineTreeNodes(node)

    def joinTreeNodes(self, root):
        for node in root.getLista():
            dot.edge(root.getId(), node.getId())
            self.joinTreeNodes(node)

    def drawGraph(self):
        dot.render("test-output/round-table.gv", view=True)  # doctest: +SKIP
        "test-output/round-table.gv.jpg"
