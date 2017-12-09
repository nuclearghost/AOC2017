
class Node:
    def __init__(self, line):
        inputs = line.split(" ")
        self.name = inputs[0]
        self.weight = inputs[1]
        self.parent = None
        self.children = []
        if len(inputs) > 2:
            for i in range(3, len(inputs)):
                self.children.append(inputs[i].rstrip(','))

if __name__ == "__main__":
    f = open("day7/day7in.txt","r")
    nodes = {}
    for line in f:
        node = Node(line.rstrip())
        nodes[node.name] = node
    for key, value in nodes.items():
        for child_name in value.children:
            child_node = nodes[child_name]
            child_node.parent = node

    root_node = None
    for key, value in nodes.items():
        if value.parent == None:
            print(f"updating root node to {value.name}")
            root_node = value

    print(root_node.name)
