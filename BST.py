class BST :
    def __init__(self, data) :
        self.data = data
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


def find_element(root, data) :
    current = root
    while current is not None :
        if data == current :
            return current
        if data < current :
            current = current.get_left ( )
        if data > current :
            current = current.get_right ( )
    return current


def min_element(root) :
    current = root
    if root is None :
        return None
    else :
        return current (current.get_left ( ))


def min_element_without_recursion(root) :
    current = root
    if current is None :
        return None
    else :
        while current is not None :
            current = current.get_left ( )
        return current


def max_element(root) :
    current = root
    if current is None :
        return None
    else :
        return max_element (current.get_right ( ))


def max_element_without_recursion(root) :
    current = root
    if current is None :
        return
    else :
        while current is not None :
            current = current.get_right ( )
        return current


def in_order_predecessor(root) :
    temp = None
    if root.get_left ( ) :
        temp = root.get_left ( )
        while temp is not None :
            temp = temp.get_right
    return temp


def in_order_successor(root) :
    temp = None
    if root.get_right ( ) :
        temp = root.get_right ( )
        while temp is not None :
            temp = temp.get_left ( )
    return temp


def insertion_bst(root, node) :
    if root is None :
        root = node
    else :
        if node.data < root.data :
            if root.left is None :
                root.left = node
            else :
                return insertion_bst (root.left, node)

        else :
            if root.right is None :
                root.right = node
            else :
                return insertion_bst (root.right, node)


"""def delete_node(root, data):
    if root is None:
        return None
    else:
        current = root
        while current is not None:
            if data > current.data:
                if current.get_right() is None:
                    return None
                else:
                    return delete_node(root.right, data)
            else:
                if current.get_left() is None:
                    return None
                else:
                    return delete_node(root.left, data)
    if current.get_left() is not None and current.get_right() is not None:
        current.set_data(current.get_right().data)
        current.right = None

    elif current.get_left() is None and current.get_right() is not None:
        current.set_data (current.get_right ( ).data)
        current.right = None


    elif current.get_left() is not None and current.get_right() is None:
        
"""


def lca(root, a, b) :
    while root :
        if (a <= root.data) and (b >= root.data) or (a <= root.data) and (b >= root.data) :
            return root
        elif a < root.data :
            root = root.left
        else :
            root = root.right


def check_bst(root):
    if root is None:
        return
    else:
        current = root
        if current.left.data < current.right.data:
            return True
        else:
            return False
    x = check_bst(root.left)
    y = check_bst(root.right)
    if x is True and y is True:
        print("bst")
    else:
        print("not bst")


def kth_smallest_number(root, k):
    count = 0
    if not root:
        return None
    left = kth_smallest_number(root.left, k)
    if left:
        return left
    count += 1
    if count == k:
        return root
    return kth_smallest_number(root.right, k)


def count_tree(root, n):
    if n <= 1:
        return
    else:
        sum_1 = 0
        for i in range(1, n+1):
            left = count_tree(root-1)
            right = count_tree(n-root)
            sum_1 = left*right
        return sum_1




