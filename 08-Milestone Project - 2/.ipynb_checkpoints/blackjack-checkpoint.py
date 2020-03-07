import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 
          'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        #pass
    
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
        #pass
        
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        #i = 0
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
                #print(self.deck[i])
                #i = i + 1
                pass
    
    def __str__(self):
        temp_str = ""
        i = 0
        for card in self.deck:
            temp_str = temp_str + str(card) + " "
        return temp_str

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card_dealt = self.deck.pop()
        return card_dealt
        
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        if card.rank == "Ace":
            self.aces = self.aces + 1
        self.cards.append(card)
        self.value = self.value + values[card.rank]
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces >= 1:
            self.value = self.value - 10
            self.aces = self.aces - 1    

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet amount:"))
        except:
            print("You entered a non-integer. Please try again.")
        else:
            if chips.bet > chips.total:
                print("Bet amount is over your balance of {} chips".format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        while True:
            try:
                player_ans = str(input("Will you hit or stand? [hit/stand]:"))
            except:
                print("You entered an invalid command. Please try again.")
            else:
                if player_ans[0].lower() == "h":
                    hit(deck,hand)
                    for card in hand.cards:
                        print("  {}".format(card))
                    print("Your current value: {}".format(hand.value))
                    
                    if hand.value > 21:
                    
                        while True:
                            try:
                                player_ans2 = str(input("Will you want to adjust for ace? [Y/N]:"))
                            except:
                                print("You entered an invalid command. Please try again")
                            else:
                                if player_ans2[0].lower() == "y":
                                    hand.adjust_for_ace()
                                    print("Your new value: {}".format(hand.value))
                                break
                                
                    
                elif player_ans[0].lower() == "s":
                    print("Player stands. Dealer is playing.")
                    playing = False
                    break
        break

def show_some(player,dealer):
    print("Dealer's hand:\n  Unknown\n  {}".format(dealer.cards[1]))
    #print("Dealer's value: {}".format(dealer.value))
    print("Player's hand:")
    for card in player.cards:
        print("  {}".format(card))
    print("Player's value: {}".format(player.value))
    
    
def show_all(player,dealer):
    print("Dealer's hand:")
    for card in dealer.cards:
        print("  {}".format(card))
    print("Dealer's value: {}".format(dealer.value))
    print("Player's hand:")
    for card in player.cards:
        print("  {}".format(card))
    print("Player's value: {}".format(player.value))
    pass

def player_busts(player, dealer, chips):
    print("Player goes bust!")
    chips.lose_bet()
    pass

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()
    pass

def dealer_busts(player, dealer, chips):
    print("Dealer goes bust!")
    chips.win_bet()
    pass
    
def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()
    pass
    
def push(player, dealer):
    print("It is a tie")
    pass

def play():
    
    # Set up the Player's chips
    player_chips = Chips()
    
    # Print an opening statement
    print("Welcome to the game!")
    
    continue_value = True
    while continue_value:

        # Create & shuffle the deck, deal two cards to each player
        game_deck = Deck()
        dealer = Hand()
        player = Hand()
        
        game_deck.shuffle()
        player.add_card(game_deck.deal())
        dealer.add_card(game_deck.deal())
        player.add_card(game_deck.deal())
        dealer.add_card(game_deck.deal())

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        playing = True
        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(game_deck, player)

            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                player_busts(player, dealer, player_chips)
                break
            
            else:
                # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
                while dealer.value < 17:
                    hit(game_deck, dealer)
                    dealer.adjust_for_ace()

                # Show all cards
                show_all(player, dealer)
                # Run different winning scenarios
                if player.value == 21 and len(player.cards) == 2 and dealer.value != 21 and len(dealer.cards) != 2:
                    player_chips.bet = player_chips.bet * 2
                    player_wins(player, dealer, player_chips)
                elif dealer.value > 21:
                    dealer_busts(player, dealer, player_chips)
                elif player.value > dealer.value and dealer.value < 21:
                    player_wins(player, dealer, player_chips)
                elif player.value < dealer.value and dealer.value < 21:
                    dealer_wins(player, dealer, player_chips)
                elif player.value == dealer.value and dealer.value < 21:
                    push(player, dealer)
                else:
                    push(player, dealer)
                    print("Unknown scenario. This is a fail switch.")
                break
        # Inform Player of their chips total 
        print("Player current chips amount {}".format(player_chips.total))

        # Ask to play again
        while True:
            try:
                to_play_or_not = str(input("Do you want to play again? (Yes/No):"))
            except:
                print("You entered an invalid command. Please try again")
            else:
                if to_play_or_not[0].lower() == "n":
                    continue_value = False
                    break
                elif to_play_or_not[0].lower() == "y":
                    break