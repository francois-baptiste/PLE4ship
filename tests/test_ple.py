#!/usr/bin/python


"""

This tests that all the PLE4SHIP games launch, except for doom; we
explicitly check that it isn't defined.


"""


import nose
import numpy as np
import unittest

NUM_STEPS=150

class NaiveAgent():
    def __init__(self, actions):
        self.actions = actions
    def pickAction(self, reward, obs):
        return self.actions[np.random.randint(0, len(self.actions))]


class MyTestCase(unittest.TestCase):

    def run_a_game(self,game):
        from ple4ship import PLE4SHIP
        p =  PLE4SHIP(game,display_screen=True)
        agent = NaiveAgent(p.getActionSet())
        p.init()
        reward = p.act(p.NOOP)
        for i in range(NUM_STEPS):
            obs = p.getScreenRGB()
            reward = p.act(agent.pickAction(reward,obs))

    def test_waterworld(self):
        from ple4ship.games.waterworld import WaterWorld
        game = WaterWorld()
        self.run_a_game(game)


if __name__ == "__main__":
    nose.runmodule()
