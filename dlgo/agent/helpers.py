from dlgo.goboard_slow import Board
from dlgo.gotypes import Point

__all__ = [
    'is_point_an_eye'
]


def is_point_an_eye(board: Board, point, color):
    if board.get(point) is not None:
        return False
    for neighor in point.neighbors():
        if board.is_on_grid(neighor):
            neighor_color = board.get(neighor)
            if neighor_color != color:
                return False

    friendly_corners = 0
    off_board_corners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]

    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color is color:
                friendly_corners += 1
        else:
            off_board_corners += 1   
    
    if off_board_corners > 0:
        return off_board_corners + friendly_corners == 4
    return friendly_corners >= 3