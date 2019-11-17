
def minDepth(root) -> int:
    if not root:
        return 0
    num = 0
    check_child(root, num)


def check_child( root, num):
    if not root.left and not root.right:
        return num + 1


