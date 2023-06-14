from dlgo.agent.base import Agent
from dlgo.goboard_slow import GameState
from
__all__ = [

]

class RandomBot(Agent):
    def select_move(self, game_state: GameState):
        candidates = []
        for r in range(1, game_state.board.num_rows + 1):
            for c in range(1, game_state.board.num_cols + 1):
                candidate = Point