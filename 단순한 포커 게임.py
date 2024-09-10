import random
from operator import itemgetter
from collections import Counter

SUIT_TUPLE = ("Clubs", "Diamonds", "Hearts", "Spades")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
              "Queen", "King")
INIT_SCORE = 100
MAX_ROUND = 0


def createDeck():
    deck = []
    for suit in SUIT_TUPLE:
        for value, rank in enumerate(RANK_TUPLE):
            card = {
                'suit': suit,
                'rank': rank,
                'value': value + 1,
                "attr": "hidden"
            }
            deck.append(card)

    return deck


def shuffleCards(deck):
    random.shuffle(deck)
    return deck


def getCards(deck, numCards):
    cardList = deck[-numCards:]
    return cardList


def getCard(deck, num=None):
    if num is None: return deck.pop()
    return deck.pop(num)

# 카드를 정렬하는 함수
def sortCards(cards):
    cards.sort(key=itemgetter('value'), reverse=True)
    return cards

# 현재 카드 내용을 보여주는 함수
def viewCards(cards):
    for card in cards:
        print(card)

    print()

# 카드를 플레이어에게 1장씩 나눠주는 함수
def handCards(deck, playerCards, is_open=False):
    attr = "open" if is_open else "hidden"

    dealer_card = getCard(deck)
    dealer_card["attr"] = attr
    playerCards["dealer"].append(dealer_card)

    player_card = getCard(deck)
    player_card["attr"] = attr
    playerCards["player"].append(player_card)

    return playerCards


def getValues(cards):
    return list(map(lambda x: x["value"], cards))


# 5개의 카드가 모두 같은 모양일 경우
def isFlush(cards):
    cards = sortCards(cards)
    suits_length = len(set(map(lambda x: x["suit"], cards)))

    is_flush = suits_length == 1
    if is_flush: return cards[0]['value']
    return None

# 5개의 숫자가 모두 연속일 경우
def isStraight(cards):
    cards = sortCards(cards)
    values = getValues(cards)

    is_straight = True
    for i in range(len(values) - 1):
        is_equal = values[i] - 1 == values[i + 1]
        if (not is_equal): is_straight = False

    if is_straight: return values[0]
    return None

# 4개가 같은 수가 1쌍 있을 경우
def is4Cards(cards):
    cards = sortCards(cards)
    values = getValues(cards)
    common_value = Counter(values).most_common()[0]
    is_4cards = common_value[1] == 4

    if is_4cards: return common_value[0]
    return None

# 3개의 같은 수가 1쌍 있을 경우
def isTriple(cards):
    cards = sortCards(cards)
    values = getValues(cards)
    common_value = Counter(values).most_common()[0]
    is_triple = common_value[1] == 3

    if is_triple: return common_value[0]
    return None

    return None

# 2개의 같은 수가 2쌍 있을 경우
def is2Pairs(cards):
    cards = sortCards(cards)
    values = getValues(cards)
    common_values = Counter(values).most_common(2)
    is_2pairs = common_values[0][1] == 2 and common_values[0][
        1] == common_values[1][1]

    if is_2pairs: return common_values[0][1]
    return None

# 2개의 같은 수가 1쌍 있을 경우
def is1Pairs(cards):
    cards = sortCards(cards)
    values = getValues(cards)
    common_value = Counter(values).most_common(1)[0]
    is_1pairs = common_value[1] == 2

    if is_1pairs: return common_value[1]
    return None

# 위에 해당되지 않는 경우
def isHigh(cards):
    cards = sortCards(cards)
    return cards[0]["value"]


def getScore(cards):
    flush = isFlush(cards)
    if flush: return {"flush": flush}

    straight = isStraight(cards)
    if straight: return {"straight": straight}

    cards4 = is4Cards(cards)
    if cards4: return {"4cards": cards4}

    triple = isTriple(cards)
    if triple: return {"triple": triple}

    pairs2 = is2Pairs(cards)
    if pairs2: return {"2pairs": pairs2}

    pairs1 = is1Pairs(cards)
    if pairs1: return {"1pairs": pairs1}

    high = isHigh(cards)
    if high: return {"high": high}


def main():
    global INIT_SCORE
    global MAX_ROUND

    deckList = createDeck()

    while True:
        print("=" * 70)
        print(f"{' ' * 20}>>> 게임이 시작되었습니다. <<<\n")

        deckList = shuffleCards(deckList)
        playerCards = {"dealer": [], "player": []}
        MAX_ROUND += 1
        go_count = 0
        is_end = False

        for _ in range(2):
            playerCards = handCards(deckList, playerCards, True)

        print(">>> dealer 현재 카드 목록입니다. <<<")
        viewCards(playerCards["dealer"])

        print(">>> player 현재 카드 목록입니다. <<<")
        viewCards(playerCards["player"])

        for _ in range(3):
            question = int(input(">>> 계속 하시겠습니까? 1) Drop, 2) Go ===> "))
            is_continue = question == 2

            if not is_continue:
                INIT_SCORE -= ((go_count + 1) * 10)
                is_end = True

                print(f'>>> 현재 게임 횟수는 {MAX_ROUND}, 현재 점수는 {INIT_SCORE} 입니다. <<<')
                print(">>> 게임이 종료되었습니다. <<<")
                break

            playerCards = handCards(deckList, playerCards)
            go_count += 1
            print(f">>> {go_count + 2} 번째 카드를 받았습니다 <<<")

        if is_end: continue

        dealer_score = list(getScore(playerCards["dealer"]).items())[0]
        player_score = list(getScore(playerCards["player"]).items())[0]

        if dealer_score[1] < player_score[1]: INIT_SCORE += 100
        elif dealer_score[1] > player_score[1]: INIT_SCORE -= 100

        print(f"\n>>> dealer 카드 결과는 {dealer_score[0]} 입니다. <<<")
        viewCards(playerCards["dealer"])

        print(f">>> player 카드 결과는 {player_score[0]} 입니다. <<<")
        viewCards(playerCards["player"])

        print(f'>>> 현재 게임 횟수는 {MAX_ROUND}, 현재 점수는 {INIT_SCORE} 입니다. <<<')

        if INIT_SCORE <= 0:
            print(">>> 게임이 종료되었습니다. <<<")
            break

        question = int(input(">>> 게임을 계속 하시겠습니까? 1) Continue, 2) Stop ===> "))
        is_continue = question == 1
        if not is_continue:
            print(">>> 게임이 종료되었습니다. <<<")
            break


if __name__=='__main__':
    main()
