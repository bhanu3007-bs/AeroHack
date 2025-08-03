import copy
from collections import deque

# Cube representation
def create_solved_cube():
    return {
        'U': [['W'] * 3 for _ in range(3)],
        'D': [['Y'] * 3 for _ in range(3)],
        'F': [['G'] * 3 for _ in range(3)],
        'B': [['B'] * 3 for _ in range(3)],
        'L': [['O'] * 3 for _ in range(3)],
        'R': [['R'] * 3 for _ in range(3)],
    }

def rotate_face(face, clockwise=True):
    return list(zip(*face[::-1])) if clockwise else list(zip(*face))[::-1]

def apply_move(cube, move):
    # Sample: only U and U' implemented for demo
    cube = copy.deepcopy(cube)
    clockwise = not move.endswith("'")
    face = move[0]

    if face == 'U':
        cube['U'] = rotate_face(cube['U'], clockwise)
        f, r, b, l = cube['F'][0], cube['R'][0], cube['B'][0], cube['L'][0]
        if clockwise:
            cube['F'][0], cube['R'][0], cube['B'][0], cube['L'][0] = l, f, r, b
        else:
            cube['F'][0], cube['R'][0], cube['B'][0], cube['L'][0] = r, b, l, f
    # Add other moves: D, R, L, F, B similarly
    return cube

def is_solved(cube):
    # Check if all stickers on each face are the same
    for face in cube.values():
        color = face[0][0]
        for row in face:
            for sticker in row:
                if sticker != color:
                    return False
    return True

# BFS Solver
def solve_cube(scrambled_cube):
    visited = set()
    queue = deque([(scrambled_cube, [])])
    moves = ['U', "U'"]  # Extend to all moves

    while queue:
        state, path = queue.popleft()
        state_key = str(state)

        if state_key in visited:
            continue
        visited.add(state_key)

        if is_solved(state):
            return path

        for move in moves:
            new_state = apply_move(state, move)
            queue.append((new_state, path + [move]))

    return None


# Main block to demonstrate solution output
if __name__ == "__main__":
    cube = create_solved_cube()
    # Scramble with ['U']
    scramble_moves = ['U']
    scrambled_cube = cube
    for move in scramble_moves:
        scrambled_cube = apply_move(scrambled_cube, move)
    solution = solve_cube(scrambled_cube)
    print("Solution:", solution)