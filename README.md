# Análise de Desempenho: GraphQL vs. REST

## Descrição
Este projeto consiste em um experimento controlado, desenvolvido em Python, para comparar quantitativamente o desempenho de APIs **GraphQL** e **REST**. Utilizando a API pública "The Rick and Morty API", o estudo coleta e analisa métricas de performance para responder a questões fundamentais sobre latência e eficiência no tráfego de dados.

## Métricas de Desempenho Avaliadas
Este projeto analisa as seguintes métricas de performance de APIs:

- **Tempo de Resposta (ms)**: Mede a latência total da requisição do ponto de vista do cliente. Corresponde ao tempo decorrido entre o envio da requisição e o recebimento completo da resposta.
- **Tamanho da Resposta (bytes)**: Mede o "peso" total do corpo da resposta HTTP. Um tamanho menor indica uma maior eficiência no uso de dados e evita o *over-fetching*.

## Requisitos
- Python 3.8 ou superior instalado.
- Conexão com a internet para acessar a API pública.
- (Opcional) Git para clonar o repositório.

*Observação: Não é necessário nenhum token de acesso, pois a API utilizada é pública.*

## Instruções de Execução

1. **Estrutura de Pastas:**
   Garanta que seu projeto tenha a seguinte estrutura, com todos os scripts Python dentro da pasta `code`:
   ```
   /graphql-rest-experiment
   |-- /code
   |   |-- main.py
   |   |-- experimento.py
   |   |-- analise.py
   |   |-- analise_avancada.py
   |-- /docs
   |-- /outputs
   |-- requirements.txt
   |-- README.md
   ```

2. **Instale as Dependências:**
   Navegue até a pasta raiz do projeto e instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o Menu Principal:**
   Para rodar o projeto, navegue até a pasta `code` e execute o script `main.py`.
   ```bash
   cd code
   python main.py
   ```
   Você verá um menu interativo. Siga as opções:
    - **Opção 1:** Para executar o experimento de coleta de dados. Isso irá (re)gerar o arquivo `results.csv`.
    - **Opção 2:** Para rodar a análise básica e gerar os gráficos de **Boxplot**.
    - **Opção 3:** Para rodar a análise avançada e gerar os gráficos de **Barras, Densidade e Linhas** para o dashboard.

## Saída Esperada
Após a execução das opções do menu, os seguintes artefatos serão gerados:

- **`../outputs/results.csv`**: Arquivo CSV contendo os dados brutos de todas as medições. (Gerado pela Opção 1)
- **`../docs/rq1_tempo_boxplot.png`**: Gráfico de boxplot comparando o tempo de resposta. (Gerado pela Opção 2)
- **`../docs/rq2_tamanho_boxplot.png`**: Gráfico de boxplot comparando o tamanho da resposta. (Gerado pela Opção 2)
- **`../docs/fig_barras_medias.png`**: Gráfico de barras comparando as médias de performance. (Gerado pela Opção 3)
- **`../docs/fig_densidade_tempo.png`**: Gráfico de densidade mostrando a distribuição dos tempos. (Gerado pela Opção 3)
- **`../docs/fig_linha_pareada.png`**: Gráfico de linhas mostrando a consistência pareada das medições. (Gerado pela Opção 3)

## Observações
- Os resultados do tempo de resposta podem variar ligeiramente a cada execução devido a flutuações nas condições da rede.
- O código está preparado para criar as pastas `outputs` e `docs` automaticamente caso elas não existam.
- Para uma análise aprofundada dos resultados e conclusões, consulte o **Relatório Final** que se encontra na pasta `docs`.