# 🧬 TSP Genetic Algorithm Solver

A Python implementation of a **Genetic Algorithm (GA)** to solve the **Traveling Salesman Problem (TSP)**. The algorithm evolves a population of tours over multiple generations to find the shortest possible route that visits every city exactly once and returns to the starting point.

---

## ✨ Features

- 🧬 **Genetic Algorithm** — Evolves a population over generations
- 🎯 **Multiple Selection Methods** — Roulette Wheel & Greedy Selection
- 🔀 **Multiple Crossover Methods** — Single-Point & Two-Point Crossover
- 🧪 **Multiple Mutation Methods** — Single-Point & Two-Point Mutation
- 📉 **Fitness-Based Replacement** — Least-fit individuals are replaced
- 🗺️ **Adjacency Matrix Input** — Distances between cities are defined as a matrix
- 🏆 **Best Solution Tracking** — Returns the shortest tour found

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `random`
- **Concepts:** Genetic Algorithms, Evolutionary Computation, Optimization, TSP

---

## 📂 Project Structure

- `tsp_ga.py` — Main program (genetic algorithm and TSP logic)
- `README.md` — Project documentation

---

## 🧩 Core Functions

| Function | Responsibility |
|----------|----------------|
| `generate_population()` | Creates the initial random population of tours |
| `fitness()` | Calculates the total distance of a tour |
| `roulette_wheel_selection()` | Selects parents based on fitness probability |
| `greedy_selection()` | Selects the two best individuals as parents |
| `single_point_crossover()` | Performs single-point crossover |
| `two_point_crossover()` | Performs two-point crossover |
| `single_point_mutation()` | Swaps a gene to a new position |
| `two_point_mutation()` | Swaps two genes in the chromosome |
| `replace_least_fit()` | Replaces the worst individuals with offspring |
| `genetic_algorithm()` | Main GA loop over generations |

---

## 🧠 How the Genetic Algorithm Works

1. **Initialize** a random population of tours
2. **Evaluate** each tour using the fitness function (total distance)
3. **Select** parents using greedy selection
4. **Crossover** parents to produce offspring
5. **Mutate** offspring to maintain diversity
6. **Replace** the least-fit individuals in the population
7. **Repeat** for a fixed number of generations
8. **Return** the best tour found

---

## 🗺️ Sample Distance Matrix

The program uses a 5-city adjacency matrix:

```
   0  14   4  11  18
  14   0   5   7   7
   4   5   0   9  17
  11   7   9   0   4
  18   7  17   4   0
```

Each entry `matrix[i][j]` represents the distance between city `i` and city `j`.

---

## 🚀 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/FatemehPaksima/TSP-Genetic-Algorithm.git
```

### 2. Navigate into the folder:
```bash
cd TSP-Genetic-Algorithm
```

### 3. Run the program:
```bash
python tsp_ga.py
```

---

## 📊 Sample Output

```
Best solution: [0, 2, 1, 3, 4, 0]
Best value: 32
```

- **Best solution** — The shortest tour found (starts and ends at city 0)
- **Best value** — Total distance of the tour

---

## ⚙️ Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `population_size` | 5 | Number of individuals per generation |
| `generations` | 50 | Number of evolution cycles |
| `mutation_rate` | 0.3 | Probability of mutation |

You can tweak these values in the `main()` function to experiment with different results.

---

## 📜 License

This project was developed as part of a university Artificial Intelligence course.  
Free to use for learning purposes.

---

## 👨‍💻 Author

**Fatemeh Paksima**
GitHub: [@FatemehPaksima](https://github.com/FatemehPaksima)
