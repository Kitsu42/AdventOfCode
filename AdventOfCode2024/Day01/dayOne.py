import os

from collections import Counter

def txtToArrays(filename):

    #Lê um arquivo .txt e retorna duas listas de inteiros.

    if not os.path.exists(filename):
        raise FileNotFoundError(f"O arquivo {filename} não foi encontrado.")
    left_coordinates, right_coordinates = [], []
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) != 2:
                raise ValueError("Cada linha do arquivo deve conter exatamente dois valores.")
            try:
                left_coordinates.append(int(values[0]))
                right_coordinates.append(int(values[1]))
            except ValueError:
                raise ValueError("Os valores no arquivo devem ser números inteiros.")
    return left_coordinates, right_coordinates

def calculate_frequency(numbers):
    #Calcula a frequência de cada número em uma lista.

    return Counter(numbers)

def calculate_similarity(left_list, right_list):
    #Calcula a pontuação de similaridade entre duas listas.
    
    right_freq = calculate_frequency(right_list)
    similarity_score = 0

    for num in left_list:
        similarity_score += num * right_freq.get(num, 0)  # Multiplica o número pela sua frequência na lista direita

    return similarity_score

if __name__ == "__main__":
    filename = 'coordenadas.txt'
    try:
        # Ler as listas
        left_list, right_list = txtToArrays(filename)

        # Calcular a distância
        distance_result = sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))
        print(f"A distância calculada é: {distance_result}")

        # Calcular a frequência
        left_freq = calculate_frequency(left_list)
        right_freq = calculate_frequency(right_list)

        # Calcular a pontuação de similaridade
        similarity_score = calculate_similarity(left_list, right_list)
        print(f"A pontuação de similaridade é: {similarity_score}")

    except (FileNotFoundError, ValueError) as e:
        print(f"Erro: {e}")
