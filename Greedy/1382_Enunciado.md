## 1382. Balance a Binary Search Tree

Dado o nó raiz de uma árvore binária de busca, retorne uma árvore binária de busca balanceada com os mesmos valores de nó. Se houver mais de uma resposta possível, retorne qualquer uma delas.

Uma árvore binária de busca é considerada balanceada se a diferença de profundidade entre as duas subárvores de cada nó não for maior do que 1.

### Exemplo 1:

![solucao_Klyssmann](/assets/balance1-tree.jpg)

Entrada: root = [1,null,2,null,3,null,4,null,null]
Saída: [2,1,3,null,null,null,4]
Explicação: Esta não é a única resposta correta, [3,1,4,null,2] também é correto.

### Exemplo 2:

![solucao_Klyssmann](/assets/balanced2-tree.jpg)

Entrada: root = [2,1,3]
Saída: [2,1,3]

### Restrições:

O número de nós na árvore está no intervalo [1, 10^4].
1 <= Node.val <= 10^5


## Solução
[https://leetcode.com/problems/balance-a-binary-search-tree/description/](https://leetcode.com/problems/balance-a-binary-search-tree/description/)

![solucao_Klyssmann](/assets/1382.PNG)