import random
import biddingAgent

class CopycatAgent(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID = ID
        self.budget = budget
        self.lastPrice = 0

    def getName(self):
        return "Other Copycat Bidding Agent"

    def getColor(self):
        return "Magenta4"

    # def init(self, cards, ID, players, budget):
    #    pass

    def getBid(self, card, index):
        if self.lastPrice <= self.budget:
            return self.lastPrice
        return self.budget

    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price
        self.lastPrice = price
        
    def getBudget(self):
    	return self.budget

    def __repr__(self):
        return self.__class__.__name__