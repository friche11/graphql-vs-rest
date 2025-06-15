# Relatório Final

## 1. Introdução

A linguagem de consulta GraphQL representa uma alternativa moderna às tradicionais APIs REST. Proposta pelo Facebook, sua abordagem baseada em grafos permite que clientes solicitem exatamente os dados de que necessitam, evitando o over-fetching (excesso de dados) e o under-fetching (necessidade de múltiplas chamadas) comuns em REST. Apesar da crescente adoção do GraphQL, os benefícios quantitativos em cenários práticos nem sempre são claros.

Neste contexto, o objetivo deste estudo é realizar um **experimento controlado** para avaliar quantitativamente os benefícios da adoção de uma API GraphQL em detrimento de uma API REST. Especificamente, buscaremos responder às seguintes perguntas de pesquisa:

- **RQ1:** Respostas às consultas GraphQL são mais rápidas que respostas às consultas REST?
- **RQ2:** Respostas às consultas GraphQL têm tamanho menor que respostas às consultas REST?

## 2. Metodologia

Para responder às questões de pesquisa, realizamos um experimento controlado seguindo os passos de desenho, preparação, execução e análise.

### 2.1 Desenho do Experimento

O experimento foi estruturado com base nos seguintes elementos:

* **Hipóteses:**
    * **H1_0 (Tempo):** Não existe diferença estatisticamente significativa entre o tempo médio de resposta de uma consulta GraphQL e o de sua consulta REST equivalente.
    * **H2_0 (Tamanho):** Não existe diferença estatisticamente significativa entre o tamanho médio da resposta de uma consulta GraphQL e o de sua consulta REST equivalente.

* **Variáveis:**
    * **Independentes:** Tipo de API (REST, GraphQL) e Complexidade da Consulta (Simples, Complexa).
    * **Dependentes:** Tempo de Resposta (ms) e Tamanho da Resposta (bytes).

* **Objetos e Tratamentos:**
    * Utilizamos a API pública **"The Rick and Morty API"**, que oferece acesso aos mesmos dados via REST e GraphQL, como nosso objeto de estudo.
    * Definimos 4 tratamentos distintos baseados na combinação das variáveis independentes (T1: REST Simples, T2: GraphQL Simples, T3: REST Complexa, T4: GraphQL Complexa).

* **Ambiente e Execução:**
    * O experimento foi executado em um ambiente de desenvolvimento padrão, utilizando scripts Python com as bibliotecas `requests`, `pandas`, `matplotlib`, `seaborn` e `scipy`.
    * Realizamos **50 medições** para cada um dos 4 tratamentos, totalizando 200 pontos de dados. Para mitigar o efeito de flutuações de rede e caching, as requisições foram intercaladas e enviadas com headers `Cache-Control: no-cache`.

### 2.2 Análise de Dados

1. **Execução e Coleta:** Um script Python (`experimento.py`) realizou as 200 requisições aos endpoints da API, medindo o tempo de resposta e o tamanho do conteúdo de cada chamada e salvando os resultados em um arquivo `results.csv`.
2. **Análise e Validação:** Um segundo script (`analise.py`) processou o arquivo `results.csv`. Foram geradas estatísticas descritivas (média, mediana, desvio padrão) para validar os dados e observar as tendências. Para a análise inferencial, aplicamos o **Teste T de Student para amostras pareadas**, adequado ao nosso projeto *within-subjects*, para verificar a significância estatística das diferenças observadas.

## 3. Resultados

A análise dos dados coletados revelou diferenças claras entre as duas tecnologias. A tabela abaixo resume as estatísticas descritivas encontradas na execução final:

| api_type  | query_type | time_ms (mean) | time_ms (median) | size_bytes (mean) |
| :---      | :---       | :---           | :---             | :---              |
| **GraphQL** | Complexa   | 359.87         | 355.26           | 3307.0            |
|           | Simples    | 362.17         | 360.33           | 63.0              |
| **REST** | Complexa   | 325.67         | 322.35           | 2719.0            |
|           | Simples    | 331.13         | 323.59           | 2719.0            |

### RQ1: Relação de Velocidade entre GraphQL e REST

A análise numérica mostra que as respostas da API REST foram, em média, mais rápidas que as da API GraphQL para ambos os tipos de consulta. Para a consulta complexa, por exemplo, a média de tempo do REST foi de 325.67 ms, enquanto a do GraphQL foi de 359.87 ms. As medianas seguem a mesma tendência.

O Teste T pareado confirmou que essa diferença é altamente significativa. Para ambos os tipos de consulta (simples e complexa), o p-value obtido foi de 0.000000, o que nos permite rejeitar a hipótese nula com o máximo de confiança estatística.

**Conclusão para RQ1:** Rejeitamos a hipótese nula (H1_0). Existe uma diferença significativa, e, neste experimento, a API REST apresentou menor latência.

### RQ2: Relação de Tamanho entre GraphQL e REST

Os resultados para o tamanho da resposta demonstram a principal vantagem do GraphQL. Para a consulta simples, GraphQL foi drasticamente mais eficiente, retornando apenas 63 bytes contra os 2719 bytes do REST. Isso representa uma redução de 97.7% no tráfego de dados, pois o REST retornou o objeto completo do personagem (over-fetching), enquanto GraphQL entregou apenas os campos solicitados.

O Teste T confirmou que a diferença no tamanho é extremamente significativa, com um p-value de 0.000000.

**Conclusão para RQ2:** Rejeitamos a hipótese nula (H2_0). GraphQL oferece respostas com tamanho significativamente menor, especialmente ao evitar o over-fetching.

## 4. Discussão

Os resultados deste experimento fornecem uma visão matizada sobre a performance de GraphQL e REST.

A superioridade do **REST em termos de velocidade** pode ser atribuída à natureza de seus endpoints. Um endpoint REST é, geralmente, uma operação pré-definida e otimizada no servidor. Em contrapartida, o servidor GraphQL precisa de uma etapa adicional para interpretar e resolver a consulta arbitrária enviada pelo cliente, o que pode introduzir uma pequena sobrecarga na latência.

Por outro lado, a vantagem do **GraphQL no tamanho dos dados** é inquestionável e representa seu maior benefício prático. A capacidade de solicitar apenas os campos necessários é crucial para aplicações sensíveis à banda, como em redes móveis. Além disso, a habilidade de agregar dados relacionados em uma única chamada (como visto na consulta complexa) simplifica a lógica do cliente e reduz drasticamente o número total de requisições, mitigando o problema N+1.

## 5. Conclusão Final

Este estudo comparou quantitativamente o desempenho de APIs GraphQL e REST através de um experimento controlado. Concluímos que:

1.  **Não há garantia de que GraphQL seja mais rápido.** No nosso cenário, a API REST apresentou tempos de resposta inferiores com significância estatística.
2.  **GraphQL é drasticamente mais eficiente no uso de dados.** Ele reduz significativamente o tamanho do payload ao evitar o over-fetching e pode diminuir a complexidade do cliente ao resolver consultas aninhadas em uma única chamada.

A escolha entre GraphQL e REST, portanto, não é uma questão de superioridade absoluta, mas de um **trade-off**. Para aplicações onde a eficiência de dados e a flexibilidade do cliente são primordiais, GraphQL é uma escolha poderosa. Para cenários onde a latência mínima em endpoints simples e fixos é o fator mais crítico, REST continua sendo uma solução robusta e performática.