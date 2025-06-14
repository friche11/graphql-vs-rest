import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

def analisar_resultados():
    """
    Função para carregar os dados do CSV, analisar e gerar gráficos.
    """
    file_path = "results.csv"
    if not os.path.exists(file_path):
        print(f"Arquivo '{file_path}' não encontrado. Execute o experimento primeiro.")
        return

    print("Iniciando a análise dos resultados...")
    df = pd.read_csv(file_path)

    # --- Análise Descritiva ---
    print("\n--- Estatísticas Descritivas ---")
    print(df.groupby(['api_type', 'query_type']).agg({
        'time_ms': ['mean', 'std', 'median'],
        'size_bytes': ['mean', 'std', 'median']
    }))

    sns.set_theme(style="whitegrid")

    # --- Análise RQ1: Tempo de Resposta ---
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='query_type', y='time_ms', hue='api_type', order=['Simples', 'Complexa'])
    plt.title('RQ1: Comparação do Tempo de Resposta (ms)', fontsize=16)
    plt.xlabel('Tipo de Consulta', fontsize=12)
    plt.ylabel('Tempo de Resposta (ms)', fontsize=12)
    plt.savefig("rq1_tempo_boxplot.png")
    print("\nGráfico 'rq1_tempo_boxplot.png' salvo.")
    plt.close() # Fecha a figura para liberar memória

    # --- Análise RQ2: Tamanho da Resposta ---
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='query_type', y='size_bytes', hue='api_type', order=['Simples', 'Complexa'])
    plt.title('RQ2: Comparação do Tamanho da Resposta (bytes)', fontsize=16)
    plt.xlabel('Tipo de Consulta', fontsize=12)
    plt.ylabel('Tamanho da Resposta (bytes)', fontsize=12)
    plt.savefig("rq2_tamanho_boxplot.png")
    print("Gráfico 'rq2_tamanho_boxplot.png' salvo.")
    plt.close()

    # --- Testes Estatísticos ---
    print("\n--- Testes de Hipóteses (p-value < 0.05 indica diferença significativa) ---")
    rest_data = df[df['api_type'] == 'REST']
    gql_data = df[df['api_type'] == 'GraphQL']

    for query_t in ['Simples', 'Complexa']:
        print(f"\nResultados para Consulta '{query_t}':")
        # Tempo
        t_stat_time, p_value_time = stats.ttest_rel(
            rest_data[rest_data['query_type'] == query_t]['time_ms'],
            gql_data[gql_data['query_type'] == query_t]['time_ms']
        )
        print(f"  RQ1 (Tempo)   -> p-value: {p_value_time:.6f}")
        # Tamanho
        t_stat_size, p_value_size = stats.ttest_rel(
            rest_data[rest_data['query_type'] == query_t]['size_bytes'],
            gql_data[gql_data['query_type'] == query_t]['size_bytes']
        )
        print(f"  RQ2 (Tamanho) -> p-value: {p_value_size:.6f}")

# Este bloco permite que o arquivo seja executado de forma independente
if __name__ == "__main__":
    analisar_resultados()
