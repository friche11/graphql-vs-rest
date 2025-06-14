import requests
import time
import pandas as pd

# --- Configurações do Experimento ---
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
        # Usamos try/except para garantir que o experimento não pare por uma falha de rede
        try:
            print(f"Executando medição {i + 1}/{N_MEDICOES}...", end='\r')

            # --- T1: Simples REST ---
            start_time = time.perf_counter()
            r = requests.get(API_URL_REST, headers=headers)
            r.raise_for_status() # Lança erro se a requisição falhar
            results.append({
                "medicao": i + 1, "api_type": "REST", "query_type": "Simples",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })

            # --- T2: Simples GraphQL ---
            start_time = time.perf_counter()
            r = requests.post(API_URL_GRAPHQL, json={'query': QUERY_SIMPLE_GRAPHQL}, headers=headers)
            r.raise_for_status()
            results.append({
                "medicao": i + 1, "api_type": "GraphQL", "query_type": "Simples",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })
            
            # --- T3: Complexa REST ---
            start_time = time.perf_counter()
            r = requests.get(API_URL_REST_COMPLEX, headers=headers)
            r.raise_for_status()
            results.append({
                "medicao": i + 1, "api_type": "REST", "query_type": "Complexa",
                "time_ms": (time.perf_counter() - start_time) * 1000,
                "size_bytes": len(r.content)
            })

            # --- T4: Complexa GraphQL ---
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
            
    # Salvar resultados
    df_results = pd.DataFrame(results)
    output_path = "results.csv"
    df_results.to_csv(output_path, index=False)
    print(f"\n\nExperimento concluído! Resultados salvos em: {output_path}")

# Este bloco permite que o arquivo seja executado de forma independente
if __name__ == "__main__":
    executar_experimento()
