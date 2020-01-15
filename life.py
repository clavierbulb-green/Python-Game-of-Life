from typing import List, Generator, Tuple


def game_of_life(seed: List[int],
                 width: int) -> Generator[List[int], None, None]:
    ''' A generator function that takes a flat representation of a board
    of squares as a seed and a board width and yields the result of an
    additional round of Conway's Game of Life.'''

    NEIGHBOR_COORDS: List[Tuple[int, int]] = [(-1, -1), (0, -1), (1, -1),
                                              (-1, 0),           (1, 0),
                                              (-1, 1),  (0, 1),  (1, 1)]

    def play_round(state: List[int]) -> List[int]:
        def count_live_neighbors(i: int) -> int:
            x: int = i % width
            y: int = i // width
            num_live_neighbors: int = 0

            for (dx, dy) in NEIGHBOR_COORDS:
                neighbor_x: int = (x + dx)
                neighbor_y: int = (y + dy)

                if neighbor_x not in range(width) or \
                        neighbor_y not in range(len(state) // width):
                    continue

                neighbor_index: int = neighbor_x + (neighbor_y * width)
                if state[neighbor_index]:
                    num_live_neighbors += 1

            return num_live_neighbors

        next: List[int] = []
        for (i, sq) in enumerate(state):
            num_live_neighbors: int = count_live_neighbors(i)
            # a square with 3 live neighbors stays alive/becomes alive
            if num_live_neighbors == 3:
                next.append(1)
            # a square with 2 live neighbors maintains its state
            elif num_live_neighbors == 2:
                next.append(sq)
            # else a cell dies/stays dead
            else:
                next.append(0)

        return next

    current: List[int] = seed
    while True:
        yield current
        next: List[int] = play_round(current)
        current = next
