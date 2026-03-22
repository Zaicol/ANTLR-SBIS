from antlr4 import *
import pydot


def rule_to_str(rule, parser):
    if isinstance(rule, TerminalNode):
        return f"'{rule.getText()}'"
    else:
        # Используем имя правила вместо индекса
        try:
            return parser.ruleNames[rule.getRuleIndex()]
        except:
            return "unknown_rule"


# Рекурсивно строим узлы и связи
def add_nodes_edges(tree, parser, parent_node=None, tree_id=0, tree_graph=None):
    node_id = str(id(tree))
    label = rule_to_str(tree, parser)

    node = pydot.Node(node_id, label=label)
    tree_graph.add_node(node)

    if parent_node:
        edge = pydot.Edge(parent_node, node)
        tree_graph.add_edge(edge)

    if hasattr(tree, 'children'):
        for child in tree.children:
            add_nodes_edges(child, parser, node, tree_id + 1, tree_graph)


def generate_graph_tree(tree, parser):
    # Создаем пустой граф
    tree_graph = pydot.Dot(graph_type='digraph', rankdir="TB")

    # Начинаем добавлять узлы и ребра
    add_nodes_edges(tree, parser, tree_graph=tree_graph)

    # Сохраняем в файл и открываем
    tree_graph.write_png('ast_tree.png')
    print("Графическое дерево разбора сохранено как 'ast_tree.png'")
