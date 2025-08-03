🧩 Rubik’s Cube Solver (3x3) – AI-Based Algorithmic Solution

Welcome to the Rubik’s Cube Solver project! This repository contains a Python-based solution that simulates and solves a standard 3x3 Rubik’s Cube using algorithmic approaches like BFS. It includes full cube modeling, move simulation, state prediction, and solver logic with potential for scalability and visualization.




📌 Features

🔲 3x3 Rubik’s Cube representation using arrays (2D lists)

🔁 Simulation of all legal cube moves (U, D, L, R, F, B, and their inverses)

🧠 Solver engine using Breadth-First Search (BFS)

🧪 Move tracking and validation of solved state

💡 Extensible architecture for adding advanced algorithms (A*, IDA*)

🎥 Visual structure (tree/graph) and planned support for GUI





🛠️ Technologies Used

Python 3

collections.deque for BFS

copy for deep state transitions

(Optional) matplotlib, pygame, or Streamlit for GUI





🚀 How It Works

Methodology:

1. Cube Representation: Modeled using a dictionary of 2D lists.


2. Move Simulation: Functions that simulate each valid cube move.


3. State Transitions: Each move generates a new cube configuration.


4. Solver: BFS algorithm finds the shortest move sequence to solve.


5. Output: Returns a list of moves leading to the solved state.



Example:

cube = create_cube()
scrambled = apply_move(cube, 'U')
solution = solve_cube(scrambled)
print("Solution:", solution)




📊 Flowchart

Cube Representation → Move Simulation → BFS Solver → Output




📈 Scalability & Bonus

Support for NxN cubes (2x2, 4x4, etc.) via modular move logic

GUI enhancement with animated solving steps

Real-cube scanning (OpenCV-based integration)

Heuristics and advanced search for optimization





✅ Output

Sample output for a basic scramble:

Input: ['U', 'F']
Output: ["F'", "U'"]




📂 Folder Structure

├── rubiks_solver.py      # Main algorithm code

├── README.md             # Project documentation




🙌 Contributors

Bhanu sri.M – Algorithm & Solver Design

AeroHack 2025
