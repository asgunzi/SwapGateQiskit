# SwatGateQiskit
Reflexões sobre o Swap Gate quântico
Algumas reflexões sobre a porta quântica Swap.

A porta Swap, como o próprio nome sugere, troca o estado de dois qubits.

Ela é representada pelo símbolo a seguir.

![](https://informacaoquantica.files.wordpress.com/2020/04/swap01.png)

Ou por:

![](https://informacaoquantica.files.wordpress.com/2020/04/swap-gate-using-cnot-gates.png)

Os seguintes tópicos serão discutidos:

    Como eu derivo a matriz de estados da mesma?
    Equivalência em cnots.
    Não é equivalente a trocar os “fios”?
    Implementação em qiskit


# 1. Como eu derivo a matriz de estados da mesma?

Eu sempre gosto de fazer esse tipo de exercício, para aprofundar os conceitos.

A porta troca o primeiro qubit pelo segundo, ou seja, este é o efeito:

|00> em |00>

|01> em |10>

|10> em |01>

|11> em |11>

Lembrando, |00> na forma vetorial é igual a [1 0 0 0]. |01> é dado por [0 1 0 0]. |10> é dado por [0 0 1 0]. |11> é dado por [0 0 0 1].

Portanto, representando matricialmente as operações acima:

Entrada:

[[ 1 0 0 0]

[0 1 0 0]

[0 0 1 0]

[0 0 0 1]]

Saída:

[[ 1 0 0 0]

[0 0 1 0]

[0 1 0 0]

[0 0 0 1]]

É uma matriz unitária, conforme esperado.

# 2. Equivalência em cnots.

A porta pode ser implementada por três cnots, conforme o diagrama acima já mostrava:

![](https://informacaoquantica.files.wordpress.com/2020/04/swap-gate-using-cnot-gates.png)


Um exercício é fazer a multiplicação das matrizes do cnot para chegar à matriz do item 1 acima. Não é difícil, e no próximo post posso detalhar.

# 3. Não é equivalente a trocar os “fios”?

Numa porta lógica clássica, implementada via circuitos eletrônicos, a porta swap seria sim equivalente a trocar os fios do circuito – o fio 1 vira fio 2, e o fio 2 o fio 1.

Porém, num computador quântico, pode ou não existir um “fio”.

Por exemplo, pode existir um computador quântico que utilize a camada onde está o elétron num átomo como qubit. Digamos que a manipulação dos estados quânticos seja jogando um laser no átomo. Neste caso, não vai existir um fio de verdade.

Ou, digamos, os qubits sejam fótons – que, por definição, ficam o tempo todo viajando à velocidade da luz. Manipulamos fótons via filtros polarizadores, espelhos e cristais, por exemplo. Neste caso, talvez eu consiga trocar a posição de um fóton com outro, via jogo de espelhos, digamos. Mas, a questão é que a lógica do circuito é outra. Não podemos mais pensar em termos eletrônicos.

![](https://informacaoquantica.files.wordpress.com/2020/04/20190919121736_1200_675_-_laser.jpg?w=1024)

# 4. Implementação em qiskit:

Vou criar o circuito swap e imprimir a matriz de estados do circuito em qiskit.

O circuito é representado a seguir. Lembrando que sempre temos que reservar o mesmo número de bits clássicos, por isso, são 2 qubits e 2 bits.
![](https://informacaoquantica.files.wordpress.com/2020/04/circuitoswap.jpg)


A matriz do circuito, resultante do modelo:

![](https://informacaoquantica.files.wordpress.com/2020/04/circuitoswapunitario.jpg)



Veja também:

Lembrei do texto [Reflexões sobra a teoria da reflexidade de George Soros](https://ideiasesquecidas.com/2016/06/14/reflexoes-sobre-a-teoria-da-reflexividade/). Nenhuma relação direta com o conteúdo aqui, mas é bastante interessante.

