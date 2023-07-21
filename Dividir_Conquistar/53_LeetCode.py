from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def maior_soma(left, right):
            # Caso base: se o intervalo é composto por um único elemento, retornamos esse elemento
            if left == right:
                return nums[left]

            # Divide o intervalo ao meio
            mid = (left + right) // 2

            # Recursivamente encontrar a submatriz com a maior soma nos subintervalos à esquerda e à direita
            maior_soma_esquerda = maior_soma(left, mid)
            maior_soma_direita = maior_soma(mid + 1, right)

            # Encontra a submatriz com a maior soma que cruza o meio
            maior_soma_cruzada = maior_soma_submatriz(left, mid, right)

            # Retorna a maior soma entre as três submatrizes
            return max(maior_soma_esquerda, maior_soma_direita, maior_soma_cruzada)

        # Encontra a submatriz com a maior soma que cruza o meio
        def maior_soma_submatriz(left, mid, right):
            soma_esquerda = float('-inf')
            soma_direita = float('-inf')

            # Calcula a soma do lado esquerdo
            soma_atual = 0
            for i in range(mid, left - 1, -1):
                soma_atual += nums[i]
                soma_esquerda = max(soma_esquerda, soma_atual)

            # Calcula a soma do lado direito
            soma_atual = 0
            for i in range(mid + 1, right + 1):
                soma_atual += nums[i]
                soma_direita = max(soma_direita, soma_atual)

            # Retorna a soma máxima entre o lado esquerdo e direito
            return soma_esquerda + soma_direita

        return maior_soma(0, len(nums) - 1)

if __name__ == "__main__":

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solucao = Solution()
    resultado = solucao.maxSubArray(nums)
    print(resultado)