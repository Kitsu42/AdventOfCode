import re

def somar_resultados_de_multiplicacoes(memoria_corrompida):
    padrao_mul = r"mul\((\d+),(\d+)\)"
    padrao_comando = r"(do\(\)|don't\(\))"

    multiplicacoes_ativadas = True
    soma_resultados = 0
    
    # Dividir a memória em blocos processáveis
    partes = re.split(f"({padrao_mul}|{padrao_comando})", memoria_corrompida)
    
    for parte in partes:
        if not parte:
            continue
        if parte == "do()":
            multiplicacoes_ativadas = True
        elif parte == "don't()":
            multiplicacoes_ativadas = False
        else:
            match = re.match(padrao_mul, parte)
            if match and multiplicacoes_ativadas:
                x, y = map(int, match.groups())
                soma_resultados += x * y

    return soma_resultados

# Caminho do arquivo de memória corrompida
caminho_memoria = '/home/kitsu/Documentos/Projects/AdventOfCode/Day03/Relatorio.txt'

# Ler o conteúdo do arquivo
with open(caminho_memoria, 'r') as arquivo:
    memoria = arquivo.read()

# Chamar a função e exibir o resultado
resultado = somar_resultados_de_multiplicacoes(memoria)
print(f"Soma dos resultados das multiplicações válidas: {resultado}")
