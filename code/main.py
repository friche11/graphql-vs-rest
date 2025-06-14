# Importa as funções principais dos outros módulos
from experimento import executar_experimento
from analise import analisar_resultados
import os

def main():
    """
    Função principal que orquestra a execução do projeto de laboratório.
    """
    print(">>> INICIANDO PROJETO DE LABORATÓRIO: GraphQL vs. REST <<<")

    # Etapa 1: Executar o experimento para coletar os dados
    print("\n--- ETAPA 1: EXECUÇÃO DO EXPERIMENTO ---")
    executar_experimento()

    # Etapa 2: Analisar os resultados coletados
    # Verifica se o arquivo de resultados foi realmente criado antes de continuar
    if os.path.exists("results.csv"):
        print("\n--- ETAPA 2: ANÁLISE DOS RESULTADOS ---")
        analisar_resultados()
    else:
        print("\nERRO: O arquivo 'results.csv' não foi criado. A análise foi abortada.")
        print("Verifique sua conexão com a internet ou possíveis erros no script 'experimento.py'.")

    print("\n>>> PROJETO CONCLUÍDO <<<")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
