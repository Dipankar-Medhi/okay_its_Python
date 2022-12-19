
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right


def hasPath(root, sum):
    if root is None:
        return False

    # True if it is the leaf node
    if root.val == sum and root.left is None and root.right is None:
        return True

    # Subtract the value of the current node
    # from the given number to get a new sum
    #  => S = S - node.value

    if hasPath(root.left, sum - root.val):
        return True
    if hasPath(root.right, sum - root.val):
        return True

    return False


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(hasPath(root, 23))
