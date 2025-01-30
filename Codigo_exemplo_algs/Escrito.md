# Algoritmos

### Dentro de Algorithms.h está todos os algoritmos perguntados no exercício. 
Só houve um que eu consegui realizar que foi o de pesquisa Linear

Bubble Sort, ele vai verificar o adjacente, a ele, ver se o número atual é maior, caso seja ele irá trocar de posição com o n+1.
E ficará fazendo isso com todos os números da lista até que a lista esteja organizada.

Merge, ele vai separar a lista em pequenas sublistas de somente 2 números. Para cada uma dessas listas ele irá organizar quem é o maior, e ir agrupando novamente as listas, comparando uma com as outras e ordenando da maneira correta. Esse algoritmo usa o metódo Divide and Conquer (Dividir e Conquistar)

Insertion, o mais simples deles vai procurar pelo maior ou menor número. E fazer isso com os demais enquanto muda a posiçã
Ex: 2,6,1,3,15
1 - 1,2,6,3,15
2- 1,2,3,6,15

## Agora vamos falar de pesquisa
Linear Search, é o mais básico. Procure um elemento em uma array. É isso
basta um for e uma condicional e voilá. Normalmente é utilizado para dizer em qual index encontra-se X elemento e vice-versa

### Pesquisa Binária
A mais cabulosa de todas, porém precisa da lista organizada para ser realizada.
Vai usar o principio de dividir e conquistar também, sempre utilizando o meio da array para saber se o X se encontra maior que o meio ou menor que o mesmo.
Exemplo 
x = 25
1 - 100
x > 50 !
x agora só poderá ser menor que 50, no caso tbm teria um verificador para saber se ele é maior igual ou n ao meio. Basta ver o algorithms.h
enfim

agora teriamso de 
0-50
o meio é 25 que é o X e voila em 2 passos encontramos nosso número. sendo que na linear no piro dos casos teriamso que gastar O(n)
Enquanto que na binaria, gastamos O(logN)



# O que diabos é O(n) ??? 
Basicamente, a notação para definir o tempo máximo de execução do seu algoritmo
ou seja, no pior dos casos em quanto tempo x atividade será concluída.

As mais conhecidas: O(logN), O(n*logN),O(N), O(n²)
O(logN) o mais rápido, um exemplo é a lista binária.
O(N), será concluida em N vezes, digamos que vc tem q percorrer 100 contatos. Para achar um nome. No pior dos casos vc percorre os 100, isso é com a lista não organizada
O(n*logN), O Merge é um bom exemplo, ele só não é tão bom, pois embora ele quebre pela metade algumas vezes o número de operações que teriam de ser realizadas. Ainda sim é necessário repetir algumas ações que podem atrapalhar na execução.
O(n²) é tudo aqui que precisa de n*n coisas para realizado, Exemplo: percorrer todas as linhas de todas as colunas de uma tabela 
I * J, para cada i vezes voce vai ter que percorrer J vezes de uma certa quantidade
