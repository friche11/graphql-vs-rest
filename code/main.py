from experimento import executar_experimento
from analise import analisar_resultados
import os

def main():
    """
    Função principal que orquestra a execução do projeto de laboratório.
    """
    print(">>> INICIANDO PROJETO DE LABORATÓRIO: GraphQL vs. REST <<<")

    # Etapa 1: Executar o experimento
    print("\n--- ETAPA 1: EXECUÇÃO DO EXPERIMENTO ---")
    executar_experimento()

    # --- ALTERAÇÃO AQUI ---
    # Define o caminho para o arquivo de resultados
    results_path = "../outputs/results.csv"

    # Etapa 2: Analisar os resultados, verificando o caminho correto
    if os.path.exists(results_path):
        print("\n--- ETAPA 2: ANÁLISE DOS RESULTADOS ---")
        analisar_resultados()
    else:
        print(f"\nERRO: O arquivo '{results_path}' não foi criado. A análise foi abortada.")
        print("Verifique sua conexão com a internet ou possíveis erros no script 'experimento.py'.")

    print("\n>>> PROJETO CONCLUÍDO <<<")

if __name__ == "__main__":
    main()