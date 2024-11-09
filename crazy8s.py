"""
Author TJ Stoll

Console based game of crazy 8s

November 7, 2024
"""

import random

# Game Objects
playDeck = []
drawDeck = []
playerHand = []
opponentHand = []
playCard = ""

# Build the main deck
cardValues = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
cardSuits = ['s', 'c', 'h', 'd']
deck = [value + suit for value in cardValues for suit in cardSuits]


# Operations ==================================================================
def shuffle(cards: list):
    """
    Returns shuffled cards
    """
    cardsLength = len(cards)
    shuffledIndices = random.sample(range(0, cardsLength), cardsLength)
    shuffledCards = [cards[i] for i in shuffledIndices]
    
    return shuffledCards


def deal(hand: list, cards: list, quantity: int):
    """
    Returns the hand with more cards and cards with less cards
    """
    # add cards to hand
    hand.extend(cards[:quantity])
    # remove cards from cards
    updatedCards = cards[quantity:]
    
    return hand, updatedCards


def playCard(playCard: str, hand: list, playDeck: list):
    """
    """
    # add play card to playDeck
    playDeck.append(playCard)
    # remove playcard from hand
    hand.remove(playCard)
    
    return hand, playDeck

# Display =====================================================================
def displayGame():
    """
    """
    print('Opp: ', opponentHand) # DELETE THIS!!
    print(playDeck[-1], len(drawDeck))
    print('You: ', playerHand)
    
if __name__ == "__main__":
    drawDeck = shuffle(deck)
    opponentHand, drawDeck = deal(opponentHand, drawDeck, 8)
    playerHand, drawDeck = deal(playerHand, drawDeck, 8)
    playDeck, drawDeck = deal(playDeck, drawDeck, 1)
    displayGame()
    