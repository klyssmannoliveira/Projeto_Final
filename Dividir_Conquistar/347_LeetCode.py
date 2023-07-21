from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # conta as frequências dos elementos
        def contar_frequencias(nums):
            frequencias = {}
            for num in nums:
                if num in frequencias:
                    frequencias[num] += 1
                else:
                    frequencias[num] = 1
            return frequencias
        
        # Combina as frequências contadas nas duas metades
        def combinar_frequencias(freq_esq, freq_dir):
            for num, freq in freq_dir.items():
                if num in freq_esq:
                    freq_esq[num] += freq
                else:
                    freq_esq[num] = freq
            return freq_esq
        
        # Caso base: se o array tem apenas um elemento, retornar esse elemento
        if len(nums) == 1:
            return nums
        
        # Divide o array em duas metades
        meio = len(nums) // 2
        nums_esq = nums[:meio]
        nums_dir = nums[meio:]
        
        # Recursivo para contar as frequências nas duas metades
        freq_esq = contar_frequencias(nums_esq)
        freq_dir = contar_frequencias(nums_dir)
        
        # Combina as frequências das duas metades
        freq_total = combinar_frequencias(freq_esq, freq_dir)
        
        # PSelecionar os elementos mais frequentes
        k_elementos = sorted(freq_total, key=freq_total.get, reverse=True)[:k]
        
        return k_elementos

if __name__ == "__main__":
    # Exemplo de uso:
    solucao = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solucao.topKFrequent(nums, k))  # Saída: [1, 2]
