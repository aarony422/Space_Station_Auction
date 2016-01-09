import card

class SpaceStation:
    # name and ID correspond to the player who is building the SpaceStation
    def __init__(self, name, ID):
        slef.name = name
        self.ID = ID
        self.cards = []
        self.scores = [0,0,0,0,0]

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getCards(self):
        return self.cards

    # adds a card to the list of won cards and increases the scores of the
    # categories that appear on the card
    def addCard(self, card):
        self.cards.append(card)
        for i in range(0,5):
            self.scores[i] += card.getValue(i)

    def getScores(self):
        return self.scores

    def __repr__(self):
        return(self.name + "'s Space Station: [" +
                str(self.scores[0]) + ", " +
                str(self.scores[1]) + ", " +
                str(self.scores[2]) + ", " +
                str(self.scores[3]) + ", " +
                str(self.scores[4]) + "]")