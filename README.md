# Hill Climbing Algorithm for TSP

## Introduction

This Python script implements the Hill Climbing algorithm to solve the Traveling Salesman Problem (TSP). The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits a set of cities and returns to the starting city.

## Authors

- Kaitake Gloria
- Mawanda Dennis

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Run the script:

    ```bash
    python your_script.py
    ```

## Description

The script consists of the following functions:

- `random_solution(tsp)`: Generates a random solution for the TSP.
- `route_length(tsp, solution)`: Calculates the length of a given route.
- `get_neighbours(solution)`: Generates neighboring solutions.
- `get_best_neighbour(tsp, neighbours)`: Finds the best neighboring solution.
- `hill_climbing(tsp)`: Implements the Hill Climbing algorithm for TSP.

## Example

```python
if __name__ == '__main__':
    main()
# sales-man-problem-with-the-hill-climbing-ALG
