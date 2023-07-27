# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def allPossibleFBT(self, n: int) -> TreeNode:
        memo = {}  # Memoization para armazenar árvores binárias completas já calculadas
        
        def generateFBT(n):
            # Verificar se já calculamos essa árvore antes
            if n in memo:
                return memo[n]
            
            # Caso base: para n = 1, só existe uma árvore com um nó (raiz)
            if n == 1:
                return [TreeNode(0)]
            
            result = []
            for i in range(1, n, 2):
                # Recursivamente gerar árvores para as subárvores esquerda e direita
                left_subtrees = generateFBT(i)
                right_subtrees = generateFBT(n - 1 - i)
                
                # Combinar as subárvores esquerda e direita para formar as árvores completas
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        result.append(root)
            
            # Armazenar a árvore gerada para n na memoização antes de retorná-la
            memo[n] = result
            return result
        
        return generateFBT(n)
    
def print_tree(node):
    if node is None:
        return "null"
    return "[" + str(node.val) + "," + print_tree(node.left) + "," + print_tree(node.right) + "]"

def main():
    n = 7
    solution = Solution()
    result = solution.allPossibleFBT(n)
    
    formatted_result = [print_tree(tree) for tree in result]
    output_str = ", ".join(formatted_result)
    
    print(f"Output: [{output_str}]")

if __name__ == "__main__":
    main()
