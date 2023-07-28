from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {}  # Tabela de memoização para armazenar as combinações já calculadas
        
        def generate(n):
            # Verificar se já calculamos a combinação para n antes
            if n in memo:
                return memo[n]
            
            # Caso base: para n = 0, não há combinações válidas
            if n == 0:
                return [""]
            
            result = []
            for i in range(n):
                # Recursivamente gerar combinações para os parênteses internos
                inner_parentheses = generate(i)
                outer_parentheses = generate(n - 1 - i)
                
                # Combinar as combinações internas e externas para formar as combinações válidas
                for inner in inner_parentheses:
                    for outer in outer_parentheses:
                        result.append("(" + inner + ")" + outer)
            
            # Armazenar a combinação gerada para n na memoização antes de retorná-la
            memo[n] = result
            return result
        
        return generate(n)

def main():
    n = 3
    solution = Solution()
    combinations = solution.generateParenthesis(n)
    print(f"Combinações para n = {n}:")
    for comb in combinations:
        print(comb)

if __name__ == "__main__":
    main()