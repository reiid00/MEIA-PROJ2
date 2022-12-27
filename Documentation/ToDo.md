# Projeto 2:
**Objetivo** - Otimização do Stock Físico de uma Loja (maximizando os lucros da mesma).

**Tipo de Aplicação** - Sistema de Recomendação.

## A Fazer

### Blog
1. Completar as páginas "Challenge 1" e " Challenge 2", respeitando uma estrutura igual que também será utilizada para os próximos projetos. Esta estrutura deverá possuir três secções, nomeadamente a definição do objetivo, a solução concretizada, enumerando os pontos cruciais que foram atingidos e alguns que poderão ser melhorados e uma secção final com a restrospecao da equipa (duas partes, Geral e Individual, sendo que no primeiro projeto só existem 3 restrospecoes individuais) face aos obstáculos sentidos e ultrapassados, à satisfação da solução obtida e um comentário pessoal face ao projeto global tanto no ponto de vista de equipa como no ponto de vista individual.

  Resumo da Estrutura:
    - Objetivo
    - Solução
    - Restrospecao
    - - Geral
    - - Elemento 1
    - - Elemento 2
    - - ...

  As páginas dos challenges 3 e 4 também deverão ser editadas como preparação para o futuro, delineando a estrutura da mesma forma que foi delineada nos outros dois, mas apenas escrevendo algo do gênero "TBD" na parte do conteúdo.

2. Alterar a página inicial para facilitar o acesso às páginas de cada challenge, sendo que deverá ser apresentando um resumo breve com um botão que redireciona para a página, acompanhado de um icon ou imagem representativo da ideia explorada nesse desafio. A página inicial também deverá ser atualizada para facilitar o acesso à página do blog (com os updates semanais).

3. Atualizar a página do About Us para colocar apenas o acesso ao linkedin e ao email de cada elemento (sugiro email do isep para todos menos o Vinicius)

4. Atualizar o blog inteiro, retirando tudo que não é utilizado, isto é, que faz parte da template e que ainda não foi preenchido com valores a sério, procurando sempre substituir isso por algo adequado para a nossa equipa/mestrado, a não ser que não se enquadre mesmo nisso e não afete visualmente o website, sendo que nesse caso pode ser simplesmente removido, embora isto deva ser confirmado sempre juntamente com os restantes elementos da equipa.

5.  Completar a semana 7, 8, 12 (mencionar a master session que ocorreu) e 13 do blog. (a 7 e 8 não estavam não sei porquê, preciso de confirmar com o Vasco e Isadora se chegaram a escrever algo e entretanto foi apagado, dado que tinha ideia que estava escrito). A semana 10 está quase finalizada, restando apenas a parte de brainstorming, dado que houve mts alterações e ent n sabia se metia na mesma o que foi pensado inicialmente, mas acho que é melhor e irei terminar isso este fim de semana.

6. Alterar a estrutura da página do blog que tem os updates semanais, sendo que deverá ser possível visualizar somente as semanas de cada challenge, através de filtros facilmente acessíveis ou algo semelhante. Esta estrutura deverá também apresentar cada semana com uma imagem de apoio e uma (ou mais) keyword representativa da semana (p. ex. Semana 9 - Exames Finais, Semana 1- Brainstorming, Semana 8 - Pitch). A imagem de cada semana deverá ser diferente e certamente o wixsite terá algumas para utilizarmos, sendo que resta escolhermos com base naquilo que foi descrito em cada semana, isto é, uma imagem que seja adequada ao que foi realizado na respetiva semana.

7. (___opcional___) Se possível, irmos fazer uma atividade ou um jantar ou algo do gênero, quando estivermos mais tranquilos de tempo e com tudo organizado, para tirarmos uma foto de grupo e ficarmos-nos a conhecer melhor até porque temos dois novos elementos e iremos ter mais 2 projetos pela frente. Preferencialmente após o pitch, mas a tempo de atualizarmos o site com a imagem antes de os professores analisarem o blog.


### Aprendizagem Automática
**Objetivo** - Para um dataset com o histórico de vendas diárias de diversos produtos, será necessário desenvolver uma função que divide os dados de vendas em diferentes dataframes, um para cada produto, criando e treinando um modelo para um desses dataframes e armazenando o modelo resultado (função Y=mx +b) num ficheiro csv ou assim, para dps este ficheiro ser consumido pelo método de otimização, permitindo que o mesmo usufrua da previsão obtida. Deverão existir dois modelos por produto, um para prever as unidades vendidas no dia seguinte e outro para prever o lucro de vendas do dia seguinte. Se existirem muitos dados, podemos tentar fazer à semana, mas penso que será melhor diariamente, até porque a minha análise de planeamento, descrita mais à frente, tem em consideração um modelo diário de previsão, mas à partida também não será difícil adaptar o mesmo para utilizar uma lógica semanal.


### Planeamento e Tomada de Decisão
**Método** - ILP (Integer Linear Programming)

Abaixo, deixo as configurações que penso que farão mais sentido aplicar neste projeto, sendo que podemos pensar nisto como um software em que o utilizador escolhe os valores pretendidos, alguns destes opcionais, anexando o dataset com o histórico de vendas dos produtos que pretende que sejam (ou possam ser) incluídos na otimização. Já agora, alguém deverá fazer um mockup (p. ex. em balsamiq) de como poderia ficar uma interface desse tipo, para apresentarmos no blog, no pitch, na demo e talvez até no artigo, como sendo o protótipo do nosso produto, sendo a interface/software uma das coisas a explorar no trabalho futuro.

