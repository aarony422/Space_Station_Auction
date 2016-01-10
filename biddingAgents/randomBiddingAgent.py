import random
import biddingAgent

class RandomBiddingAgent(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID = ID
        self.budget = budget

    def getName(self):
        return "Random Bidding Agent"

    def getColor(self):
        return "Blue"

    # def init(self, cards, ID, players, budget):
    #    pass

    def getBid(self, card, index):
        return random.randint(0, self.budget)

    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price

    def __repr__(self):
        return self.__class__.__name__
