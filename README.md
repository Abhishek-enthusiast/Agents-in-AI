# 🤖 Agents-in-AI

A practical Python repository for learning and implementing **Artificial Intelligence search techniques and optimization algorithms** through small, understandable examples.

The repository currently focuses on **uninformed search** and **local search / optimization**, with accompanying PowerPoint presentations.

## 📌 Repository Overview

This project contains implementations for:

- Exploration vs. Exploitation
- Hill Climbing Search
- 8-Queens Problem using Hill Climbing
- Simulated Annealing for different team-based optimization problems
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Depth-Limited Search (DLS)
- Bidirectional Search
- Category-wise PowerPoint presentations

The repository connects **AI theory with executable Python programs**.

## 🗂️ Repository Structure

| File | Description |
|---|---|
| `CAT-3 Exploration & Exploitation.py` | Hill climbing and random-restart search on a state-space landscape |
| `CAT-3 Hill climbing for 8 Queens Problem.py` | 8-Queens optimization using hill climbing |
| `CAT-3 Simulator Annealing for diff teams.py` | Simulated annealing for practical optimization problems |
| `CAT-4 Breadth-First Search.py` | Breadth-First Search implementation |
| `CAT-4 Depth-First Search.py` | Depth-First Search implementation |
| `CAT-4 Depth-Limited Search.py` | Depth-Limited Search implementation |
| `CAT-4 Bidirectional Search.py` | Bidirectional Search implementation |
| `CATEGORY-1.pptx` | Category 1 presentation |
| `CATEGORY-2.pptx` | Category 2 presentation |
| `LICENSE` | MIT License |

The current `main` branch contains these core Python implementations and presentation files. 

## 🧠 Topics Covered

### 1. Exploration and Exploitation

Search algorithms balance two competing goals:

- **Exploration:** discover new regions of the search space.
- **Exploitation:** improve the current promising solution.

The repository demonstrates this using a numerical state-space landscape and **random-restart hill climbing**, which repeatedly starts from different states and keeps the best result found.

### 2. Hill Climbing — 8 Queens

The **8-Queens Problem** places eight queens on an 8×8 chessboard so that no two queens attack each other.

The implementation:

1. Generates neighboring board configurations.
2. Calculates queen conflicts.
3. Selects the neighbor with the lowest conflict count.
4. Stops at `0` conflicts or when no better neighbor exists.

`0` conflicts represents the desired global optimum, while a state with no better neighbor but remaining conflicts represents a local optimum.

### 3. Simulated Annealing

**Simulated Annealing** is a local-search optimization technique that can temporarily accept worse states, helping the search escape local optima.

The repository applies it to practical examples:

- **Project Team — Task Allocation:** distribute workload evenly.
- **Logistics Team — Route Optimization:** reduce delivery-route distance.
- **Academic Team — Exam Scheduling:** reduce scheduling conflicts.

The algorithm uses a temperature value and gradually moves from exploration toward exploitation.

## 🔎 Uninformed Search

Uninformed search algorithms do not use problem-specific heuristic information.

### Breadth-First Search — BFS

BFS explores nodes **level by level** using a queue.

### Depth-First Search — DFS

DFS explores one branch as deeply as possible before backtracking.

### Depth-Limited Search — DLS

DLS is DFS with a specified maximum depth, preventing the search from going beyond the chosen limit.

### Bidirectional Search

Bidirectional Search searches from both the start and goal states and attempts to connect the two searches.

## 📊 Algorithm Comparison

| Algorithm | Strategy | Main Data Structure | Typical Strength |
|---|---|---|---|
| BFS | Level-by-level | Queue | Shortest path for equal-cost edges |
| DFS | Deep-first | Stack | Simple and memory-efficient in many cases |
| DLS | DFS with depth limit | Stack / Recursion | Controls search depth |
| Bidirectional | From both ends | Two queues | Can reduce effective search depth |
| Hill Climbing | Improve current state | Neighbor evaluation | Simple optimization |
| Random-Restart Hill Climbing | Multiple hill climbs | Repeated searches | Better exploration |
| Simulated Annealing | Probabilistic local search | Temperature schedule | Escapes local optima |

## 🛠️ Requirements

The current programs use the **Python standard library**. No external packages are required.

Recommended:

- Python 3.9+
- Git
- VS Code, GitHub Codespaces, or another Python IDE

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Abhishek-enthusiast/Agents-in-AI.git
```

### Enter the project directory

```bash
cd Agents-in-AI
```

### Run an algorithm

```bash
python "CAT-4 Breadth-First Search.py"
```

## ▶️ Example Commands

### BFS

```bash
python "CAT-4 Breadth-First Search.py"
```

### DFS

```bash
python "CAT-4 Depth-First Search.py"
```

### Depth-Limited Search

```bash
python "CAT-4 Depth-Limited Search.py"
```

### Bidirectional Search

```bash
python "CAT-4 Bidirectional Search.py"
```

### 8-Queens Hill Climbing

```bash
python "CAT-3 Hill climbing for 8 Queens Problem.py"
```

### Exploration / Exploitation

```bash
python "CAT-3 Exploration & Exploitation.py"
```

### Simulated Annealing

```bash
python "CAT-3 Simulator Annealing for diff teams.py"
```

## 🎯 Learning Objectives

After completing the examples, you should be able to:

- Understand state-space search.
- Implement BFS, DFS, DLS, and Bidirectional Search.
- Explain local and global optima.
- Analyze exploration vs. exploitation.
- Implement hill climbing.
- Apply hill climbing to the 8-Queens problem.
- Understand why hill climbing can get trapped in local optima.
- Use random restarts to improve local search.
- Implement simulated annealing.
- Apply optimization to task allocation, routing, and scheduling.

## 📚 Recommended Learning Path
```
AI Search Basics
       ↓
Breadth-First Search
       ↓
Depth-First Search
       ↓
Depth-Limited Search
       ↓
Bidirectional Search
       ↓
State-Space Optimization
       ↓
Local vs Global Optimum
       ↓
Hill Climbing
       ↓
8-Queens Problem
       ↓
Exploration vs Exploitation
       ↓
Random-Restart Hill Climbing
       ↓
Simulated Annealing
       ↓
Real-World Optimization
```

## 💡 Key Concepts

**Local Optimum**  
A state that is better than its immediate neighbors but may not be the best state in the complete search space.

**Global Optimum**  
The best possible state in the complete search space.

**Exploration**  
Searching new or less-explored regions.

**Exploitation**  
Improving the current promising solution.

**Uninformed Search**  
Search that does not use additional heuristic information to estimate the distance to the goal.

## 📈 Future Improvements

Possible extensions include:

- A* Search
- Uniform-Cost Search
- Iterative Deepening Search
- Greedy Best-First Search
- Beam Search
- Genetic Algorithms
- Minimax and Alpha-Beta Pruning
- Search-tree visualization
- Interactive 8-Queens visualization
- Runtime and memory benchmarking
- Automated test cases
- A unified command-line interface

## License:
This project is released under the **MIT License**.

## Author-

**Abhishek**

GitHub: https://github.com/Abhishek-enthusiast

Repository: https://github.com/Abhishek-enthusiast/Agents-in-AI
