import operator


def nearestn_solution(distances, minimize=True):
    """
    A function for finding approximate optimal route and optimal resulting value. Used on large data sets,
    increases performance at expense of lower accuracy.
    :param distances: Input matrix (pd.DataFrame)
    :param minimize: Bool value that defines if we are trying to minimize or maximize result value.
    :return: Returns approximate optimal route, keeping names of matrix and approximate optimal value.
    """

    oper = operator.lt if minimize else operator.gt  # Comparison operator that will be used during program execution.

    names = list(distances.columns)  # A list to save matrix names.

    distances = [list(arr) for arr in distances.to_numpy()]  # Converting pd.DataFrame to a simple 2-D list.
    num_cities = len(distances)
    visited = [False] * num_cities  # A list for keeping track of visited vertices.
    tour = []  # Variable for optimal route
    total_distance = 0  # Variable for optimal value

    """
    Defining current city as first visited:
    """

    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

    """
    Main nested loop. For each vertex finds nearest not visited vertex:
    """

    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = float("inf") if minimize else float("-inf")

        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if oper(distance, nearest_distance):
                    nearest_city = city
                    nearest_distance = distance

        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    """
    Come back to the first city:
    """

    tour.append(0)
    total_distance += distances[current_city][0]

    return ' '.join([str(names[i]) for i in tour]), total_distance



