#!/usr/bin/env python2
#Jesse Bacon 8/17/15
import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = { nine:'9', ten:'10', jack:'J', queen:"Q", king:"K", ace:"A" }
values = { 'five of a kind!':7, 'a straight!':6, 'four of a kind!':5, 'full house.':4, 'three of a kind':3, \
       'two pairs':2, 'one pair':1, 'a high card.':0 }


player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Poker Dice.")
    while game():
        pass
    scores()

def game():
    print("The computer will help you to roll five dice.")
    throws()
    return play_again()

def throws():
    roll_number = 5
    global dice
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dice", i+1,':',names[dice[i]]) 
    global result
    result = hand(dice)
    print( "You currently have", result )
    rerolls = swap_prompt()
    global your_hand
    your_hand = replace_dice(rerolls)
    global opponents_hand
    opponents_hand = opponent_roll()
    global hand_fd
    global shark_fd
    hand_fd = sorted( [ (key, len(list(group))) for key, group in groupby(dice) ] )
    shark_fd = sorted( [ (key, len(list(group))) for key, group in groupby(shark_dice) ] )
    return compare_hands()
             
def roll(roll_number):
    numbers = range(1,7)
    dice = range(int(roll_number))
    iterations = 0
    while iterations < roll_number:
        iterations = iterations + 1
        dice[iterations-1] = random.choice(numbers)
    return dice

def hand(dice):
    dice.sort()
    dice_hand = [ len(list(group)) for key, group in groupby(dice) ]
    dice_hand.sort(reverse=True)
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]
    
    if dice == straight1 or dice == straight2:
        return "a straight!"
    elif dice_hand[0] == 5:
        return "five of a kind!" 
    elif dice_hand[0] == 4:
        return "four of a kind!"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "full house."
        else:
            return "three of a kind"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "two pairs"
        else:
            return "one pair"
    else:
        return "a high card."
    
def play_again():
    answer = raw_input( "Would you like to play again? y/n: " )
    if answer in ( "y", "Y", "yes", "Yes", "Of Course!" ):
        return answer
    else:
        print( "Thank you very much for playing our game.  See you next time!" )

def scores():
    global player_score, computer_score
    print( "HIGH SCORES" )
    print( "Player: ", player_score )
    print( "Computer: ", computer_score )
    
def swap_prompt():
    rerolls = input( "how many dice do you want to throw again? " )
    try:
        if int(rerolls) in (0,1,2,3,4,5):
            pass
    except ValueError:
        print "Received a non numeric value"
    print( "rerolling {0} dice.".format(rerolls) )
    return int(rerolls)

def replace_dice(rerolls):
    global result
    if rerolls == 0:
        result = hand(dice)
        print( "You finish with", result )
    else:
        for i in range(rerolls):
            try:
                print("{0} dice left to swap.".format(rerolls - i))
                position = input( "Which roll position do you want to redo? (1,2,3,4,5) " )
            except ValueError:
                print( "Use the numeric position of the dice to be swapped." )
                
            dice[position - 1] = roll(1)[0]
            
        dice.sort()
        for i in range(len(dice)):
            print( "Dice",i + 1,":",names[dice[i]] )
        
        
        result = hand(dice)
        print( "You finish with", result )
        return result
    
def opponent_roll():
    print("The opponent will now roll")
    roll_number = 5
    global shark_dice
    shark_dice = roll(roll_number)
    shark_dice.sort()
    for i in range(len(shark_dice)):
        print("Dice", i+1,':',names[shark_dice[i]]) 
    global shark_result
    shark_result = hand(shark_dice)
    print( "shark has ", shark_result )
    op_fd = [ (key, len(list(group))) for key, group in groupby(shark_dice) ] 
    try:
        replacements = [ y[0] for y in op_fd if y[1] == 1 ]
    except:
        print( "Shark holds what he's got." )
        return shark_result
    for i in replacements:
        shark_dice.remove(i)
        shark_dice.append(roll(1)[0])
        shark_dice.sort()
    shark_result = hand(shark_dice)
    print( "Shark decided to trade in some cards" )
    for i in range(len(shark_dice)):
        print("Dice", i+1,':',names[shark_dice[i]]) 
    print( "shark has ", shark_result )
    return shark_result

def compare_hands():
    if values[result] > values[shark_result]:
        print( "You have won the round." )
        global player_score
        player_score += 1
        return scores()
    elif values[result] < values[shark_result]:
        print( "Shark, takes the round." )
        global computer_score
        computer_score += 1
        return scores()
    else:
        return evaluate_a_tie()
       
def evaluate_a_tie():
    global player_score
    global computer_score
    global win
    global lose
    win = 0
    lose = 0
    if values[your_hand] == 0:
        print("Both Players pull High card.")
        compare_high_card()
    elif values[your_hand] == 1:
        print( "One pair each." )
        compare_one_pair()
    elif values[your_hand] == 2:
        print( "Two pairs each." )
        compare_two_pairs()
    elif values[your_hand] == 3:
        print( "Three of a kind for both players." )
        compare_three_of_a_Kinds()
    elif values[your_hand] == 4:
        print("Two full houses.")
        compare_full_houses()
    elif values[your_hand] == 5:
        print( "You and shark drew four of a kind each." )
        compare_four_of_a_kind()
    elif values[your_hand] == 6:
        print( "Straight and narrow, go the shark or sparrow. Tied." )
        compare_straights()
    elif values[your_hand] == 7:
        print( "We got a Texas standoff.  Shark pulls 5 of a kind." )
        compare_fives()
    else:
        print( 'Would have done it "In a way."' )
    
    if win == 1:
        player_score +=1
        print("won")
    else:
        computer_score +=1
        print("lost")  
    return scores()

