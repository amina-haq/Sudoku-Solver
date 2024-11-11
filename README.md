# Sudoku Solver

Sudoku Solver is a Python application that solves Sudoku puzzles using a backtracking algorithm. It also includes input validation and an optional feature to visualise the solving process step-by-step, which can be helpful for debugging and understanding how the algorithm works.

## Features

- **Backtracking Algorithm**: Uses a backtracking approach to fill the Sudoku grid, backtracking when a constraint is violated.
- **Input Validation**: Checks the input puzzle for any errors or conflicts and provides helpful error messages to correct them.
- **Real-Time Visualisation**: Optional feature to visualise the puzzle-solving process, helping users understand how the algorithm works.

## Installation

To get started with the Sudoku Solver in VS Code, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/SudokuSolver.git
    cd SudokuSolver
    ```

2. **Open the Project in VS Code:**

    Launch **VS Code** and open the `SudokuSolver` directory:
    - **File** > **Open Folder...** > Select the `SudokuSolver` folder.

3. **Set Up Python Environment:**

    Ensure you have Python installed. You can check this by running:

    ```bash
    python --version
    ```

    If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/).

4. **Install Required Dependencies:**

    If your project uses libraries like `Pygame` or `Matplotlib` for visualisation, you can install them using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Solver:**

    Open the terminal in VS Code (**Terminal** > **New Terminal**) and run the main Python file:

    ```bash
    python sudoku_solver.py
    ```

## Usage

1. **Input Puzzle:**

    Enter your Sudoku puzzle in the input format (either directly or as prompted by the application).

2. **Run the Solver:**

    Run the solver using the command above. If the visualisation feature is enabled, you will see the solving process in real-time.

3. **View Results:**

    After solving, the completed puzzle will be displayed, or error messages will be shown if the puzzle input was invalid.

## Example

### Input Puzzle

```plaintext
5 3 _ | _ 7 _ | _ _ _
6 _ _ | 1 9 5 | _ _ _
_ 9 8 | _ _ _ | _ 6 _
---------------------
8 _ _ | _ 6 _ | _ _ 3
4 _ _ | 8 _ 3 | _ _ 1
7 _ _ | _ 2 _ | _ _ 6
---------------------
_ 6 _ | _ _ _ | 2 8 _
_ _ _ | 4 1 9 | _ _ 5
_ _ _ | _ 8 _ | _ 7 9
```
### Output Puzzle
```plaintext
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

### Tech Stack

_Language: Python_

_Algorithm: Backtracking_

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](https://github.com/amina-haq/CareCompanion/blob/master/CONTRIBUTING.md) for guidelines on how to get involved.
