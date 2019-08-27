class node :
    def __init__(self) :
        self.data = None
        self.right = None
        self.left = None

    def set_data(self, data) :
        self.data = data

    def get_data(self) :
        return self.data

    def get_left(self) :
        return self.left

    def get_right(self) :
        return self.right


def prefix_order(root, result) :
    if not root :
        return
    result.append (root.data)
    prefix_order (root.left, result)
    prefix_order (root.right, result)


def infix_order(root, result):
    if not root:
        return
    infix_order(root.left, result)
    result.append(root.data)
    infix_order(root.right, result)

def postfix_order(root,result):
    if not root:
        return
    postfix_order(root.left,result)
    postfix_order(root.right,result)
    result.append(root.data)



