import operator


def dynamic_solution(matrix_vals, minimize=True):
    """
    A function that calculates optimal value and route.
    :param matrix_vals: Input matrix (pd.DataFrame)
    :param minimize: Bool value that defines if we are trying to minimize or maximize result value.
    :return: Returns optimal route, keeping names of matrix and optimal value.
    """
    def func(i, mask):
        """
        A recursive helper function that helps to calculate the optimal value and route.
        :param i: Defines which vertex we are currently on.
        :param mask: Binary mask, used to display which vertices is not yet visited.
        :return: Returns optimal distance and route for current recursive lap.
        """

        """
        Base case, if there is no more vertices, returns value from our input matrix 
        and indexes of first and current vertices:
        """
        if mask == ((1 << i) | 3):
            return matrix_vals[1][i], [1, i]

        """
        Checking memo matrix if we have found memo[i][mask] earlier:
        """

        if memo[i][mask] is not None:
            return memo[i][mask]

        res_distance = float("inf") if minimize else float("-inf")
        res_path = []

        """
        A for loop, which performs recursive call to find value for current route:
        """

        for j in range(1, n + 1):
            if (mask & (1 << j)) != 0 and j != 1 and j != i:
                dist, path = func(j, mask & (~(1 << i)))
                if oprtr(dist + matrix_vals[j][i], res_distance):
                    res_distance = dist + matrix_vals[j][i]
                    res_path = path + [i]

        memo[i][mask] = res_distance, res_path  # memoization
        return res_distance, res_path

    oprtr = operator.lt if minimize else operator.gt  # Comparison operator that will be used during program execution.

    names = list(matrix_vals.columns)  # A list to save matrix names.

    matrix_vals = [list(arr) for arr in matrix_vals.to_numpy()]  # Converting pd.DataFrame to a simple 2-D list.

    n = len(matrix_vals)

    """
    Adding additional zeros for the sake of easier implementation and correct behaviour of algorithm:
    """

    for i in range(n):
        matrix_vals[i] = [0] + matrix_vals[i]

    matrix_vals = [[0] * (n + 1)] + matrix_vals

    """
    Creating memo matrix of size (n+1)^2 to add memoization into algorithm@
    """

    memo = [[None] * (1 << (n + 1)) for _ in range(n + 1)]

    """
    ans_distance and ans_path variables to keep track of an optimal value and route of the optimal value respectively:
    """

    ans_distance, ans_path = float("inf") if minimize else float("-inf"), []

    """
    Driver loop for finding optimal value and route
    """

    for i in range(1, n + 1):
        distance, path = func(i, (1 << (n + 1)) - 1)
        if oprtr(distance + matrix_vals[i][1], ans_distance):
            ans_distance = distance + matrix_vals[i][1]
            ans_path = path + [1]

    return ' '.join([str(names[i-1]) for i in ans_path]), ans_distance


if __name__ == "__main__":
    import pandas as pd

    l = pd.DataFrame([[0, 10, 15, 20], [10, 0, 25, 30], [15, 25, 0, 35], [20, 30, 35, 0]])
    path, distance = dynamic_solution(l)
    print("Optimal distance:", distance)
    print("Optimal path:", path)

