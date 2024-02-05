import numpy as np
import numpy.typing as npt
from queue import Queue

import clash_royale.envs.game_engine.cards as cr


class Hand():
    def __init__(self, deck: list[type[cr.Card]]) -> None:
        self.deck = Queue(maxsize=8)
        for card in deck:
            self.deck.put(card, block=False)
        
        self.available = [self.deck.get(block=False) for i in range(4)]
        self.next = self.deck.get(block=False)

    def query(self, index: int) -> cr.Card:
        if index < 4:
            return self.available[index]
        else:
            return self.next
        
    def pop(self, index: int) -> None:
        self.deck.put(self.available[index], block=False)
        self.available[index] = self.next
        self.next = self.deck.get(block=False)

    def hand(self) -> Queue:
        return self.available

        

class Player():
    def __init__(self, deck: list[str]) -> None:
        self.elixir = 5.0

        deck = [cr.name_to_card[card_name] for card_name in deck]
        np.random.shuffle(deck)
        self.hand = Hand(deck)

    def get_pseudo_valid_hand(self) -> list[cr.Card]:
        return [card for card in self.hand.hand() if card.elixir <= self.elixir]
    
    def play_card(self, index: int) -> None:
        elixir = self.hand.query(index).elixir
        self.hand.pop(index)
        self.elixir -= elixir

        assert index < 4 and self.elixir >= 0 


class GameEngine():
    # note: mu-zero should never require a game to be copied
    def __init__(self, 
                 deck1: list[str] = ['knight' * 8], 
                 deck2: list[str] = ['knight' * 8], 
                 fps=30,
                 seed: int=0,
                 resolution: npt.ArrayLike = [128, 128],
                 dimensions: npt.ArrayLike = [32, 18]):
        
        np.random.seed(seed)
        self.fps = fps
        self.resolution = resolution

        self.images = []
        self.actions = []
        self.current_frame = 0

        self.player_1 = Player(deck1)
        self.player_2 = Player(deck2)

    def image(self):
        pass

    def apply(self, action: tuple(int, int, int)):
        pass

    def step(self):
        pass

    def is_terminal(self):
        pass

    def terminal_value(self):
        pass

    def legal_actions(self, to_play: int) -> np.ndarray:
        actions = np.zeros(shape=(32, 18, 5), dtype=np.float64)
        if to_play == 0:
            hand = self.player_1.get_hand()
        else:
            hand = self.player_2.get_hand()

        for card in hand:
            if card.elixir
        # action logic
        return actions


