
class Tree(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

root = Tree(1)
a = root.left = Tree(2)
root.right = Tree(3)
a.right = Tree(5)

# print(root.left.right.val)

# class Solution(object):
#     def binaryTreePaths(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         if root is None:
#             return root
#         path_string = ''
#         list_of_paths = []
#         self.dfs(root,path_string,list_of_paths)
#         return list_of_paths
#
#     def dfs(self,root,path_string,list_of_paths):
#         if root.left is None and root.right is None:
#             list_of_paths.append(path_string + str(root.val))
#             return
#         path_string += str(root.val) + '->'
#         if root.left is not None:
#             self.dfs(root.left,path_string,list_of_paths)
#         if root.right is not None:
#             self.dfs(root.right, path_string, list_of_paths)


class Solution(object):
    # def binaryTreePaths(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[str]
    #     """
    #     if not root:
    #         return root
    #     path = ''
    #     list_path = []
    #     self.dfs(root, path, list_path)
    #     return list_path
    #
    # def dfs(self, root, path, list_path):
    #     if not root.left and not root.right:
    #         list_path.append(path + str(root.val))
    #         return
    #     path += str(root.val) + "->"
    #     if root.left is not None:
    #         self.dfs(root.left, path, list_path)
    #     if root.right is not None:
    #         self.dfs(root.right, path, list_path)
    def BinaryTreePaths(self, root):
        if not root:
            return root
        path = ''
        result = []
        self.dfs(root, path, result)
        return result

    def dfs(self, root, path, result):
        if root.left is None and root.right is None:
            result.append(path + str(root.val))
            return
        path += str(root.val) + "->"
        if root.left is None:
            self.dfs(root.right, path, result)
        if root.right is None:
            self.dfs(root.left, path, result)

b = Solution()
result = b.BinaryTreePaths(root)
print(result)
