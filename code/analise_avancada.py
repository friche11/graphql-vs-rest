import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_visualizacoes_avancadas():
    
    csv_path = "../outputs/results.csv"
    docs_dir = "../docs"

    if not os.path.exists(csv_path):
        print(f"Arquivo de resultados '{csv_path}' não encontrado.")
        return

    os.makedirs(docs_dir, exist_ok=True)
    df = pd.read_csv(csv_path)
    
    # Prepara o tema dos gráficos
    sns.set_theme(style="whitegrid")
    palette = {"REST": "b", "GraphQL": "chocolate"}

    # --- 1. Gráfico de Barras para comparar as médias ---
    df_mean = df.groupby(['api_type', 'query_type']).mean().reset_index()

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Comparação das Médias de Performance', fontsize=18)

    # Gráfico de barras para Tempo de Resposta
    sns.barplot(data=df_mean, x='query_type', y='time_ms', hue='api_type', ax=axes[0], palette=palette)
    axes[0].set_title('Tempo de Resposta Médio (ms)')
    axes[0].set_xlabel('Tipo de Consulta')
    axes[0].set_ylabel('Tempo Médio (ms)')
    
    # Gráfico de barras para Tamanho da Resposta
    sns.barplot(data=df_mean, x='query_type', y='size_bytes', hue='api_type', ax=axes[1], palette=palette)
    axes[1].set_title('Tamanho da Resposta Médio (bytes)')
    axes[1].set_xlabel('Tipo de Consulta')
    axes[1].set_ylabel('Tamanho Médio (bytes)')
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(docs_dir, "fig_barras_medias.png"))
    print(f"Gráfico de barras salvo em '{docs_dir}/fig_barras_medias.png'")
    plt.close()

    # --- 2. Gráfico de Densidade (KDE) para distribuição do tempo ---
    plt.figure(figsize=(12, 7))
    sns.kdeplot(data=df, x='time_ms', hue='api_type', fill=True, common_norm=False, palette=palette, alpha=0.5)
    plt.title('Distribuição do Tempo de Resposta (ms)', fontsize=16)
    plt.xlabel('Tempo de Resposta (ms)')
    plt.ylabel('Densidade')
    plt.savefig(os.path.join(docs_dir, "fig_densidade_tempo.png"))
    print(f"Gráfico de densidade salvo em '{docs_dir}/fig_densidade_tempo.png'")
    plt.close()

    # --- 3. Gráfico de Linhas por Medição (Comparação Pareada) ---
    df_pivot = df.pivot_table(index='medicao', columns=['api_type', 'query_type'], values='time_ms')
    
    fig, axes = plt.subplots(2, 1, figsize=(16, 12), sharex=True)
    fig.suptitle('Performance do Tempo de Resposta a Cada Medição', fontsize=18)
    
    # Gráfico de linha para Consultas Simples
    df_pivot.plot(y=[('REST', 'Simples'), ('GraphQL', 'Simples')], ax=axes[0], style='-o', markersize=4)
    axes[0].set_title('Consulta Simples')
    axes[0].set_ylabel('Tempo (ms)')
    axes[0].legend(['REST', 'GraphQL'])
    axes[0].grid(True)
    
    # Gráfico de linha para Consultas Complexas
    df_pivot.plot(y=[('REST', 'Complexa'), ('GraphQL', 'Complexa')], ax=axes[1], style='-o', markersize=4)
    axes[1].set_title('Consulta Complexa')
    axes[1].set_ylabel('Tempo (ms)')
    axes[1].set_xlabel('Número da Medição (Trial)')
    axes[1].legend(['REST', 'GraphQL'])
    axes[1].grid(True)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(os.path.join(docs_dir, "fig_linha_pareada.png"))
    print(f"Gráfico de linhas salvo em '{docs_dir}/fig_linha_pareada.png'")
    plt.close()
    
    print("\nVisualizações avançadas geradas com sucesso.")

if __name__ == "__main__":
    gerar_visualizacoes_avancadas()