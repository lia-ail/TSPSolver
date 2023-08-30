def dynamic_solution(matrix_vals):
    def func(i, mask):
        if mask == ((1 << i) | 3):
            return matrix_vals[1][i], [1, i]

        """
        Base case, if there is no more vertices, return value from our input matrix 
        and indexes of first and current vertices
        """

        if memo[i][mask] is not None:
            return memo[i][mask]

        """
        Checking memo matrix if we have found memo[i][mask] earlier
        """

        res_distance = float("inf")
        res_path = []

        for j in range(1, n + 1):
            if (mask & (1 << j)) != 0 and j != 1 and j != i:
                dist, path = func(j, mask & (~(1 << i)))
                if dist + matrix_vals[j][i] < res_distance:
                    res_distance = dist + matrix_vals[j][i]
                    res_path = path + [i]

        """
        A for loop, which performs recursive call to find value for current route
        """

        memo[i][mask] = res_distance, res_path  # memoization
        return res_distance, res_path


    names = list(matrix_vals.columns)



    matrix_vals = [list(arr) for arr in matrix_vals.to_numpy()]

    n = len(matrix_vals)

    for i in range(n):
        matrix_vals[i] = [0] + matrix_vals[i]

    matrix_vals = [[0] * (n + 1)] + matrix_vals

    """
    Adding additional zeros for the sake of easier implementation and correct behaviour of algorithm
    """

    memo = [[None] * (1 << (n + 1)) for _ in range(n + 1)]

    """
    Creating memo matrix of size (n+1)^2 to add memoization into algorithm
    """

    ans_distance, ans_path = float("inf"), []

    """
    ans_distance and ans_path variables to keep track of minimum value and route of the minimum value respectively
    """

    for i in range(1, n + 1):
        distance, path = func(i, (1 << (n + 1)) - 1)
        if distance + matrix_vals[i][1] < ans_distance:
            ans_distance = distance + matrix_vals[i][1]
            ans_path = path + [1]

    """
    Driver loop for finding optimal value and route
    """

    return ' '.join([str(names[i-1]) for i in ans_path]), ans_distance


if __name__ == "__main__":
    import pandas as pd

    l = pd.DataFrame([[0, 10, 15, 20], [10, 0, 25, 30], [15, 25, 0, 35], [20, 30, 35, 0]])
    path, distance = dynamic_solution(l)
    print("Optimal distance:", distance)
    print("Optimal path:", path)

