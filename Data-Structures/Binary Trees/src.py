class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{self.value}]"

    def display_tree(self):  # Post Order traversal of the tree
        if self is None:
            print(None)
            return

        if self.left:
            self.left.display_tree()

        if self.right:
            self.right.display_tree()
        elif self.left:
            print(None, end=' ')

        print(self, end=' ')


if __name__ == "__main__":
    node1 = Node(8)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(1)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6

    r"""
    Structure should be:
            
            node1
             /\
            /  \
        node2  node3
         /\      \ 
        /  \      \
    node4  node5  node6
    """

    node1.display_tree()