def compare_high_card():
    global win
    global lose
    while True:
        for i in range(5):
            if dice[i] > shark_dice[i]:
                win = 1
                print 'Your High card for the win.'
                break
            elif dice[i] < shark_dice[i]:
                lose = 1
                print 'Shark has a higher card.'
                break
            else:
                pass
        break
    return scores()

def compare_one_pair():
    global win
    global lose
    while True:
        your_pair = [ x[0] for x in hand_fd if x[1] == 2 ]
        shark_pair = [ y[0] for y in shark_fd if y[1] == 2 ]
        if your_pair > shark_pair:
            win = 1
            print("You have the higher pair.")
            return scores()
        elif shark_pair < your_pair:
            lose = 1
            print("Shark has the higher pair")
            return scores()
        else:
            global dice
            global shark_dice
            dice = [x[0] for x in hand_fd if x[1] == 1 ]
            shark_dice = [x[0] for x in shark_fd if x[1] == 1 ]
            return compare_high_card()
        
def compare_two_pairs():
    global win
    global lose
    while True:
        your_pairs = sorted([ x[0] for x in hand_fd if x[1] == 2 ], reverse=True )
        shark_pairs = sorted([ y[0] for y in shark_fd if y[1] == 2 ], reverse=True )
        if your_pairs[0] > shark_pairs[0]:
            win = 1
            print("You have the higher first pair.")
            return scores()
        elif shark_pairs[0] < your_pairs[0]:
            lose = 1
            print("Shark has the higher first pair.")
            return scores()
        elif your_pairs[0] == shark_pairs[0]:
            if your_pairs[1] > shark_pairs[1]:
                win = 1
                print("Your secondary pair is higher.")
                return scores()
            elif shark_pairs[1] < your_pairs[1]:
                lose = 1
                print("Shark has the higher secondary pair.")
                return scores()
            else:
                global dice
                global shark_dice
                dice = [x[0] for x in hand_fd if x[1] == 1 ]
                shark_dice = [x[0] for x in shark_fd if x[1] == 1 ]
                return compare_high_card()

def compare_three_of_a_Kinds():
    global win
    global lose
    while True:
        your_triples = [ x[0] for x in hand_fd if x[1] == 3 ]
        shark_triples = [ y[0] for y in shark_fd if y[1] == 3 ]
        if your_triples > shark_triples:
            win = 1
            print("You have the higher triplicate.")
            return scores()
        elif shark_triples < your_triples:
            lose = 1
            print("Shark has the higher triplicate")
            return scores()
        else:
            global dice
            global shark_dice
            dice = [x[0] for x in hand_fd if x[1] == 1 ]
            shark_dice = [x[0] for x in shark_fd if x[1] == 1 ]
            return compare_high_card()

def compare_full_houses():
    your_triples = [ x[0] for x in hand_fd if x[1] == 3 ]
    shark_triples = [ y[0] for y in shark_fd if y[1] == 3 ]
    your_pairs = sorted([ x[0] for x in hand_fd if x[1] == 2 ], reverse=True )
    shark_pairs = sorted([ y[0] for y in shark_fd if y[1] == 2 ], reverse=True )
    global win
    global lose
    while True:
        if your_triples > shark_triples:
            win = 1
            print( "You have brought the fuller house." )
            return scores()
        elif your_triples < shark_triples:
            lose = 1
            print( "Shark pulls out a fuller house." )
        elif your_triples == shark_triples:
            if your_pairs > shark_pairs:
                win = 1
                print( "Your house has a better addition." )
                return scores()
            elif your_pairs < shark_pairs:
                lose = 1
                print( "Shark has built screened porch on his full house." )
                return scores()
            else:
                print("You two make nice neighbors. Walk away, from a texas standoff.")

def compare_four_of_a_kind():
    global win
    global lose
    while True:
        your_quads = [ x[0] for x in hand_fd if x[1] == 4 ]
        shark_quads = [ y[0] for y in shark_fd if y[1] == 4 ]
        if your_quads > shark_quads:
            win = 1
            print("You have the higher quadruple draw.")
            return scores()
        elif shark_quads < your_quads:
            lose = 1
            print("Shark has the higher quadrupled draw.")
            return scores()
        else:
            global dice
            global shark_dice
            dice = [x[0] for x in hand_fd if x[1] == 1 ]
            shark_dice = [x[0] for x in shark_fd if x[1] == 1 ]
            return compare_high_card()

def compare_straights():
    global win
    global lose
    while True:
        if hand_fd > shark_fd:
            win = 1
            print("A sucker did not see your straight.")
            return scores()
        elif hand_fd < shark_fd:
            lose = 1
            print( "Shark, also had a straight." )
            return scores()
        else:
            print("Both walk away from a Texas standoff.")
        
def compare_fives():
    global win
    global lose
    while True:
        your_penta = [ x[0] for x in hand_fd if x[1] == 5 ]
        shark_penta = [ y[0] for y in shark_fd if y[1] == 5 ]
        if your_penta > shark_penta:
            win = 1
            print("You have the higher card in Texas standoff.")
            return scores()
        elif shark_penta < your_penta:
            lose = 1
            print("Shark has the higher card in a Texas standoff.")
            return scores()
        else:
            print("Something went down.")
    
if __name__ == '__main__':
    start()
