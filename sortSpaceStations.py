import operator
import space_station
import card

class SortSpaceStations(object):
    @staticmethod
    def sort_stations(stations):
        SortSpaceStations.resetAllRankScores(stations)
        SortSpaceStations.updateRankScores(stations)
        # sort stations
        stations.sort(key=operator.attrgetter('rankScore'), reverse=True)
        return stations

    @staticmethod
    def resetAllRankScores(stations):
        for s in stations:
            s.resetRankScore()

    @staticmethod
    def updateRankScores(stations):
        for i in range(0, len(stations)):
            for j in range(i+1, len(stations)):
                SortSpaceStations.addPointToWinner(stations[i], stations[j])

    @staticmethod
    def addPointToWinner(A, B):
        AScores = A.getScores()
        BScores = B.getScores()
        a = 0
        b = 0

        for i in range(0, len(AScores)):
            if (AScores[i] > BScores[i]):
                a += 1
            elif (BScores[i] > AScores[i]):
                b += 1

        if (a > b):
            A.incrementRankScore(1)
        elif (b > a):
            B.incrementRankScore(1)
