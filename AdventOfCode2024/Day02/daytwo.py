def verificar_seguranca(linha):
    numeros = list(map(int, linha.split()))
    
    # Verifica se a sequência é crescente ou decrescente
    crescente = all(numeros[i] < numeros[i + 1] and 1 <= numeros[i + 1] - numeros[i] <= 3 for i in range(len(numeros) - 1))
    decrescente = all(numeros[i] > numeros[i + 1] and 1 <= numeros[i] - numeros[i + 1] <= 3 for i in range(len(numeros) - 1))

    return crescente or decrescente

def verificar_com_remocao(linha):
    numeros = list(map(int, linha.split()))
    # Tenta remover cada nível e verifica se a sequência resultante é segura
    for i in range(len(numeros)):
        numeros_sem_um = numeros[:i] + numeros[i+1:]
        if verificar_seguranca(" ".join(map(str, numeros_sem_um))):
            return True
    return False

def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    seguros_sem_remocao = 0
    seguros_com_remocao = 0

    for linha in linhas:
        linha = linha.strip()
        if verificar_seguranca(linha):
            seguros_sem_remocao += 1
            seguros_com_remocao += 1
        elif verificar_com_remocao(linha):
            seguros_com_remocao += 1

    return seguros_sem_remocao, seguros_com_remocao

def main():
    caminho_arquivo = '/home/kitsu/Documentos/Projects/AdventOfCode/Day02/Relatorio.txt'
    seguros_sem_remocao, seguros_com_remocao = processar_arquivo(caminho_arquivo)

    print(f"Quantidade de relatórios seguros sem remoção: {seguros_sem_remocao}")
    print(f"Quantidade de relatórios seguros com remoção: {seguros_com_remocao}")

if __name__ == "__main__":
    main()

