class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def emOrder_travessia(node):
            # Travessia em ordem (Sub-árvore esquerda, raiz, sub-árvore direita)
            if not node:
                return []
            return emOrder_travessia(node.left) + [node.val] + emOrder_travessia(node.right)

        def arvore_balanceada(values):
            
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = arvore_balanceada(values[:mid])
            root.right = arvore_balanceada(values[mid+1:])
            return root

        # Obtem lista ordenada da arvore
        sorted_values = emOrder_travessia(root)

        # Construção da nova árvore balanceada a partir da lista ordenada.
        balanced_root = arvore_balanceada(sorted_values)

        return balanced_root
    
def imprimir_arvore(node):
    if node is not None:
        left_val = "None" if node.left is None else str(node.left.val)
        right_val = "None" if node.right is None else str(node.right.val)
        print(f"[{node.val}, {left_val}, {right_val}]")
        imprimir_arvore(node.left)
        imprimir_arvore(node.right)

def main():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))

    solution = Solution()

    balanced_root = solution.balanceBST(root)

    # Imprimindo a árvore no formato [root, folha L, folha R]
    imprimir_arvore(balanced_root)

if __name__ == "__main__":
    main()