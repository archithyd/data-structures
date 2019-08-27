import queue
import stack

max_num = 0


def max_data(root):
    global max_num
    if not root:
        return
    if root.data > max_num:
        max_num = root.data

    max_data(root.left)
    max_data(root.right)
    return max_num


def find_val(root, value):
    flag = 0
    if not root:
        return 0
    if root.data == value:
        return 1

    else :
        temp = find_val(root.left, value)
        if temp == 1:
            return temp
        elif flag == 0:
            return find_val(root.right, value)


def find_len(root):
    if root is None:
        return
    return find_len(root.right) + find_len(root.right) + 1


def find_len2(root):
    if root is None:
        return
    q = queue()
    q.en_queue(root)
    node = None
    count = 0
    while not q.is_empty:
        node = q.de_queue()
        count += 1
        if node.left is not None:
            q.en_queue(node.left)
        if node.right is not None:
            q.en_queue(node.right)
    return count


def level_reverse_order(root):
    if root is None:
        q = queue()
        s = stack()
        q.en_queue(root)
        node = None
        while not q.is_empty:
            node = q.de_queue
            if node.left is not None:
                q.en_queue(node.left)
            if node.right is not None:
                q.en_queue(node.right)
            s.push(node)
        while not s.is_empty:
            print(s.pop().get_data)


def delete_root(root):
    if root is None:
        return
    delete_root(root.left)
    delete_root(root.right)
    del root


def find_depth(root):
    if root is None:
        return
    return max(find_depth(root.left), find_depth(root.right)) + 1


def deepest_node(root):
    if root is None:
        return
    q = queue
    q.en_queue(root)
    node = None
    while not q.is_empty:
        node = q.de_queue
        if node.left is not None:
            q.en_queue(node.left)
        if node.right is not None:
            q.en_queue(node.right)
    return node.get_data()


def find_number_of_leaves(root):
    if root is None:
        return
    q = queue()
    q.en_queue(root)
    node = None
    count = 0
    while not q.is_empty:
        node = q.de_queue()
        if node.left is None and node.right is None:
            count += 1
            if node.left is not None:
                q.en_queue(node.left)
            if node.right is not None:
                q.en_queue(node.right)
    return count


def find_full_node(root):
    if root is None:
        return
    q = queue()
    q.en_queue(root)
    node = None
    count = 0
    while q.is_empty:
        node = q.de_queue()
        if node.left is None and node.right is None:
            count += 1
        if node.left is not None:
            q.en_queue(node.left)
        if node.right is not None:
            q.en_queue(node.right)
    return count


def find_node_with_one_child(root):
    if root is None:
        return
    q = queue()
    q.en_queue(root)
    node = None
    count = 0
    while q.is_empty:
        node.q.de_queue()
        if node.left is not None and node.right is None or node.left is None and node.right is not None:
            count += 1
        if node.left is not None:
            q.en_queue(node.left)
        if node.right is not None:
            q.en_queue(node.right)
    return count


def compare_tree(root1, root2):
    if root1 is None and root2 is None:
        return "True"
    if (not root1.left and not root2.right) and (not root2.left and not root2.right) and (root1.data == root2.data):
        return "True"
    if (root1.left and not root1.right) and (not root1.left and root1.right) and (root2.left and not root2.right) \
            and (not root2.left and root2.right) and root1.data != root2.data:
        return "False"
    left = compare_tree(root1.left, root2.left)
    right = compare_tree(root1.right, root2.right)
    if left is "True" and right is "True":
        return "True"
    else:
        return "False"


def path_finder(value,root,path,paths):
    if not root:
        return False

    if not root.left and not root.right:
        if root.data==value:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False

    left=path_finder(value-root.data,root.left,path+[root.data],paths)
    right=path_finder(value-root.data,root.right,path+[root.data],paths)
    return left or right

def sum_of_binary_tree(root):
    if root is None:
        return
    return root.data+sum_of_binary_tree(root.left)+sum_of_binary_tree(root.right)


def sum_without_recurssion(root):
    if root is None:
        return
    q=queue()
    q.en_queue(root)
    node=None
    sum=0
    while not q.is_empty():
        node=q.de_queue()
        sum+=node.get_data()
        if not node.left:
            q.en_queue(node.left)
        if not node.right:
            q.en_queue(node.right)
    return sum


def mirror_of_the_tree(root):
    if root is not None:
        mirror_of_the_tree(root.left)
        mirror_of_the_tree(root.right)
        temp=root.right
        root.right=root.left
        root.left=temp
    return root



def are_mirror(root1,root2):
    if root1 is None and root2 is None:
        return 1
    if root1 is None or root2 is None:
        return 0
    if root1.data!=root2.data:
        return 0
    return are_mirror(root1.left,root2.right) and are_mirror(root1.right,root2.left)


def lca(root,a1,a2):
    if root is None:
        return None
    if root.data==a1 and root.data==a2:
        return root
    left=lca(root.left,a1,a2)
    right=lca(root.right,a1,a2)


def print_ancestor(root,node):
    if root is None:
        return
    if root.left==node or root.right or  print_ancestor(root.left) or print_ancestor(root.right):
        print(root.data)
    return 0






