class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Criando uma tabela de memoização para armazenar os resultados intermediários
        memo = [[0] * 5 for _ in range(n+1)]
        
        # Inicializando a tabela para o caso base n = 1
        for i in range(5):
            memo[1][i] = 1
        
        # Calculando os resultados para n >= 2 usando a memoização
        for i in range(2, n+1):
            for j in range(5):
                for k in range(j, 5):
                    memo[i][j] += memo[i-1][k]
        
        # Soma dos resultados finais para todas as vogais
        result = sum(memo[n])
        return result
    
    
def main():
    n = 2
    solution = Solution()
    result = solution.countVowelStrings(n)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()