from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(array):
            if len(array) <= 1:
                return array

            # Divide a lista em duas partes
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            # Ordena recursivamente as duas metades
            left_half = merge_sort(left_half)
            right_half = merge_sort(right_half)

            # Mescla as duas metades ordenadas
            return merge(left_half, right_half)

        def merge(left, right):
            merged = []
            left_index, right_index = 0, 0

            # Compara os elementos das duas listas e insere na lista mesclada em ordem crescente
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

            # Adiciona os elementos restantes das duas listas
            merged.extend(left[left_index:])
            merged.extend(right[right_index:])

            return merged

        # Recursivo
        return merge_sort(nums)
    
def main():
    nums = [5, 2, 3, 1]

    solution = Solution()

    sorted_nums = solution.sortArray(nums)

    print("Lista ordenada:", sorted_nums)

if __name__ == "__main__":
    main()