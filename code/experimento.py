import requests
import time
import pandas as pd
import os # Importa o módulo 'os' para manipulação de pastas e caminhos

# --- Configurações do Experimento (sem alterações) ---
N_MEDICOES = 50
API_URL_REST = "https://rickandmortyapi.com/api/character/1"
API_URL_GRAPHQL = "https://rickandmortyapi.com/graphql"

QUERY_SIMPLE_GRAPHQL = """
query { character(id: 1) { name status } }
"""
QUERY_COMPLEX_GRAPHQL = """
query { character(id: 1) { name status episode { name air_date } } }
"""
API_URL_REST_COMPLEX = "https://rickandmortyapi.com/api/character/1"

def executar_experimento():
    """
    Função principal para executar todos os trials do experimento.
    """
    print("Iniciando a coleta de dados...")
    results = []
    headers = { 'Cache-Control': 'no-cache', 'Pragma': 'no-cache' }

    for i in range(N_MEDICOES):
        try:
            print(f"Executando medição {i + 1}/{N_MEDICOES}...", end='\r')
            
            # --- Coleta de dados (sem alterações na lógica) ---
            # T1: Simples REST
            start_time = time.perf_counter()
            r = requests.get(API_URL_REST, headers=headers)
            r.raise_for_status()
            results.append({
                "medicao": i + 1, "api_type": "REST", "query_type": "Simples",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })
            # T2: Simples GraphQL
            start_time = time.perf_counter()
            r = requests.post(API_URL_GRAPHQL, json={'query': QUERY_SIMPLE_GRAPHQL}, headers=headers)
            r.raise_for_status()
            results.append({
                "medicao": i + 1, "api_type": "GraphQL", "query_type": "Simples",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })
            # T3: Complexa REST
            start_time = time.perf_counter()
            r = requests.get(API_URL_REST_COMPLEX, headers=headers)
            r.raise_for_status()
            results.append({
                "medicao": i + 1, "api_type": "REST", "query_type": "Complexa",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })
            # T4: Complexa GraphQL
            start_time = time.perf_counter()
            r = requests.post(API_URL_GRAPHQL, json={'query': QUERY_COMPLEX_GRAPHQL}, headers=headers)
            r.raise_for_status()
            results.append({
                "medicao": i + 1, "api_type": "GraphQL", "query_type": "Complexa",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })
            
            time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            print(f"\nErro na medição {i + 1}: {e}. Pulando para a próxima.")
            continue
            
    # --- ALTERAÇÃO PRINCIPAL AQUI ---
    df_results = pd.DataFrame(results)
    
    # Define o diretório de saída um nível acima da pasta atual
    output_dir = "../outputs"
    # Garante que o diretório de saída exista; se não, cria-o
    os.makedirs(output_dir, exist_ok=True)
    
    # Constrói o caminho completo para o arquivo CSV
    output_path = os.path.join(output_dir, "results.csv")
    df_results.to_csv(output_path, index=False)
    
    print(f"\n\nExperimento concluído! Resultados salvos em: {output_path}")

if __name__ == "__main__":
    executar_experimento()