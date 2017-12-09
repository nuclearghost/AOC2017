class Node:
    def __init__(self, line):
        inputs = line.split(" ")
        self.name = inputs[0]
        self.weight = int(inputs[1].lstrip("(").rstrip(")"))
        self.parent = None
        self.children = []
        self.child_nodes = []
        self.children_weight = 0
        if len(inputs) > 2:
            for i in range(3, len(inputs)):
                self.children.append(inputs[i].rstrip(','))

    def total_weight(self):
        return self.weight + self.children_weight

def find_root(nodes):
    for key, value in nodes.items():
        if value.parent == None:
            print(f"updating root node to {value.name}")
            return value

def dfs(node, visited):
    if node not in visited:
        visited.append(node)
        for child in node.child_nodes:
            dfs(child, visited)
    return visited

def set_child_weights(nodes):
    for node in nodes:
        for child_node in node.child_nodes:
            node.children_weight = node.children_weight + child_node.total_weight()

def find_unbalanced_node(nodes):
    for node in nodes:
        indent = 0
        children_weight = None
        print(f"{' ' * indent}{node.name} | {len(node.children)} children | Children Weight: {node.children_weight} | Total Weight: {node.total_weight()}")
        for child_node in node.child_nodes:
            indent = 2
            if children_weight == None:
                children_weight = child_node.total_weight()
                print(f"{' ' * indent}Child weight from node {child_node.name}: {children_weight}")
            elif child_node.total_weight() != children_weight:
                print(f"{' ' * indent}Found a fishy element {child_node.name} Node Weight: {child_node.weight} Node Children's Weight: {child_node.children_weight} Total Weight: {child_node.total_weight() } | balance: {children_weight}")
            else:
                print(f"{' ' * indent}{child_node.name} Node Weight: {child_node.weight} Node Children's Weight: {child_node.children_weight} Total Weight: {child_node.total_weight() } | balance: {children_weight}")

if __name__ == "__main__":
    f = open("day7/day7in.txt","r")
    # f = open("day7/test.txt","r")
    nodes = {}
    for line in f:
        node = Node(line.rstrip())
        nodes[node.name] = node
    for key, node in nodes.items():
        for child_name in node.children:
            child_node = nodes[child_name]
            child_node.parent = node
            node.child_nodes.append(child_node)

    root_node = find_root(nodes)
    dfs_nodes = dfs(root_node, [])
    set_child_weights(reversed(dfs_nodes))
    find_unbalanced_node(reversed(dfs_nodes))
