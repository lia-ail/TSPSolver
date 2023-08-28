def dynamic_solution(matrix_vals, first_vertex=4):
    def func(i, mask):
        if mask == ((first_vertex << i) | 3):
            return matrix_vals[1][i]

        if memo[i][mask] != -1:
            return memo[i][mask]

        res = float("inf")

        for j in range(1, n + 1):
            if (mask & (i << j)) != 0 and j != 1 and j != i:
                res = min(res, func(j, mask & (~(1 << i))) + matrix_vals[j][i])
        memo[i][mask] = res
        return res

    n = len(matrix_vals)

    for i in range(n):
        matrix_vals[i] = [0] + matrix_vals[i]

    matrix_vals = [[0] * (n+1)] + matrix_vals

    memo = [[-1] * (1 << (n + 1)) for _ in range(n+1)]

    ans = float("inf")

    for i in range(1, n+1):
        ans = min(ans, func(i, (1 << (n + 1))-1) + matrix_vals[i][first_vertex])

    return ans


print(dynamic_solution([[0, 16, 11, 6], [8, 0, 13, 16], [4, 7, 0, 9], [5, 12, 2, 0]]))
