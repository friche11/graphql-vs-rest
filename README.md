# Análise de Desempenho: GraphQL vs. REST

## Descrição
Este projeto consiste em um experimento controlado, desenvolvido em Python, para comparar quantitativamente o desempenho de APIs **GraphQL** e **REST**. Utilizando a API pública "The Rick and Morty API", o estudo coleta e analisa métricas de performance para responder a questões fundamentais sobre latência e eficiência no tráfego de dados.

## Métricas de Desempenho Avaliadas
Este projeto analisa as seguintes métricas de performance de APIs:

- **Tempo de Resposta (ms)**: Mede a latência total da requisição do ponto de vista do cliente. Corresponde ao tempo decorrido entre o envio da requisição e o recebimento completo da resposta. Um tempo menor indica uma API mais rápida.
- **Tamanho da Resposta (bytes)**: Mede o "peso" total do corpo da resposta HTTP. Um tamanho menor indica uma maior eficiência no uso de dados, o que é crucial para aplicações móveis e com banda limitada, além de evitar o *over-fetching*.

## Requisitos
- Python 3.8 ou superior instalado.
- Conexão com a internet para acessar a API pública.
- (Opcional) Git para clonar o repositório.

*Observação: Não é necessário nenhum token de acesso, pois a API utilizada é pública.*

## Instruções de Execução

1. **Estrutura de Pastas:**
   Clone ou crie a seguinte estrutura de pastas para o projeto, garantindo que os scripts estejam dentro da pasta `code`:
   ```
   /seu-projeto
   |-- /code
   |   |-- main.py
   |   |-- experimento.py
   |   |-- analise.py
   |-- /docs
   |-- /outputs
   |-- requirements.txt
   |-- README.md
   ```

2. **Instale as Dependências:**
   Navegue até a pasta raiz do projeto (`/seu-projeto`) e instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o Projeto Completo:**
   Para rodar o experimento e a análise, execute o script principal a partir da pasta `code`. Este único comando cuidará de tudo.
   ```bash
   cd code
   python main.py
   ```
   O script irá primeiro executar o experimento (coletando 200 pontos de dados) e, em seguida, realizará a análise estatística e a geração dos gráficos.

## Saída Esperada
Após a execução, os seguintes artefatos serão gerados:

- **`../outputs/results.csv`**: Um arquivo CSV contendo os dados brutos de todas as 200 medições (tempo e tamanho para cada requisição).
- **`../docs/rq1_tempo_boxplot.png`**: Um gráfico de boxplot comparando o tempo de resposta entre GraphQL e REST.
- **`../docs/rq2_tamanho_boxplot.png`**: Um gráfico de boxplot comparando o tamanho da resposta entre as duas APIs.
- **Relatório no Terminal**: O terminal exibirá as estatísticas descritivas (média, mediana) e os resultados dos testes de hipóteses (p-values).

## Observações
- Os resultados do tempo de resposta podem variar ligeiramente a cada execução devido a flutuações nas condições da rede e na carga do servidor da API pública.
- O código está preparado para criar as pastas `outputs` e `docs` automaticamente caso elas não existam.
- Para uma análise aprofundada dos resultados e conclusões, consulte o **Relatório Final** que está dentro da pasta `docs`.
