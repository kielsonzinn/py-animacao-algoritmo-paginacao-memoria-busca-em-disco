# TODO's

- Ajustar para no de paginação de memória, ter um label em baixo de cada card, que horas ele foi adicionado e que horas ele foi acessado

# O que foi usado

 - [Python](https://www.python.org/doc)
 - [Pygame](https://www.pygame.org/docs)

# Executando

```sh
pip install -r requirements.txt
python substituicao_de_pagina.py
python busca_em_disco.py
```

# Algoritmo de substituição de página

## FIFO (First-In, First-Out)

```
Passo	Página Acessada	Estado da Memória	Falta de Página?	Página Removida
1		1				[1]				Sim					-
2		2				[1, 2]				Sim					-
3		3				[1, 2, 3]			Sim					-
4		4				[2, 3, 4]			Sim					1 (mais antiga)
5		1				[3, 4, 1]			Sim					2 (mais antiga)
6		2				[4, 1, 2]			Sim					3 (mais antiga)
7		5				[1, 2, 5]			Sim					4 (mais antiga)
8		1				[1, 2, 5]			Não					-
9		2				[1, 2, 5]			Não					-
10		3				[2, 5, 3]			Sim					1 (mais antiga)
11		4				[5, 3, 4]			Sim					2 (mais antiga)
12		5				[3, 4, 5]			Sim					5 (mais antiga)
```

## LRU (Least Recently Used)

```
Passo	Página Acessada	Estado da Memória	Falta de Página?	Página Removida
1		1				[1]                             Sim					-
2		2				[1, 2]				Sim					-
3		3				[1, 2, 3]			Sim					-
4		4				[2, 3, 4]			Sim					1 (menos usada recentemente)
5		1				[3, 4, 1]			Sim					2 (menos usada recentemente)
6		2				[4, 1, 2]			Sim					3 (menos usada recentemente)
7		5				[1, 2, 5]			Sim					4 (menos usada recentemente)
8		1				[1, 2, 5]			Não					-
9		2				[1, 2, 5]			Não					-
10		3				[1, 2, 3]			Sim					1 (menos usada recentemente)
11		4				[4, 2, 3]			Sim					1 (menos usada recentemente)
12		5				[4, 5, 3]			Sim					5 (menos usada recentemente)
```

# Algoritmo de busca em disco

```
Algoritmo       Descrição                                                       Vantagens                                                           Desvantagens
FCFS	        Atende os pedidos na ordem de chegada.	                        Simples de implementar.                                             Pode ser ineficiente em sistemas com muitos acessos.
SSTF	        Atende o pedido mais próximo.	                                Reduz o tempo de movimento da cabeça.                               Pode causar starvation.
SCAN	        Move em uma direção até o fim e volta.	                        Garante que todos os pedidos sejam atendidos.                       Pode ser ineficiente para pedidos nas extremidades.
C-SCAN	        Move em uma direção até o fim e volta rapidamente ao início.	Melhora a eficiência para pedidos distantes.                        Não atende aos pedidos durante o retorno.
LOOK	        Move até o último pedido e inverte a direção.	                Mais eficiente que o SCAN.                                          Pode ser imprevisível se não atingir o final do disco.
C-LOOK	        Move até o último pedido e retorna rapidamente ao início.       Garante maior eficiência e elimina movimentos desnecessários.       Atrasos podem ocorrer para pedidos na direção oposta.
```
