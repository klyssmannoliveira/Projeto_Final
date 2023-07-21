from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_linha = [0] * n  # Alturas máximas de cada linha
        max_coluna = [0] * n  # Alturas máximas de cada coluna

        for r in range(n):
            for c in range(n):
                max_linha[r] = max(max_linha[r], grid[r][c])
                max_coluna[c] = max(max_coluna[c], grid[r][c])

        max_aumento = 0  # soma máxima das alturas que podem ser aumentadas

        for r in range(n):
            for c in range(n):
                # A altura máxima permitida para esse prédio pode ser calculado o menor valor entre as alturas máximas da linha e coluna
                altura_max_permitida = min(max_linha[r], max_coluna[c])
                # Somar a altura máxima permitida para o prédio atual à soma total das alturas que podem ser aumentadas
                max_aumento += max(0, altura_max_permitida - grid[r][c])

        return max_aumento
    
def main():
    grid = [
        [3, 0, 8, 4],
        [2, 4, 5, 7],
        [9, 2, 6, 3],
        [0, 3, 1, 0]
    ]
    solution = Solution()

    result = solution.maxIncreaseKeepingSkyline(grid)

    print("Máxima soma das alturas que podem ser aumentadas:", result)

if __name__ == "__main__":
    main()