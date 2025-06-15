import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os # Importa o módulo 'os'

def analisar_resultados():
    """
    Função para carregar os dados do CSV, analisar e gerar gráficos.
    """
    # --- ALTERAÇÃO 1: Definir os caminhos corretos ---
    csv_path = "../outputs/results.csv"
    docs_dir = "../docs"

    # Garante que o diretório de docs exista; se não, cria-o
    os.makedirs(docs_dir, exist_ok=True)
    
    if not os.path.exists(csv_path):
        print(f"Arquivo '{csv_path}' não encontrado. Execute o experimento primeiro.")
        return

    print("Iniciando a análise dos resultados...")
    df = pd.read_csv(csv_path)

    # --- Análise Descritiva (sem alterações) ---
    print("\n--- Estatísticas Descritivas ---")
    print(df.groupby(['api_type', 'query_type']).agg({
        'time_ms': ['mean', 'std', 'median'],
        'size_bytes': ['mean', 'std', 'median']
    }))

    sns.set_theme(style="whitegrid")

    # --- ALTERAÇÃO 2: Salvar gráficos na pasta /docs ---
    # Gráfico RQ1: Tempo de Resposta
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='query_type', y='time_ms', hue='api_type', order=['Simples', 'Complexa'])
    plt.title('RQ1: Comparação do Tempo de Resposta (ms)', fontsize=16)
    plt.savefig(os.path.join(docs_dir, "rq1_tempo_boxplot.png"))
    print(f"\nGráfico 'rq1_tempo_boxplot.png' salvo na pasta '{docs_dir}'.")
    plt.close()

    # Gráfico RQ2: Tamanho da Resposta
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='query_type', y='size_bytes', hue='api_type', order=['Simples', 'Complexa'])
    plt.title('RQ2: Comparação do Tamanho da Resposta (bytes)', fontsize=16)
    plt.savefig(os.path.join(docs_dir, "rq2_tamanho_boxplot.png"))
    print(f"Gráfico 'rq2_tamanho_boxplot.png' salvo na pasta '{docs_dir}'.")
    plt.close()

    # --- Testes Estatísticos (sem alterações) ---
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

if __name__ == "__main__":
    analisar_resultados()