from typing import List, Generator, Tuple


def game_of_life(seed: List[List[int]]
                 ) -> Generator[List[List[int]], None, None]:
    ''' A generator function that takes a representation of a board
    of squares as a seed and yields the result of an additional round
    of Conway's Game of Life.'''

    NEIGHBOR_COORDS: List[Tuple[int, int]] = [(-1, -1), (0, -1), (1, -1),
                                              (-1, 0),           (1, 0),
                                              (-1, 1),  (0, 1),  (1, 1)]

    def play_round(state: List[List[int]]) -> List[List[int]]:
        '''Returns a representation of the state that results from applying
        one round of the Game of Life to an input state.
        The rules of the Game are as follows:
            A square/cell with
            - 3 live neighbors stays 'alive', or becomes 'alive' if 'dead'
            - 2 live neighbors maintains its state ('dead' or 'alive')
            - any other number of live neighbors 'dies', or stays 'dead'
        '''

        def count_live_neighbors(x: int, y: int) -> int:
            '''Returns the number of live squares that are neighbors (i.e.
            adjacent horizontally, vertically, or diagonally) to a square
            defined by given x and y coordinates in the current board state.'''

            num_live_neighbors: int = 0

            for (dx, dy) in NEIGHBOR_COORDS:
                neighbor_x: int = (x + dx)
                neighbor_y: int = (y + dy)

                if neighbor_x not in range(len(state[0])) or \
                        neighbor_y not in range(len(state)):
                    continue

                if state[neighbor_y][neighbor_x]:
                    num_live_neighbors += 1

            return num_live_neighbors

        next: List[List[int]] = [[] for row in range(len(state))]
        for (y, row) in enumerate(state):
            for (x, sq) in enumerate(row):
                num_live_neighbors: int = count_live_neighbors(x, y)
                if num_live_neighbors == 3:
                    next[y].append(1)
                elif num_live_neighbors == 2:
                    next[y].append(sq)
                else:
                    next[y].append(0)
        return next

    current: List[List[int]] = seed
    while True:
        yield current
        next: List[List[int]] = play_round(current)
        current = next
