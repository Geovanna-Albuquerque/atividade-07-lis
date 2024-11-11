#Faça um programa que crie uma matriz M (com valores informados do usuário) e mostre a matriz com o dobro
#dos valores lidos (2*M).

def criar_matriz():
    # Solicita as dimensões da matriz
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    # Cria a matriz com valores informados pelo usuário
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

    def multiplicar_matriz_por_2(matriz):
    # Cria uma nova matriz com o dobro dos valores
    matriz_dobrada = []
    for linha in matriz:
        linha_dobrada = [valor * 2 for valor in linha]
        matriz_dobrada.append(linha_dobrada)
    
    return matriz_dobrada

def imprimir_matriz(matriz):
    # Exibe a matriz de forma organizada
    for linha in matriz:
        print(" ".join(map(str, linha)))
        # Função principal
def main():
    # Cria a matriz original
    matriz_original = criar_matriz()
    
    print("\nMatriz original:")
    imprimir_matriz(matriz_original)
    
    # Cria a matriz com o dobro dos valores
    matriz_dobrada = multiplicar_matriz_por_2(matriz_original)
    
    print("\nMatriz com o dobro dos valores:")
    imprimir_matriz(matriz_dobrada)

# Executa o programa
if __name__ == "__main__":
    main()

