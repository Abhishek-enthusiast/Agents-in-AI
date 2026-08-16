#1. Project Team — Task Allocation

import random
import math

tasks = [8, 7, 6, 5, 4, 3, 2, 1]
teams = 3


def calculate_cost(solution):
    workload = [0] * teams

    for task, team in zip(tasks, solution):
        workload[team] += task

    average = sum(workload) / teams

    return sum((load - average) ** 2 for load in workload)


def get_neighbor(solution):
    neighbor = solution.copy()

    task = random.randint(0, len(tasks) - 1)
    neighbor[task] = random.randint(0, teams - 1)

    return neighbor


def simulated_annealing():
    current = [
        random.randint(0, teams - 1)
        for _ in tasks
    ]

    current_cost = calculate_cost(current)
    temperature = 100

    while temperature > 0.01:

        neighbor = get_neighbor(current)
        neighbor_cost = calculate_cost(neighbor)

        difference = neighbor_cost - current_cost

        if difference < 0:
            current = neighbor
            current_cost = neighbor_cost

        else:
            probability = math.exp(-difference / temperature)

            if random.random() < probability:
                current = neighbor
                current_cost = neighbor_cost

        temperature *= 0.995

    return current


solution = simulated_annealing()

print("TASK ALLOCATION")
print("================")

print("Tasks :", tasks)
print("Teams :", solution)
print("Cost  :", calculate_cost(solution))

for team in range(teams):
    workload = sum(
        tasks[i]
        for i in range(len(tasks))
        if solution[i] == team
    )

    print("Team", team + 1, "Workload:", workload)

#------------------------------------------------------------------------

#2. Logistics Team — Delivery Route Optimization

import random
import math

cities = [
    (0, 0),
    (2, 5),
    (5, 2),
    (7, 7),
    (9, 3),
    (4, 9)
]


def calculate_distance(route):
    distance = 0

    for i in range(len(route)):
        current = cities[route[i]]
        next_city = cities[route[(i + 1) % len(route)]]

        distance += math.dist(current, next_city)

    return distance


def get_neighbor(route):
    neighbor = route.copy()

    i, j = random.sample(range(len(route)), 2)

    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

    return neighbor


def simulated_annealing():
    current = list(range(len(cities)))
    random.shuffle(current)

    current_distance = calculate_distance(current)

    temperature = 100

    while temperature > 0.01:

        neighbor = get_neighbor(current)
        neighbor_distance = calculate_distance(neighbor)

        difference = neighbor_distance - current_distance

        if difference < 0:
            current = neighbor
            current_distance = neighbor_distance

        else:
            probability = math.exp(-difference / temperature)

            if random.random() < probability:
                current = neighbor
                current_distance = neighbor_distance

        temperature *= 0.995

    return current


best_route = simulated_annealing()

print("DELIVERY ROUTE")
print("================")

print("Best Route:", best_route)
print("Distance  :", calculate_distance(best_route))

#------------------------------------------------------------------------

#3. Academic Team — Exam Scheduling

import random
import math

subjects = 6
slots = 3

conflicts = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (4, 5)
]


def calculate_cost(schedule):
    cost = 0

    for subject1, subject2 in conflicts:
        if schedule[subject1] == schedule[subject2]:
            cost += 1

    return cost


def get_neighbor(schedule):
    neighbor = schedule.copy()

    subject = random.randint(0, subjects - 1)

    neighbor[subject] = random.randint(0, slots - 1)

    return neighbor


def simulated_annealing():
    current = [
        random.randint(0, slots - 1)
        for _ in range(subjects)
    ]

    current_cost = calculate_cost(current)

    temperature = 100

    while temperature > 0.01:

        neighbor = get_neighbor(current)
        neighbor_cost = calculate_cost(neighbor)

        difference = neighbor_cost - current_cost

        if difference < 0:
            current = neighbor
            current_cost = neighbor_cost

        else:
            probability = math.exp(-difference / temperature)

            if random.random() < probability:
                current = neighbor
                current_cost = neighbor_cost

        temperature *= 0.995

    return current


schedule = simulated_annealing()

print("EXAM SCHEDULING")
print("================")

print("Schedule:", schedule)
print("Conflicts:", calculate_cost(schedule))