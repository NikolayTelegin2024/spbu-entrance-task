import sys
from collections import deque


def load_matrix(filepath):
    """считываем матрицу инцедетности из текстового файла"""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append([int(x) for x in line.split()])

    if not rows:
        return []

    if len(rows[0]) == 2 and len(rows) == rows[0][0] + 1:
        return rows[1:]

    return rows


def build_reversed_adj(matrix):
    """строим список смежности для обращеного графа"""
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    adj = [[] for _ in range(n)]

    for col in range(m):
        u = None
        v = None
        for row in range(n):
            if matrix[row][col] == -1:
                u = row
            elif matrix[row][col] == 1:
                v = row

        if u is not None and v is not None:
            adj[v].append(u)

    return adj


def count_reachable(start, adj, n):
    """считаем n вершин достижимых из заданной через BFS"""
    visited = [False] * n
    visited[start] = True
    queue = deque([start])
    count = 1

    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)

    return count


def find_universal_vertices(matrix):
    """возвращаем список вершин достижимых из всех остальных"""
    n = len(matrix)
    if n == 0:
        return []
    if n == 1:
        return [1]

    adj = build_reversed_adj(matrix)
    res = []

    for i in range(n):
        if count_reachable(i, adj, n) == n:
            res.append(i + 1)

    return res


def main():
    matrix = load_matrix(sys.argv[1])
    ans = find_universal_vertices(matrix)

    if ans:
        print("Есть такие вершины - ")
        print(" ".join(map(str, ans)))
    else:
        print("Таких вершин нет")


if __name__ == "__main__":
    main()