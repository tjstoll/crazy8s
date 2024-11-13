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

# Build the main deck
cardValues = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']
cardSuits = ['s', 'c', 'h', 'd']

cardRanking = {
    'Q s': range(48,49),
    '2': range(4,8),
    'J': range(40,44),
    '8': range(28,32)
    }

# ranking card strength from least to most
cardRanking = [range(28,32),
               range(40,44),
               range(4,8),
               range(48,49)]

# Backend Mechanics ===========================================================
def calculateCardValueByIndex(ind: int):
    """
    Calculate the value of the card located at ind
    
    """
    cardValueIndex = ind//4
    cardSuitIndex = ind%4
    card = cardValues[cardValueIndex] + ' ' + cardSuits[cardSuitIndex]
    
    return card

def calculateCardIndexByValue(val: str):
    """
    Calculate the card index by the card value val
    """
    cardValue, cardSuit = val.split(' ')
    cardValueIndex = cardValues.index(cardValue)*4
    cardSuitIndex = cardSuits.index(cardSuit)
    cardIndex = cardValueIndex + cardSuitIndex
    
    return cardIndex

# Operations ==================================================================
def shuffle(cardsLength: int):
    """
    Shuffle indices of cards.
    Returns shuffled cards.
    """
    #cardsLength = len(cards)
    shuffledIndices = random.sample(range(0, cardsLength), cardsLength)
    #shuffledCards = [cards[i] for i in shuffledIndices]
    
    return shuffledIndices


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

def validatePlay(card: 'str', playDeck: list):
    """
    """
    topCardIndex = playDeck[-1]
    topCard = calculateCardValueByIndex(topCardIndex)
    
    if card != '':
        cardValue, cardSuit = card.split(' ')
        if cardValue == '8':
            return True
        elif cardValue in topCard or cardSuit in topCard:
            return True
        else:
            return False
    else:
        return True
    
def pickUpCards(qty: int, hand: list):
    """
    Add qty amount of cards to hand
    """
    for pickUp in range(0, qty):
        pickUpCard = drawDeck[0]
        drawDeck.remove(pickUpCard)
        hand.append(pickUpCard)

def play(card: str, hand: list, playDeck: list):
    """
    Plays a card
    """
    
    if card != '':
        cardIndex = calculateCardIndexByValue(card)
        
        # Remove card from hand and add to play deck
        if cardIndex in hand:
            hand.remove(cardIndex)
            playDeck.append(cardIndex)
            
    # No card has been offered to play
    # Add card from draw deck to hand and skip turn    
    else:
        pickUpCards(1, hand)

def computerPlay(opponentHand: list, playDeck: list):
    """
    Returns computers play
    """
    # Retrieve top card
    topCardIndex = playDeck[-1]
    
    # can only play a card in a certain index range (value range)
    # ie if topcard index is 0 then only playable value is index 0 - 4
    lowerValueIndexRange = 4*(topCardIndex//4)
    upperValueIndexRange = lowerValueIndexRange + 4
    validCardsByValue = range(lowerValueIndexRange, upperValueIndexRange)
    
    # can only play a card of specific suit
    # ie if topcard Index is 11 then only playable suit is 3
    # therefore every 4 cards starting from index 3 is a playable card
    suitIndex = topCardIndex%4
    validCardsBySuit = [x*4+suitIndex for x in range(0,13)]
    
    # collect list of all playable cards on the top card
    opponentPlayOptions = []
    for card in opponentHand:
        if card in validCardsByValue:
            opponentPlayOptions.append(card)
        elif card in validCardsBySuit:
            opponentPlayOptions.append(card)
        # If card is any 8
        elif card in range(28,32):
            opponentPlayOptions.append(card)
            
    # calculate which card is best to play
    # TO BE CONTINUED
    if len(opponentPlayOptions) > 1:
        #print([calculateCardValueByIndex(x) for x in opponentPlayOptions])
        return [opponentPlayOptions[-1]]
    elif len(opponentPlayOptions) == 0:
        opponentPlayOptions.append('')
        
    return opponentPlayOptions


# Display =====================================================================
def displayGame():
    """
    Display current state of the game
    """
    opponentHandDisplay = [calculateCardValueByIndex(c) for c in opponentHand]
    playerHandDisplay = [calculateCardValueByIndex(c) for c in playerHand]
    topCard = calculateCardValueByIndex(playDeck[-1])
    
    print('\nOpp: ', opponentHandDisplay) # DELETE THIS!!
    print(topCard, '|', len(drawDeck))
    print('You: ', playerHandDisplay)
 
    
# Gameloop=====================================================================
def advance(card: 'str'):
    """
    """
    playValidated = validatePlay(card, playDeck)
    if playValidated:
        play(card, playerHand, playDeck)
    
        displayGame()
    
        opponentPlay = computerPlay(opponentHand, playDeck)
    
        if opponentPlay[0] != '':
            play(calculateCardValueByIndex(opponentPlay[0]), opponentHand, playDeck)
        else:
            play(opponentPlay[0], opponentHand, playDeck)
        
        displayGame()
    else:
        topCard = calculateCardValueByIndex(playDeck[-1])
        print("Can't play {0} on {1}.. Try again!".format(card, topCard))
        displayGame()
    
    
# =============================================================================
if __name__ == "__main__":
    drawDeck = shuffle(52)
    opponentHand, drawDeck = deal(opponentHand, drawDeck, 8)
    playerHand, drawDeck = deal(playerHand, drawDeck, 8)
    playDeck, drawDeck = deal(playDeck, drawDeck, 1)
    displayGame()
    