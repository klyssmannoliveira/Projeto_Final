from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def dividir(nums, left, right, k):
            # Contar as frequências dos elementos na sublista
            frequencias = {}
            for i in range(left, right + 1):
                if nums[i] in frequencias:
                    frequencias[nums[i]] += 1
                else:
                    frequencias[nums[i]] = 1
            
            # Ordenar os elementos pela frequência em ordem decrescente
            sorted_elements = sorted(frequencias, key=frequencias.get, reverse=True)
            
            # Retornar os k elementos mais frequentes
            return sorted_elements[:k]
        
        # Chamar a função dividir recursivamente para obter os k elementos mais frequentes
        return dividir(nums, 0, len(nums) - 1, k)

if __name__ == "__main__":

    solucao = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solucao.topKFrequent(nums, k))  # Saída: [1, 2]
