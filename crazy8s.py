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
cardSuits = [' s', ' c', ' h', ' d']
deck = [value + suit for value in cardValues for suit in cardSuits]

cardRanking = {
    'Q s': 4,
    '2': 3,
    'J': 2,
    '8': 1
    }


# Operations ==================================================================
def shuffle(cards: list):
    """
    Shuffle indices of cards.
    Returns shuffled cards.
    """
    cardsLength = len(cards)
    shuffledIndices = random.sample(range(0, cardsLength), cardsLength)
    shuffledCards = [cards[i] for i in shuffledIndices]
    
    return shuffledCards


def deal(hand: list, cards: list, quantity: int):
    """
    Deal quantity from cards and place in hand.
    Returns updated hand and updated cards.
    """
    # add cards to hand
    hand.extend(cards[:quantity])
    # remove cards from cards
    updatedCards = cards[quantity:]
    
    return hand, updatedCards


def playCard(playCard: str, hand: list, playDeck: list):
    """
    Take playCard from hand and place in playDeck.
    Return updated hand and updated playDeck.
    """
    # add play card to playDeck
    playDeck.append(playCard)
    # remove playcard from hand
    hand.remove(playCard)
    
    return hand, playDeck

def computerPlay(opponentHand: list, playDeck: list):
    """
    
    """
    topCard = playDeck[-1].split(' ')
    cardsToPlay = []
    playCard = ''
    
    # Collect all cards in hand that can be played on the topCard
    for card in opponentHand:
        if topCard[0] in card or topCard[1] in card:
            cardsToPlay.append(card)       
    
    # Decide which is the better card to play
    if len(cardsToPlay) > 1:
            pass
        


# Display =====================================================================
def displayGame():
    """
    Display current state of the game
    """
    print('\nOpp: ', opponentHand) # DELETE THIS!!
    print(playDeck[-1], '|', len(drawDeck))
    print('You: ', playerHand)
    
    
# =============================================================================
if __name__ == "__main__":
    drawDeck = shuffle(deck)
    opponentHand, drawDeck = deal(opponentHand, drawDeck, 8)
    playerHand, drawDeck = deal(playerHand, drawDeck, 8)
    playDeck, drawDeck = deal(playDeck, drawDeck, 1)
    displayGame()
    