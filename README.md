# Trabalho de TDD da disciplina INE5455 - Testes de Software

## Parte 1 - Desenvolva a seguinte parte do problema seguindo a abordagem TDD:

Uma empresa W possui vários funcionários e desenvolve vários
projetos. Cada funcionário pode trabalhar em vários projetos
simultaneamente e cada projeto pode ter vários funcionários.

## Parte 2 - Desenvolva a seguinte parte do problema seguindo a abordagem TDD: (continuação)

Um projeto tem uma coleção de ocorrências. E uma ocorrência
representa alguma coisa que precisa ser trabalhada. Uma
chave identifica unicamente uma ocorrência e um resumo
mostra sobre o que trata a ocorrência. Cada ocorrência tem
um funcionário responsável, que precisa trabalhar no mesmo
projeto da ocorrência.

Cada funcionário pode ser responsável por, no máximo, 10
ocorrências abertas considerando todos os projetos nos quais
ele participa.

Cada ocorrência pode estar em dois estados: aberta ou fechada.
Quando uma ocorrência é criada, ela é atribuída ao seu
responsável e permanece no estado aberta enquanto o seu
responsável não a termina. Quando o responsável termina a
ocorrência, ela é fechada. O responsável pela ocorrência pode
ser modificado enquanto a ocorrência está aberta.

Existem diferentes tipos de ocorrências: tarefa, bug, melhoria.
Cada ocorrência tem diferentes prioridades (alta, média,
baixa) e estas prioridades podem ser modificadas enquanto a
ocorrência está aberta.