class Solution:
    def minPartitions(self, n: str) -> int:
        max_digito = 0 

        for digit in n:
            max_digito = max(max_digito, int(digit))

        return max_digito
    
def main():

    n = "82734"

    solution = Solution()

    resultado = solution.minPartitions(n)

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()