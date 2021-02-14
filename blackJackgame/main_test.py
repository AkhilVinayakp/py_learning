# blackjack game test file
from typing import Tuple
class Card:
    ''' Basic implimentation of the class '''
    def __init__(self, rank:str, suit:str) -> None:
        '''
        parameters:
        ----------
        rank:
        suit:

        '''
        self.suit = suit
        self.rank = rank
        # need
        self.hard, self.soft = self._points()
    def _points(self) -> Tuple[int,int]:
        return self.rank, self.rank
    
class AceCard(Card):
    '''
    Ace card Implimentation have rank either 1 or 11
    '''
    def _points(self) -> Tuple[int,int]:
        return 1,11


class FaceCard(Card):
    '''
    The rank of each face card is 10
    '''
    def _points(self) -> Tuple[int, int]:
        return 10, 10
        