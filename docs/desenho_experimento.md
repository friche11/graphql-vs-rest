# Desenho do Experimento Controlado: GraphQL vs. REST

Este documento detalha o planejamento experimental para comparar quantitativamente o desempenho de APIs GraphQL e REST, com base nas perguntas de pesquisa RQ1 (velocidade) e RQ2 (tamanho da resposta).

### A. Hipóteses Nula e Alternativa

Para cada pergunta de pesquisa, formulamos as seguintes hipóteses:

* **Para RQ1 (Tempo de Resposta):**
    * **H1_0 (Hipótese Nula):** Não existe diferença estatisticamente significativa entre o tempo médio de resposta de uma consulta GraphQL e o de sua consulta REST equivalente.
    * **H1_A (Hipótese Alternativa):** Existe uma diferença estatisticamente significativa entre o tempo médio de resposta de uma consulta GraphQL e o de sua consulta REST equivalente.
* **Para RQ2 (Tamanho da Resposta):**
    * **H2_0 (Hipótese Nula):** Não existe diferença estatisticamente significativa entre o tamanho médio do corpo da resposta de uma consulta GraphQL e o de sua consulta REST equivalente.
    * **H2_A (Hipótese Alternativa):** Existe uma diferença estatisticamente significativa entre o tamanho médio do corpo da resposta de uma consulta GraphQL e o de sua consulta REST equivalente.

### B. Variáveis

* **Variáveis Independentes:** O fator que manipulamos.
    * **Tipo de API:** Categórica com dois níveis: (1) GraphQL, (2) REST.
    * **Complexidade da Consulta:** Categórica com dois níveis: (1) Consulta Simples, (2) Consulta Complexa.
* **Variáveis Dependentes:** O que medimos para avaliar o efeito.
    * **Tempo de Resposta (ms):** Numérica. Medido do momento do envio da requisição até o recebimento completo da resposta.
    * **Tamanho da Resposta (bytes):** Numérica. Medido pelo tamanho total do corpo (`content`) da resposta HTTP.

### C. Tratamentos

Os tratamentos são as combinações das variáveis independentes que aplicaremos:

1.  **T1:** Executar uma consulta **simples** na API **REST**.
2.  **T2:** Executar uma consulta **simples** na API **GraphQL**.
3.  **T3:** Executar uma consulta **complexa** na API **REST**.
4.  **T4:** Executar uma consulta **complexa** na API **GraphQL**.

### D. Objetos Experimentais

* **API Alvo:** A API pública **"The Rick and Morty API"** ([https://rickandmortyapi.com/](https://rickandmortyapi.com/)), que oferece acesso aos mesmos dados via REST e GraphQL.
    * **Endpoint REST:** `https://rickandmortyapi.com/api`
    * **Endpoint GraphQL:** `https://rickandmortyapi.com/graphql`
* **Consultas Definidas:**
    * **Simples:** Buscar os dados de um único personagem (ex: Rick Sanchez, ID=1).
    * **Complexa:** Buscar os dados de um único personagem (ID=1) e, para esse personagem, o nome e a data de exibição dos 5 primeiros episódios em que ele apareceu.

### E. Tipo de Projeto Experimental

Utilizaremos um **projeto fatorial 2x2 (within-subjects)**.

* **Fatorial:** Porque temos duas variáveis independentes (Tipo de API, Complexidade da Consulta).
* **Within-subjects (Medidas Repetidas):** Porque as mesmas consultas conceituais são submetidas a ambos os tratamentos (REST e GraphQL), permitindo uma comparação pareada que reduz a variabilidade.

### F. Quantidade de Medições

Para cada um dos 4 tratamentos, realizaremos **50 medições (trials)**. Isso totaliza **200 pontos de dados**, uma quantidade robusta para a aplicação de testes estatísticos como o Teste T de Student para amostras pareadas.

### G. Ameaças à Validade

* **Validade Interna:**
    * **Flutuações de Rede:** A latência da internet pode variar.
        * **Mitigação:** Executar os trials para REST e GraphQL de forma intercalada e em um curto período para minimizar variações temporais.
    * **Caching:** Caching no servidor ou em proxies pode levar a tempos de resposta irreais.
        * **Mitigação:** Adicionar headers na requisição para desabilitar o cache (ex: `Cache-Control: no-cache`).
* **Validade Externa:**
    * **Representatividade da API:** Os resultados obtidos podem não ser generalizáveis para todas as APIs.
        * **Conclusão:** Os resultados devem ser discutidos dentro do contexto da API do Rick and Morty.
* **Validade de Construto:**
    * **Medição de Tempo:** O tempo medido pelo script Python inclui a latência da rede e o processamento local.
        * **Mitigação:** Ser consistente na forma de medição (usar `time.perf_counter`) e reconhecer que é uma medição *end-to-end* do ponto de vista do cliente.