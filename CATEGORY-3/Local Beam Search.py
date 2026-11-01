import math
import random


class EightQueensProblem:
    def __init__(self, state=None):
        self.state = state if state is not None else [random.randint(0, 7) for _ in range(8)]

    def evaluate(self):
        conflicts = 0
        n = len(self.state)
        for i in range(n):
            for j in range(i + 1, n):
                if self.state[i] == self.state[j] or abs(self.state[i] - self.state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_neighbors(self):
        neighbors = []
        for col in range(8):
            for row in range(8):
                if self.state[col] != row:
                    new_state = list(self.state)
                    new_state[col] = row
                    neighbors.append(EightQueensProblem(new_state))
        return neighbors


class JobSchedulingProblem:
    def __init__(self, job_times, num_processors, state=None):
        self.job_times = job_times
        self.num_processors = num_processors
        self.state = state if state is not None else [random.randint(0, num_processors - 1) for _ in range(len(job_times))]

    def evaluate(self):
        processor_loads = [0] * self.num_processors
        for job_idx, proc_id in enumerate(self.state):
            processor_loads[proc_id] += self.job_times[job_idx]
        return max(processor_loads)

    def get_neighbors(self):
        neighbors = []
        for job_idx in range(len(self.state)):
            for proc_id in range(self.num_processors):
                if self.state[job_idx] != proc_id:
                    new_state = list(self.state)
                    new_state[job_idx] = proc_id
                    neighbors.append(JobSchedulingProblem(self.job_times, self.num_processors, new_state))
        return neighbors


class TSPProblem:
    def __init__(self, distance_matrix, state=None):
        self.dist_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        if state is None:
            self.state = list(range(self.num_cities))
            random.shuffle(self.state)
        else:
            self.state = state

    def evaluate(self):
        total_dist = 0
        for i in range(self.num_cities):
            total_dist += self.dist_matrix[self.state[i]][self.state[(i + 1) % self.num_cities]]
        return total_dist

    def get_neighbors(self):
        neighbors = []
        for i in range(self.num_cities):
            for j in range(i + 1, self.num_cities):
                new_state = self.state[:i] + self.state[i:j+1][::-1] + self.state[j+1:]
                neighbors.append(TSPProblem(self.dist_matrix, new_state))
        return neighbors


class TimetableProblem:
    def __init__(self, num_courses, num_timeslots, num_rooms, clashes_matrix, state=None):
        self.num_courses = num_courses
        self.num_timeslots = num_timeslots
        self.num_rooms = num_rooms
        self.clashes = clashes_matrix
        
        if state is None:
            self.state = [(random.randint(0, num_timeslots - 1), random.randint(0, num_rooms - 1)) for _ in range(num_courses)]
        else:
            self.state = state

    def evaluate(self):
        penalty = 0
        room_time_slots = {}
        for course_idx, (t, r) in enumerate(self.state):
            if (t, r) in room_time_slots:
                penalty += 100
            else:
                room_time_slots[(t, r)] = course_idx

        for c1 in range(self.num_courses):
            for c2 in range(c1 + 1, self.num_courses):
                t1, _ = self.state[c1]
                t2, _ = self.state[c2]
                if t1 == t2 and self.clashes[c1][c2] > 0:
                    penalty += self.clashes[c1][c2] * 10
        return penalty

    def get_neighbors(self):
        neighbors = []
        for c in range(self.num_courses):
            for t in range(self.num_timeslots):
                for r in range(self.num_rooms):
                    if self.state[c] != (t, r):
                        new_state = list(self.state)
                        new_state[c] = (t, r)
                        neighbors.append(TimetableProblem(self.num_courses, self.num_timeslots, self.num_rooms, self.clashes, new_state))
        return neighbors


def local_beam_search(problem_class, problem_args, k=5, max_iterations=500):
    beams = [problem_class(*problem_args) for _ in range(k)]
    
    for _ in range(max_iterations):
        all_candidates = []
        for state in beams:
            all_candidates.extend(state.get_neighbors())
        
        beams = sorted(all_candidates, key=lambda x: x.evaluate())[:k]
        
        if beams[0].evaluate() == 0:
            break
            
    best_state = min(beams, key=lambda x: x.evaluate())
    return best_state, best_state.evaluate()


if __name__ == "__main__":
    eq_best, eq_cost = local_beam_search(EightQueensProblem, [], k=5)
    print(f"Eight Queens (Beam K=5) -> Best State: {eq_best.state} | Conflicts: {eq_cost}")

    jobs = [12, 45, 23, 78, 34, 89, 12, 65, 34, 21, 56, 90]
    num_procs = 3
    js_best, js_cost = local_beam_search(JobSchedulingProblem, [jobs, num_procs], k=4)
    print(f"Job Scheduling (Beam K=4) -> Best Makespan: {js_cost}")

    random.seed(42)
    cities = 10
    dist_matrix = [[0 if i == j else random.randint(10, 100) for j in
