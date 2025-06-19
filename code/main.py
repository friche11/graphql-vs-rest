from experimento import executar_experimento
from analise import analisar_resultados
from analise_avancada import gerar_visualizacoes_avancadas
import os

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n" + "="*40)
    print("PROJETO DE LABORATÓRIO: GraphQL vs. REST")
    print("="*40)
    print("\nEscolha uma opção:")
    print("  1. Executar o experimento (Coletar novos dados)")
    print("  2. Rodar Análise Básica (Gerar Boxplots e Teste T)")
    print("  3. Rodar Análise Avançada (Gerar gráficos para Dashboard)")
    print("  4. Sair")
    print("-"*40)

def main():
    results_path = "../outputs/results.csv"

    while True:
        exibir_menu()
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            print("\n>>> Opção 1 selecionada: Executando o experimento...")
            executar_experimento()
            print("\n>>> Coleta de dados concluída.")

        elif escolha == '2':
            print("\n>>> Opção 2 selecionada: Gerando Análise Básica...")
            if os.path.exists(results_path):
                analisar_resultados()
                print("\n>>> Análise básica concluída. Boxplots gerados.")
            else:
                print(f"\nERRO: O arquivo de resultados '{results_path}' não foi encontrado.")
                print("Por favor, execute a opção 1 primeiro para coletar os dados.")

        elif escolha == '3':
            print("\n>>> Opção 3 selecionada: Gerando Análise Avançada...")
            if os.path.exists(results_path):
                gerar_visualizacoes_avancadas()
                print("\n>>> Análise avançada concluída. Gráficos para dashboard gerados.")
            else:
                print(f"\nERRO: O arquivo de resultados '{results_path}' não foi encontrado.")
                print("Por favor, execute a opção 1 primeiro para coletar os dados.")

        elif escolha == '4':
            print("\nSaindo do programa. Até mais!")
            break

        else:
            print("\nOpção inválida. Por favor, digite um número de 1 a 4.")
        
        input("\nPressione Enter para continuar...")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()