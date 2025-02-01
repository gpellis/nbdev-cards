"""A simple interface for dealing with cards."""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['Card']

# %% ../nbs/00_card.ipynb 6
class Card:
    "A playing card. Created by passing in a `rank` from `ranks` and a `suit` from `suits`."
    def __init__(self, rank, suit): self.rank,self.suit = rank,suit
    def __str__(self): return f"{self.rank}{self.suit}"
    __repr__ = __str__
