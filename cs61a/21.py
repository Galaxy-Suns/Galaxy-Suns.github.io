import random
import readline
import sqlite3

points = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
points.update({n: n for n in range(2, 11)})

def hand_score(hand):
    """计算玩家或庄家当前所有牌的点数

    hand - 一个列表 当前手牌
    """
    total = sum([points[card] for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

db = sqlite3.connect('cards.db')
sql = db.execute
sql('DROP TABLE IF EXISTS cards;')
sql('CREATE TABLE cards(card, who);')

def deal(card, who):
    """某人抽到某牌"""
    sql('INSERT INTO cards VALUES (?, ?);', (card, who))
    db.commit()

def score(who):
    """计算某人目前的得分"""
    cards = sql("SELECT card FROM cards where who=?;", [who]).fetchall()
    cards = [c[0] for c in cards]
    return hand_score(cards)


def bust(who):
    """检查某人是否超过21点"""
    return score(who) > 21

player, dealer = "Player", "Dealer"

def play_hand(deck):
    """进行一句21点

    deck - 列表 牌堆
    """
    deal(deck.pop(), player)
    deal(deck.pop(), dealer)
    deal(deck.pop(), player)
    hidden = deck.pop()

    while 'y' in input("再抽一张？").lower():
        deal(deck.pop(), player)
        if bust(player):
            print(player, "的牌爆掉了！")
            return 

    deal(hidden, dealer)

    while score(dealer) < 17:
        deal(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, "的牌爆掉了！")
            return

    print(player, score(player), "而", dealer, score(dealer))

deck = list(points.keys()) * 4
random.shuffle(deck)
while len(deck) > 10:
    print('\n发牌中...')
    play_hand(deck)
    sql('UPDATE cards SET who="DISCARD";')