**Configurações Obrigatórias (Hard Constraints)**:
- __A e B(int)__ - Min e Max de variedade de produtos. Se Min for 0, ent n existe mínimo. Se Max for 0, ent o Max é igual ao número de produtos diferentes no dataset. Se ambos forem 0, ent é obrigatório usar todos os produtos, isto é, a quantidade cada produto tem que ser maior que 0.

- __C e D(int)__ - Min e Max quantidades por produto. Se Min e Max forem 0, ent não são usados.

- __E e F(int)__ - Min e Max quantidades globais (soma total das quantidades escolhidas para os produtos). Se Min e Max forem 0, ent n são usados. (podemos testar sempre com isto a 0, dado que como utilizaremos as dimensões, à partida deixa de fzr sentido usar esta restrição, mas por agora podemos deixar e no futuro removemos se acharmos que n acrescenta nada)

- __G(int)__ - Dimensões uteis, em metros cúbicos, da loja. Este valor é obrigatório, ou seja, tem que ser superior a 0. A soma das dimensões de cada produto escolhido multiplicado pela respetivas quantidades, tem que ser inferior ou igual a este valor.

- __H(int)__ - Periodicidade de refill de stock médio por produto, em dias. Ou seja, representa os dias mínimos cujas quantidades escolhidas para cada produto deverão aguentar em stock até ao próximo refill no fornecedor.


**Características necessárias para cada produto**:
- __Dimensões__ - comprimento, largura e altura.

- __Lucro previsto__ - Isto será representado pela função obtida no modelo treinado em aprendizagem automática para prever o lucro de vendas do dia seguinte com base no seu histórico diário de vendas. Se o parâmetro H estiver definido com o valor 1, ent basta prever para o próximo dia, se for 10, ent é preciso aplicar o modelo de previsão de lucro de vendas para os próximos 10 dias e somar os valores obtidos, sendo que uma solução ótima é aquela que maximiza as receitas da empresa, respeitando todas as outras restrições.

- __Unidades vendidas previstas para um dado dia__ - Isto será representado pela função obtida no modelo treinado em aprendizagem automática para prever as unidades vendidas do dia seguinte com base no seu histórico diário de vendas. Se o parâmetro H estiver definido com o valor 1, ent basta prever para o próximo dia, se for 10, ent é preciso aplicar o modelo de previsão de unidades vendidas para os próximos 10 dias e somar os valores obtidos, sendo que uma solução ótima deverá apresentar mais unidades em stock do que as obtidas neste valor, mas tal não deverá ser obrigatório, caso contrário será difícil arranjar sempre uma solução, pelo que é importante ter uma função objetiva que procure atingir a melhor solução com isto em consideração, para além das receitas.

### Artigo (só começar após tudo o resto estar perfeito)
1. Atualizar o artigo de acordo com as alterações da ideia incialmente prevista.

2. Completar o estado da arte de aprendizagem automática, adicionando vantagens e desvantagens de cada um dos modelos apresentados, a aplicabilidade de cada um, o modelo escolhido e porquê e no mínimo dois exemplos de aplicações parecidas com a nossa utilizando esse mesmo modelo (e se der tambem um exemplo para os outros, caso encontremos, apresentando uma justificação do porquê que então não utilizámos esse modelo se até foi utilizado para um problema semelhante ao nosso).

3. A mesma coisa descrita no ponto anterior, mas agora para os métodos de planeamento e tomada de decisão, sendo que basta um exemplo de uma aplicação parecida com a nossa, segundo o Carlos Ramos (deve ser mais difícil encontrar isto).

4. Colocar mais referencias no texto do estado da arte, principalmente na explicação de cada modelo/método, sendo que o professor Carlos Ramos sugeriu referenciar sempre o próprio criador do mesmo, sendo que eu concordo com essa abordagem.

5. Completar o resto, nomeadamente o abstrato, conclusão, trabalho futuro, entre outros.

### Trabalho futuro
1. Explorar uma utilização mais avançada das dimensões úteis das lojas, respeitando o respetivo layout, isto é, considerando o conjunto de diferentes segmentos de dimensões úteis da loja e não apenas generalizando. Isto abriria caminho para inúmeras possibilidades, nomeamdamente possibilitando avancarmos para uma solução não só de otimização de stock em unidades, como também do respetivo reposicionamento, complementando o nosso produto.

2. Dando seguimento ao ponto anterior, podem ser explorados os produtos comprados em conjunto, procurando posicioná-los próximos entre si para potencialmente aumentar o número de vendas. Pode também ser explorado o fator peso, isto é, cada segmento de dimensão da loja, em que serão colocados certos produtos, pode possuir uma limitação de peso diferente, ou seja, pode ser mais adequado para produtos mais leves ou produtos mais pesados. Assim, este seria então um fator importante a ter em consideração não so no reposicionamento, como também na própria otimização de unidades em stock, dado que poderá eventualmente limitar as soluções consideradas ótimas.

3. Apresentar uma UI gráfica, talvez uma aplicação web, que facilitaria a utilização do produto, tornando este possivelmente um produto comercializado, em que as empresas pagariam para utilizar este modelo de otimização (e futuramente e idealmente, também de reposicionamento), selecionando as diferentes configurações pretendidas, as dimensões (futuramente até o próprio layout detalhado) de cada uma das suas lojas, anexando um dataset com o histórico de vendas dos seus produtos, devolvendo a recomendação obtida pelos modelos.
