class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for card in sorted(counts):
            need = counts[card]
            if need == 0:
                continue

            for nextCard in range(card, card + groupSize):
                if counts[nextCard] < need:
                    return False
                counts[nextCard] -= need

        return True


