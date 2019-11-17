class Solution:
    def helper(self, left, right):
        # XOR
        if bool(left is None) != bool(right is None):
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

    def isSymmetric(self, root) -> bool:
        if root is None: return True
        return self.helper(root.left, root.right)
