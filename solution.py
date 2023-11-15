import random


def random_solution(tsp):
    cities = list(range(len(tsp)))
    solution = []
    for i in range(len(tsp)):
        random_city = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_city)
        cities.remove(random_city)
    return solution


def route_length(tsp, solution):
    route_length = 0
    for i in range(len(solution)):
        route_length += tsp[solution[i - 1]][solution[i]]
    return route_length


def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours


def get_best_neighbour(tsp, neighbours):
    best_route_length = route_length(tsp, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_route_length = route_length(tsp, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length


def hill_climbing(tsp):
    current_solution = random_solution(tsp)
    current_route_length = route_length(tsp, current_solution)
    neighbours = get_neighbours(current_solution)
    best_neighbour, best_neighbour_length = get_best_neighbour(tsp, neighbours)
    print(f"This the current solution: {current_solution}")
    print(f"This is the length {current_route_length}")
    print(f"These are the neighbours \n {neighbours}")
    while best_neighbour_length < current_route_length:
        current_solution = best_neighbour
        current_route_length = best_neighbour_length
        best_neighbour, best_neighbour_length = get_best_neighbour(tsp, neighbours)
    return current_solution, current_route_length


def main():
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]
    path, cost = hill_climbing(tsp)
    print(f"Optimal path is {path}, and the heuristic value is {cost}")


if __name__ == '__main__':
    main()
