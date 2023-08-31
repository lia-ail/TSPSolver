import operator


def nearestn_solution(distances, minimize):

    oper = operator.lt if minimize else operator.gt

    names = list(distances.columns)

    distances = [list(arr) for arr in distances.to_numpy()]
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0

    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

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

    tour.append(0)
    total_distance += distances[current_city][0]

    return ' '.join([str(names[i-1]) for i in tour]), total_distance



