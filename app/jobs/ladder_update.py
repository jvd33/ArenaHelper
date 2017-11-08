from api.arena_client import ArenaClient
from api.data_client import DataClient

"""
Timed job that updates the PvP ladders.

(Check how often Blizzard updates the arena ladders, and update on a similar timer!)
Every 3 days for now
"""


class LadderUpdateJob:

    # Instantiates the timer if listening, otherwise just updates
    def __init__(self, listening=False):
        if not listening:
            self.timer = None
        self.timer = None
        self.brackets = ['2v2', '3v3', 'rbg']
        self.dc = DataClient()
        self.ac = ArenaClient()

    # Updates the 2v2 ladders for a specific region
    def update_ladders(self, bracket=None):
        self.ac.db.purge_ladders()
        if bracket is not None:
            self.ac.get_pvp_ladder(bracket)
            return
        for b in self.brackets:
            self.ac.get_pvp_ladder(b)

