from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)  # Ordenar a lista de pilhas em ordem decrescente

        total_moedas = 0  # número máximo de moedas

        n = len(piles) // 3  # Quantidade de trios (3 pilhas) que existem na lista

        for i in range(n):
            total_moedas += piles[2 * i + 1]  # Somar o valor da pilha do meio ao total de moedas

        return total_moedas

def main():
    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]

    solution = Solution()

    result = solution.maxCoins(piles)

    print("Número máximo de moedas:", result)

if __name__ == "__main__":
    main()