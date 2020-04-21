import collections
from random import choice
Card = collections.namedtuple('Crad',['rank','suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11) ]+ "J Q K".split() #或list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits\
                for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)#给牌valve
def spades_high(card):      #接受一个Card对象，使用Frenckdeck套牌中的内建函数计算
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
j = Card('J','spades')
print(spades_high(j))


deck = FrenchDeck()
#for card in sorted(deck, key = spades_high) #使用spades_high函数
#对牌排序
#    print(card)
#print(deck[0])
#print(spades_high(deck[0]))

suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)#给牌valve
#print(choice(deck))     #不要重复造轮子，使用自带库实现随机抽取
#print(deck[12::13])     #取出索引为12的那张牌，然后每隔13张拿一张
#for card in deck:       #因为实现了__getitem__方法所以牌可以迭代
#    print(card[0])
#print(deck[0])
#print(Card('Q','hearts') in deck)   #因为可迭代所以可以用in运算符








