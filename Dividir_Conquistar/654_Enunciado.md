## 654. Maximum Binary Tree

Você recebe um array de números inteiros `nums` sem duplicatas. Uma árvore binária máxima pode ser construída recursivamente a partir de `nums` usando o seguinte algoritmo:

1. Crie um nó raiz cujo valor seja o valor máximo em `nums`.
2. Construa recursivamente a subárvore esquerda no subarray prefixo à esquerda do valor máximo.
3. Construa recursivamente a subárvore direita no subarray sufixo à direita do valor máximo.
4. Retorne a árvore binária máxima construída a partir de `nums`.

### Exemplo 1:

![solucao_Klyssmann](/assets/tree1.jpg)

Entrada: nums = [3,2,1,6,0,5]
Saída: [6,3,5,null,2,0,null,null,1]
Explicação: As chamadas recursivas são as seguintes:
- O maior valor em [3,2,1,6,0,5] é 6. O prefixo esquerdo é [3,2,1] e o sufixo direito é [0,5].
    - O maior valor em [3,2,1] é 3. O prefixo esquerdo é [] e o sufixo direito é [2,1].
        - Array vazio, então não há filho.
        - O maior valor em [2,1] é 2. O prefixo esquerdo é [] e o sufixo direito é [1].
            - Array vazio, então não há filho.
            - Apenas um elemento, então o filho é um nó com valor 1.
    - O maior valor em [0,5] é 5. O prefixo esquerdo é [0] e o sufixo direito é [].
        - Apenas um elemento, então o filho é um nó com valor 0.
        - Array vazio, então não há filho.

### Exemplo 2:

![solucao_Klyssmann](/assets/tree2.jpg)

Entrada: nums = [3,2,1]
Saída: [3,null,2,null,1]

### Restrições:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
Todos os inteiros em nums são únicos.

## Solução
[https://leetcode.com/problems/maximum-binary-tree/](https://leetcode.com/problems/maximum-binary-tree/)

![solucao_Klyssmann](/assets/654.PNG)