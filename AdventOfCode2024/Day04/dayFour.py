def count_x_mas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Verifica se a posição está dentro dos limites da grade
    def is_valid_position(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Verifica se o padrão "X-MAS" existe em uma posição central (r, c)
    def find_x_mas_from(r, c):
        # Lista de padrões "X-MAS" com suas posições relativas
        patterns = [
            ([(0, 0), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)], "AM.SM.S"),
            ([(0, 0), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)], "AS.MS.S")
        ]

        # Testa cada padrão em relação às posições relativas
        for positions, expected_chars in patterns:
            for (dr, dc), char in zip(positions, expected_chars):
                nr, nc = r + dr, c + dc
                if not is_valid_position(nr, nc) or grid[nr][nc] != char:
                    break
            else:  # Apenas executado se o "for" completar sem "break"
                return True

        return False

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A" and find_x_mas_from(r, c):
                count += 1

    return count

# Ler o arquivo e transformar em uma matriz 2D
file_path = '/home/kitsu/Documentos/Projects/AdventOfCode/Day04/Relatorio.txt'

with open(file_path, 'r') as file:
    search_grid = [list(line.strip()) for line in file if line.strip()]

# Contar ocorrências de X-MAS
result = count_x_mas_occurrences(search_grid)
print(f"O padrão 'X-MAS' aparece {result} vezes na busca de palavras.")

# PORQUE ESSA MERDA NÃO ESTA FUNCIONANDO??????????????????????????