# Definição da classe TreeNode para representar um nó da árvore binária.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None

            # Encontra o índice do maior valor no subarray
            max_idx = left
            for i in range(left, right+1):
                if nums[i] > nums[max_idx]:
                    max_idx = i

            # Cria o nó raiz com o valor máximo encontrado
            root = TreeNode(nums[max_idx])

            # Constrói recursivamente a subárvore esquerda
            root.left = build_tree(left, max_idx - 1)

            # Constrói recursivamente a subárvore direita
            root.right = build_tree(max_idx + 1, right)

            return root

        # Recursivo
        return build_tree(0, len(nums) - 1)
    
def print_tree(node):
    if node is not None:
        left_val = "None" if node.left is None else str(node.left.val)
        right_val = "None" if node.right is None else str(node.right.val)
        print(f"[{node.val}, {left_val}, {right_val}]")
        print_tree(node.left)
        print_tree(node.right)

if __name__ == "__main__":
    nums = [3, 2, 1, 6, 0, 5]
    solution = Solution()
    root = solution.constructMaximumBinaryTree(nums)
    print(print_tree(root))