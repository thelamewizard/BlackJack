# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:16:13 2019

@author: Babzy
"""
from random import shuffle
import pygame
pygame.font.init()

# Pygame template - skeleton for a new pygame project

cardpngs={'CLUB':{'ACE':pygame.image.load('pcp\\CLUB\\1.png'),2:pygame.image.load('pcp\\CLUB\\2.png'),3:pygame.image.load('pcp\\CLUB\\3.png'),4:pygame.image.load('pcp\\CLUB\\4.png'),5:pygame.image.load('pcp\\CLUB\\5.png'),6:pygame.image.load('pcp\\CLUB\\6.png'),7:pygame.image.load('pcp\\CLUB\\7.png'),8:pygame.image.load('pcp\\CLUB\\8.png'),9:pygame.image.load('pcp\\CLUB\\9.png'),10:pygame.image.load('pcp\\CLUB\\10.png'),'JACK':pygame.image.load('pcp\\CLUB\\J.png'),'QUEEN':pygame.image.load('pcp\\CLUB\\Q.png'),'KING':pygame.image.load('pcp\\CLUB\\K.png')},'DIAMOND':{'ACE':pygame.image.load('pcp\\DIAMOND\\1.png'),2:pygame.image.load('pcp\\DIAMOND\\2.png'),3:pygame.image.load('pcp\\DIAMOND\\3.png'),4:pygame.image.load('pcp\\DIAMOND\\4.png'),5:pygame.image.load('pcp\\DIAMOND\\5.png'),6:pygame.image.load('pcp\\DIAMOND\\6.png'),7:pygame.image.load('pcp\\DIAMOND\\7.png'),8:pygame.image.load('pcp\\DIAMOND\\8.png'),9:pygame.image.load('pcp\\DIAMOND\\9.png'),10:pygame.image.load('pcp\\DIAMOND\\10.png'),'JACK':pygame.image.load('pcp\\DIAMOND\\J.png'),'QUEEN':pygame.image.load('pcp\\DIAMOND\\Q.png'),'KING':pygame.image.load('pcp\\DIAMOND\\K.png')},'HEART':{'ACE':pygame.image.load('pcp\\HEART\\1.png'),2:pygame.image.load('pcp\\HEART\\2.png'),3:pygame.image.load('pcp\\HEART\\3.png'),4:pygame.image.load('pcp\\HEART\\4.png'),5:pygame.image.load('pcp\\HEART\\5.png'),6:pygame.image.load('pcp\\HEART\\6.png'),7:pygame.image.load('pcp\\HEART\\7.png'),8:pygame.image.load('pcp\\HEART\\8.png'),9:pygame.image.load('pcp\\HEART\\9.png'),10:pygame.image.load('pcp\\HEART\\10.png'),'JACK':pygame.image.load('pcp\\HEART\\J.png'),'QUEEN':pygame.image.load('pcp\\HEART\\Q.png'),'KING':pygame.image.load('pcp\\HEART\\K.png')},'SPADE':{'ACE':pygame.image.load('pcp\\SPADE\\1.png'),2:pygame.image.load('pcp\\SPADE\\2.png'),3:pygame.image.load('pcp\\SPADE\\3.png'),4:pygame.image.load('pcp\\SPADE\\4.png'),5:pygame.image.load('pcp\\SPADE\\5.png'),6:pygame.image.load('pcp\\SPADE\\6.png'),7:pygame.image.load('pcp\\SPADE\\7.png'),8:pygame.image.load('pcp\\SPADE\\8.png'),9:pygame.image.load('pcp\\SPADE\\9.png'),10:pygame.image.load('pcp\\SPADE\\10.png'),'JACK':pygame.image.load('pcp\\SPADE\\J.png'),'QUEEN':pygame.image.load('pcp\\SPADE\\Q.png'),'KING':pygame.image.load('pcp\\SPADE\\K.png')}}

WIDTH = 800
HEIGHT = 600
FPS = 30



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
back_ground = pygame.image.load('tablesmall.png')
gameDisplay = screen
pygame.display.set_caption('BlackJack')
gameDisplay.blit(back_ground,(0,0))
clock = pygame.time.Clock()
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
ORANGE = (255, 154, 0)
ORANGE2 = (155,100,0)
# Text backgound colours for money, and hand totals!
RED2 = (237,28,36)
GREEN2 = (0, 146, 1)
GREEN3 = (1,111,0)
GREEN4 = (0,134,0)
GREEN5 = (0,123,0)

buttonpressed = 0
def button(x,y,w,h,inactive_color,active_color,msg='',font_size=15,action=None):
    global buttonpressed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color,(x,y,w,h))
        if action != None:
            if click[0] == 1:
                if buttonpressed == 0:
                    buttonpressed = 1
                    action()
            if click[0] == 0:
                buttonpressed = 0
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color,(x,y,w,h))

    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    smallText = pygame.font.Font("freesansbold.ttf",font_size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def betbutton(x,y,d,inactive_color,active_color,msg='',font_size=15,action=None):
    global buttonpressed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+d > mouse[0] > x-d and y+d > mouse[1] > y-d:
        pygame.draw.circle(gameDisplay, active_color,(x,y),d)
        if action != None:
            if click[0] == 1:
                if buttonpressed == 0:
                    buttonpressed = 1
                    action()
            if click[0] == 0:
                buttonpressed = 0
            
    else:
        pygame.draw.circle(gameDisplay, inactive_color,(x,y),d)

    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    smallText = pygame.font.Font("freesansbold.ttf",font_size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = (x), (y )
    gameDisplay.blit(textSurf, textRect)
        
    

def message_display(text,x,y,font,color=BLACK):
    def text_objects(text, font):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    largeText = pygame.font.Font('freesansbold.ttf',font)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center =((x),(y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.flip()

## was pre viousely
##    pygame.display.update(TextRect[0]-100,TextRect[1]-100,TextRect[2]+150,TextRect[3]+150)
class bjcard:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        if type(self.rank) == int:
            self.value = rank
        elif self.rank == 'ACE':
            self.value = 11
        else:
            self.value = 10
    def show(self):
        print('{} of {}'.format(self.rank, self.suit))
 
    def showval(self):
        self.show()
        print('card value is: ', self.value)

# =============================================================================
#  using the bjcard class, creates s Blackjack shoe,
# made of up to 1 to 7 decks of 52 cards based on user choice.
# =============================================================================

class bjdeck():

    def __init__(self):
        ranks = [i for i in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['SPADE', 'HEART','DIAMOND','CLUB']

        numberofdecks = self.how_many_decks()
        self.cards = []
        for h in range(numberofdecks):
            for i in suits:
                for j in ranks:
                    self.cards.append(bjcard(i,j))
        self.shuffle()
    def show(self):
        for card in self.cards:
            card.showval()

    def __len__(self):
        return len(self.cards)
    def shuffle(self):
        shuffle(self.cards)
    def reshuffle(self):
        gameDisplay.blit(back_ground,(0,0))
        pygame.display.flip()
        print('Reshuffling the deck!')
        ##this?:
        self.__init__()
        ##or this?:
        #self.__init__(int(num_of_decks))
    def deck1(self):
        self.tempnum =1
    def deck2(self):
        self.tempnum =2
    def deck3(self):
        self.tempnum =3
    def deck4(self):
        self.tempnum =4
    def deck5(self):
        self.tempnum =5
    def deck6(self):
        self.tempnum =6
    def how_many_decks(self):
        gameDisplay.blit(back_ground,(0,0))
        pygame.display.flip()
        self.tempnum = 0

            
        while not 0 < self.tempnum < 7:
            message_display(str('please select how many decks you would like to play with.'),400,110,20)

            for event in pygame.event.get():
                button(770,0,30,30,ORANGE,RED,'Exit',15,pygame.quit)
                button(185,125,50,40,BLUE,(0, 245, 255),'1',15,self.deck1)
                button(260,125,50,40,BLUE,(0, 245, 255),'2',15,self.deck2)
                button(335,125,50,40,BLUE,(0, 245, 255),'3',15,self.deck3)
                button(410,125,50,40,BLUE,(0, 245, 255),'4',15,self.deck4)
                button(485,125,50,40,BLUE,(0, 245, 255),'5',15,self.deck5)
                button(560,125,50,40,BLUE,(0, 245, 255),'6',15,self.deck6)

        gameDisplay.blit(back_ground,(0,0))

        return self.tempnum
# deals a hand using the cards in the deck and assigns bet amount. 
# also allows hand to be played and calculates the blackjack score.                    
            
class hand:
    def __init__(self,playername,bet,name=None):
        self.owner = playername
        self.bet = bet
        self.bust = False
        self.stood = False
        self.has_black_jack = False
        print('your cards are:')
        self.contents = []
        global bjdd
        if len(bjdd) < 20:
            bjdd.reshuffle()
        self.deal(2)
        if self.total==21:
            self.has_black_jack = True
    def deal(self,x):
        '''
        x is number of cards to be dealt!
        '''      
        if len(bjdd) < x:
            bjdd.reshuffle()

        for j in range (x):
            self.contents.append(bjdd.cards.pop(0))
            self.calctotalscore()
            self.total = sum(i.value for i in self.contents)
        self.show()
    def show(self):
        for card in self.contents:
            card.showval()

        print ('your hand total is: ' + str(sum(i.value for i in self.contents)))
    
    def calctotalscore(self):
        listofaces=[]
        for i in self.contents:
                if i.value == 11:
                    listofaces.append(self.contents.index(i))
        for ace in listofaces:
            if 32 > sum(i.value for i in self.contents) > 21:
                self.contents[ace].value = 1
    
    def totalscore(self): 
        self.calctotalscore()
        return sum(i.value for i in self.contents) 
    def hit(self):
        self.hitorstand = 'h'         
    def stand(self):
        self.hitorstand = 's'
    def double(self):
        self.hitorstand = 'd'
    def makedecision(self):
        global dealer
        self.hitorstand = ''
        self.display_hand()
        button(210,475,30,30,(188,143,99),(151,108,66),'+',)
        button(210,522,30,30,(145,23,112),(223,55,177),'-')
        button(250,498,40,40,ORANGE,ORANGE2,'Play')


        while self.hitorstand not in ('s','h','d'):
#            if self.contents[0].value == self.contents[1].value:
#                pass  
            if  self.totalscore() <12:
                button(300,400,50,40,RED,(255, 0, 175),'Double',15,self.double)
                pygame.display.update() 
                    
            button(300,300,50,40,BLUE,(0, 245, 255),'Hit',15,self.hit)
            button(300,350,50,40,RED,(255, 0, 175),'Stand',15,self.stand)
            button(770,0,30,30,ORANGE,RED,'Exit',15,pygame.quit)
            button(375,255,40,31,GREEN2,GREEN2,str(self.totalscore()),30)
              

            for event in pygame.event.get():
                pygame.display.update() 




        return self.hitorstand
                
    def display_hand(self):
        cardx = 362.5
        cardy=300

        for i in self.contents:
        
            gameDisplay.blit((cardpngs[i.suit][i.rank]),(cardx,cardy))
            pygame.display.update()            
            cardy+=30

    def playhand(self):

        self.display_hand()
        if self.totalscore() == 21:
            return 'well done! you got BlackJack!'
        while self.totalscore() < 21 and not (self.stood or self.bust):
            decision = self.makedecision()
            if decision =='h' :
                self.deal(1)
                self.display_hand()
                
                if self.totalscore() == 21:
                    self.display_hand()
                    print('well done! you hit 21!')
                    self.stood = True
                elif self.totalscore() > 21:
                    self.display_hand()
                    self.bust=True
                    
            elif decision == 's':
                self.display_hand()
                self.stood = True
            elif decision == 'd': 
                if self.owner.bankroll >= self.bet:
                    self.owner.bankroll-=self.bet
                    button(-20,570,200,31,RED2,RED2,str(self.owner.bankroll),30)
                    self.deal(1)
                    self.display_hand()
                    self.stood =True

        print ('your final hand score is: ' + str(self.totalscore())+ ' good luck!')
    def newhand(self,x):
        self.__init__(x)  

class dealerhand():
    
    def __init__(self):

        self.has_black_jack = False
        self.bust = False
        self.name = 'Dealer'
        self.contents = []
        self.deal(2)
        self.display_first_card()
        print('\n')
    def calctotalscore(self):
        listofaces=[]
        for i in self.contents:
                if i.value == 11:
                    listofaces.append(self.contents.index(i))
        for ace in listofaces:
            if 32 > sum(i.value for i in self.contents) > 21:
                self.contents[ace].value = 1
    
    def totalscore(self): 
        self.calctotalscore()
        return sum(i.value for i in self.contents) 
    def deal(self,x):
        for j in range (x):
            self.contents.append(bjdd.cards.pop(0)) 
            self.calctotalscore()
            self.total = sum(i.value for i in self.contents) 
    def show_one_card(self):
        self.contents[0].showval()
    
    def show(self):
        for card in self.contents:
            card.showval()

        print ("Dealer's total is: " + str(sum(i.value for i in self.contents)))
    def display_hand(self):
        cardx = 300
        cardy=100
        for i in self.contents:
        
            gameDisplay.blit((cardpngs[i.suit][i.rank]),(cardx,cardy))
            pygame.display.update(cardx,cardy,cardy+50,cardx+100)            
            cardx+=50
        button(375,70,40,31,GREEN3,None,str(self.totalscore()),30)

    def display_first_card(self):
        cardx = 300
        cardy=100

        gameDisplay.blit((cardpngs[self.contents[0].suit][self.contents[0].rank]),(cardx,cardy))
        pygame.display.update(cardx,cardy,cardy+50,cardx+100)            
        button(375,70,40,31,GREEN3,None,str(self.contents[0].value),30)

           
    def dealer_plays(self):
        self.display_hand()
        if self.total==21:
            self.has_black_jack = True
        self.show()
        while 1 < self.total<17:
            self.deal(1)
            self.display_hand()
            self.show()
        if 17 > self.total<22:
            self.display_hand()

            self.show()
            print('dealers score is: ',self.total)
        elif self.total >21:
            self.display_hand()

            self.show()
            print('Dealer Busts!')
            self.bust = True
            


## default playernames
defualtnames=['Player 0','Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8','Player 9']    
class player:
    def __init__(self,bankroll,name=None):
        if name == None:
            if len (defualtnames)>0:
                self.name = defualtnames.pop(0)
        else:
            self.name=name
        self.bankroll = bankroll
        self.change_bet_by = 0

        print('Hello',self.name, ', your starting balance is:',self.bankroll)
    def increase(self):
         if self.temp_bet <= self.bankroll - self.change_bet_by:
             self.temp_bet += self.change_bet_by
         elif self.temp_bet<self.bankroll:
             self.temp_bet = self.bankroll
    
    def decrease(self):
     if self.temp_bet >= self.change_bet_by:
         self.temp_bet -= self.change_bet_by 
     elif 50<self.bankroll - self.temp_bet >0:
         self.temp_bet = 0
    def bet50(self):
        self.change_bet_by = 50
    def bet100(self):
        self.change_bet_by = 100
    def bet250(self):
        self.change_bet_by = 250
    def bet500(self):
        self.change_bet_by = 500
    def bet1000(self):
        self.change_bet_by = 1000
    

    def make_bet(self):
        self.bet = self.temp_bet
    def isin(self):
        ##buttons
        gameDisplay.blit(back_ground,(0,0))
        self.temp_bet = 0
        self.bet = 0

        while self.bet ==0:
            betbutton(20,505,20,BLUE,(0, 245, 255),'50',15,self.bet50)
            betbutton(60,505,20,(217,82,36),(186,70,31),'100',15,self.bet100)
            betbutton(100,505,20,(39,157,177),(27, 106, 120),'250',15,self.bet250)
            betbutton(140,505,20,(96,102,89),(65, 69, 61),'500',15,self.bet500)
            betbutton(180,505,20,(235,215,73),(210,187,23),'1000',15,self.bet1000)

            button(770,0,30,30,ORANGE,RED,'Exit',15,pygame.quit)
            button(210,475,30,30,(188,143,99),(151,108,66),'+',15,self.increase)
            button(210,522,30,30,(145,23,112),(223,55,177),'-',15,self.decrease)
            button(250,498,40,40,ORANGE,ORANGE2,'Play',15,self.make_bet)

            for event in pygame.event.get():

                button(-20,570,200,31,RED2,RED2,str(self.bankroll),30)
                button(290,570,200,31,RED2,RED2,str(self.temp_bet),30)
                pygame.display.flip()


        self.bet = self.temp_bet
        self.bankroll -= self.temp_bet
        self.hand = hand(self,self.temp_bet)
        global dealer
        dealer = dealerhand()
        button(-20,570,200,31,RED2,RED2,str(self.bankroll),30)
        

        self.hand.playhand()

##to workout and show the player(s) with highest score
def gethiscorers(x):
    hiscore = max(x.values())
    hiscorers = []
    for i in x:
        if x[i] == hiscore:
            hiscorers.append(i)
    if len(hiscorers)>1:
        print('the players with the highest score are: ')
        print(str( hiscorers).strip('[').strip(']').strip("'").strip("'"))
        print('with a score of: ', hiscore)
    else:
        print('the player with the highest score is: ',hiscorers[0])
        print('with a score of: ', hiscore)


bjdd = bjdeck()

# =============================================================================
# =============================================================================
# # # 
# =============================================================================
# =============================================================================
import pygame
pygame.init()
print('Welcome To My Blackjack Game!')
print(len(bjdd))
def set_players():
    global a
    # start six hands and a dealer
    a = player(1000,'Troy')
set_players()
players_playing = [a]    
       
#print('\n')
#gethiscorers(playerscores)
def begin_game():

    print(a.name,' your account has $',a.bankroll,':')
    a.isin() 
           
    end_game()

def restart_game():
    a.bankroll = 1000
    begin_game()

def end_game():
#    button(300,300,50,40,GREEN4,GREEN4)
#    button(300,350,50,40,GREEN5,GREEN5)

    button(770,0,30,30,ORANGE,RED,'Exit',15,pygame.quit)

    a.hand.display_hand()
    dealer.display_hand()
    hand_done = False
    winnings = 0
    if a.hand.bust:
        print(a.name, 'You Lose')
        hand_done = True
        ##add more!!
    elif dealer.has_black_jack:
        if a.hand.has_black_jack or a.hand.total == 21:
            print(a.name,'dealer also has blackJack!, you draw!')
            a.bankroll += a.bet
            winnings = a.bet
            hand_done = True
            
        else:
            print('Dealer has BlackJack Bad luck',a.name)
            hand_done = True
            

    elif a.hand.has_black_jack:
        print(a.name, 'BLACKJACK! You Win!')
        a.bankroll += int(a.bet * 2.5) 
        winnings = a.bet*2.5
        hand_done = True
                
    else:
        while not hand_done:
    
            print('Now, the dealer:')
          
            dealer.dealer_plays()
            

            if a.hand.total < dealer.total<22:
                print(a.name, 'You Lose')
                hand_done = True
                break
            elif a.hand.total > dealer.total or dealer.total >21:
                print(a.name, 'You Win')
                a.bankroll += a.bet * 2
                winnings = a.bet*2
                hand_done = True
                break
            elif a.hand.total == dealer.total:
                print(a.name, 'You Draw')
                a.bankroll += a.bet
                winnings = a.bet
                hand_done = True
                break
        ##=============================##
        ###IMPOSIBLE SCENARIO CATCHER!###
        #else:
        #    print('HOW IS THA POSSIBLE?') 
        ###IMPOSIBLE SCENARIO CATCHER!###                           
        ##=============================##
    while hand_done:
        betbutton(20,505,20,BLUE,(0, 245, 255),'50')
        betbutton(60,505,20,(217,82,36),(186,70,31),'100')
        betbutton(100,505,20,(39,157,177),(27, 106, 120),'250')
        betbutton(140,505,20,(96,102,89),(65, 69, 61),'500')
        betbutton(180,505,20,(235,215,73),(210,187,23),'1000')
        
        button(375,255,40,31,GREEN2,GREEN2,str(a.hand.total),30)
        button(-20,570,200,31,RED2,RED2,str(a.bankroll),30)
        button(290,570,200,31,RED2,RED2,str(a.temp_bet),30)        
        button(632,570,200,31,RED2,RED2,str(int(winnings)),30)
        
        button(770,0,30,30,ORANGE,RED,'Exit',15,pygame.quit)
        if a.bankroll  >0:
            button(210,475,30,30,(188,143,99),(151,108,66),'+',15,begin_game)
            button(210,522,30,30,(145,23,112),(223,55,177),'-',15,begin_game)
            button(250,498,40,40,ORANGE,ORANGE2,'Play',15,begin_game)
            button(50,435,100,40,ORANGE,ORANGE2,'Play Again?',15,begin_game)


        elif a.bankroll <= 0:
            message_display('Game Over!!',100,50,25,BLUE)
            button(50,435,100,40,ORANGE,ORANGE2,'RESTART',15,restart_game)
    
        for event in pygame.event.get():
            pygame.display.update()

                

#        if True:
#            print('Thanks for playing!')
#            input('press any button to exit game!')
#            return



# Game loop
running = True
while running:
    clock.tick(FPS)
    begin_game()



