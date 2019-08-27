import queue


class Binary_tree :

    def __init__(self) :
        self.data = None
        self.right = None
        self.left = None

    def set_data(self, data) :
        self.data = data

    def get_data(self) :
        return self.data

    def get_right(self) :
        return self.right

    def get_left(self) :
        return self.left

    def set_right(self, new_node) :
        if self.left == None :
            self.left = Binary_tree (new_node)
        else :
            temp = Binary_tree (new_node)
            temp.right = self.right
            self.right = temp

    def set_left(self, new_node) :
        if self.right == None :
            self.right = Binary_tree (new_node)
        else :
            temp = Binary_tree (new_node)
            temp.left = self.left
            self.left = temp


def inserting_tree(root, data) :
    new_node = Binary_tree (data)
    if root is None :
        root = new_node
        return root
    q = queue ( )
    q.en_queue (root)
    node = None
    while not q.is_empty ( ) :
        node = q.de_queue ( )
        if data == node.get_data ( ) :
            return root
        if node.left is not None :
            q.en_queue (node.left)
        else :
            node.left = new_node
            return root
        if node.right is not None :
            q.en_queue (node.right)
        else :
            node.right = new_node
            return root
