## 1561. Maximum Number of Coins You Can Get

Existem 3n pilhas de moedas de tamanhos variados, você e seus amigos irão pegar pilhas de moedas da seguinte forma:

Em cada etapa, você escolherá qualquer 3 pilhas de moedas (não necessariamente consecutivas).
Da sua escolha, Alice pegará a pilha com o maior número de moedas.
Você pegará a próxima pilha com o maior número de moedas.
Seu amigo Bob pegará a última pilha.
Repita até que não haja mais pilhas de moedas.
Dado um array de inteiros chamado **piles**, onde **piles[i]** representa o número de moedas na i-ésima pilha.

Retorne o número máximo de moedas que você pode obter.

### Exemplo 1:

Entrada: piles = [2,4,1,2,7,8]
Saída: 9
Explicação: Escolha o triplo (2, 7, 8), Alice escolhe a pilha com 8 moedas, você escolhe a pilha com 7 moedas e Bob fica com a última pilha.
Escolha o triplo (1, 2, 4), Alice escolhe a pilha com 4 moedas, você escolhe a pilha com 2 moedas e Bob fica com a última pilha.
O número máximo de moedas que você pode ter é: 7 + 2 = 9.
Por outro lado, se escolhermos esta disposição (1, 2, 8), (2, 4, 7) você só obtém 2 + 4 = 6 moedas, o que não é ótimo.

### Exemplo 2:

Entrada: piles = [2,4,5]
Saída: 4

### Exemplo 3:

Entrada: piles = [9,8,7,6,5,1,2,3,4]
Saída: 18

### Restrições:

3 <= piles.length <= 10^5
piles.length % 3 == 0
1 <= piles[i] <= 10^4


## Solução
[https://leetcode.com/problems/maximum-number-of-coins-you-can-get/](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/)

![solucao_Klyssmann](/assets/1561.PNG)