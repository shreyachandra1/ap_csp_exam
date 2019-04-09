import time, signal

def game_init():
    '''This function defines and intitializes all of the global variables vital
    to the game.'''
    global mstate_100
    global mstate_200
    global mstate_300
    global mstate_400
    global mstate_500
    
    global rstate_100
    global rstate_200
    global rstate_300
    global rstate_400
    global rstate_500
    
    global astate_100
    global astate_200
    global astate_300
    global astate_400
    global astate_500
    
    global points
    
    points = [0]
    
    mstate_100 = False
    mstate_200 = False
    mstate_300 = False
    mstate_400 = False
    mstate_500 = False
    
    rstate_100 = False
    rstate_200 = False
    rstate_300 = False
    rstate_400 = False
    rstate_500 = False
    
    astate_100 = False
    astate_200 = False
    astate_300 = False
    astate_400 = False
    astate_500 = False

def end_game():
    '''This function provides the end game sequence, which is only called when
    the signal/timer goes off. This allows the player to either restart or exit
    the game.'''
    print "Your time is up! I hope you've enjoyed playing Jeopardy :)"
    print "Your total score is " + str(points[0]) + " points. Great job!"
    end = True
    end_ret = "yes"
    while end == True:
        print "Would you like to play again? (Yes or No)"
        play_again = raw_input("")
        play_again = play_again.lower()
        if play_again == "yes":
            end = False
            end_ret = "no"
        elif play_again == "no":
            print "Goodbye!"
            end = False
        elif play_again != "yes" and play_again != "no":
            print "I cannot comprehend that."
            
    return end_ret 

def animals_nval(in_val, in_str, in_ans_1, in_ans_2):
    '''This function acts as the template for all question responses, telling 
    the player whether or not their answer was correct.'''
    print in_str
    answer = raw_input("")
    answer = answer.lower()
    if answer == in_ans_1 or answer == in_ans_2:
        print "That's correct! You just earned " + str(in_val) + " points." \
              " Keep going!"
        points[0] += in_val
    else:
        print "Incorrect. The correct answer was " + in_ans_2 + ". Don't " \
              "give up yet!"
              
def mammals_exit():
    '''This function prevents the player from answering any of the mammal 
    questions again if all 5 have been attempted already (returns directly to
    category_input).'''
    if mstate_100 == True and mstate_200 == True and mstate_300 == True and \
       mstate_400 == True and mstate_500 == True:
        return False
    else:
        return True

def mammals():
    '''This function asks the five mammal questions, each one being different 
    depending on what point value the player selects. It also catches if the 
    question has been answered already, and redirects to mammals_exit if so.'''
    global mstate_100
    global mstate_200
    global mstate_300
    global mstate_400
    global mstate_500
    question = True
    while question == True:
        print "How many points are you going for? (100, 200, 300, 400, or 500):"
        point_value = raw_input("")
            
        if point_value == "100":
            if mstate_100 == False:
                animals_nval(100, "What is the fastest land mammal?", \
                             "cheetah", "cheetahs")
                mstate_100 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = mammals_exit()

        elif point_value == "200":
            if mstate_200 == False:
                loc_str = "All mammals are (Hint: Think blood type!): "
                animals_nval(200,  loc_str, "warm blooded", "warm-blooded")
                mstate_200 = True    
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = mammals_exit()
                
        elif point_value == "300"     :
            if mstate_300 == False:
                animals_nval(300, "What do all mammals have?", "hair", "hair")
                mstate_300 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = mammals_exit()
                
        elif point_value == "400":
            if mstate_400 == False:
                animals_nval(400, "What is the only mammal that can fly?", \
                             "bat", "bats")
                mstate_400 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = mammals_exit()
                
        elif point_value == "500":
            if mstate_500 == False:
                animals_nval(500, "What mammal does not have teeth?", \
                             "ant eater", "ant eaters")
                mstate_500 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = mammals_exit()
                
        else: 
            print "It isn't possible to earn that many points. Choose a new" \
                  " option."
            question = mammals_exit()

def reptiles_exit():
    '''This function prevents the player from answering any of the reptile 
    questions again if all 5 have been attempted already (returns directly to
    category_input).'''
    if rstate_100 == True and rstate_200 == True and rstate_300 == True and \
       rstate_400 == True and rstate_500 == True:
        return False
    else:
        return True
        
def reptiles():
    '''This function asks the five reptile questions, each one being different 
    depending on what point value the player selects. It also catches if the 
    question has been answered already, and redirects to reptiles_exit if so.'''
    global rstate_100
    global rstate_200
    global rstate_300
    global rstate_400
    global rstate_500
    question = True
    while question == True:
        print "How many points are you going for? (100, 200, 300, 400, or 500):"
        point_value = raw_input("")
            
        if point_value == "100":
            if rstate_100 == False:
                animals_nval(100, "What do most reptiles hatch from?", \
                             "eggs", "eggs")
                rstate_100 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = reptiles_exit()

        elif point_value == "200":
            if rstate_200 == False:
                loc_str = "All reptiles are (Hint: Think blood type!): "
                animals_nval(200,  loc_str, "cold blooded", "cold-blooded")
                rstate_200 = True    
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = reptiles_exit()
                
        elif point_value == "300"     :
            if rstate_300 == False:
                animals_nval(300, "What are reptiles' skin made of?", \
                             "scales", "scales")
                rstate_300 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = reptiles_exit()
                
        elif point_value == "400":
            if rstate_400 == False:
                animals_nval(400, "Which reptile is legless?", "snake", \
                             "snakes")
                rstate_400 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = reptiles_exit()
                
        elif point_value == "500":
            if rstate_500 == False:
                animals_nval(500, "Which lizard is the biggest?", \
                             "komodo dragon", "komodo dragon")
                rstate_500 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = reptiles_exit()
                
        else: 
            print "It isn't possible to earn that many points. Choose a new" \
                  " option."
            question = reptiles_exit()
            
def amphibians_exit():
    '''This function prevents the player from answering any of the amphibian 
    questions again if all 5 have been attempted already (returns directly to
    category_input).'''
    if astate_100 == True and astate_200 == True and astate_300 == True and \
       astate_400 == True and astate_500 == True:
        return False
    else:
        return True  
        
def amphibians():
    '''This function asks the five amphibian questions, each being different 
    depending on what point value the player selects. It also catches if the 
    question has been answered already, and redirects to amphibians_exit if 
    so.'''
    global astate_100
    global astate_200
    global astate_300
    global astate_400
    global astate_500
    question = True
    while question == True:
        print "How many points are you going for? (100, 200, 300, 400, or 500):"
        point_value = raw_input("")
            
        if point_value == "100":
            if astate_100 == False:
                local_str = "What do amphibians have to help them breathe in" \
                          " the water?"
                animals_nval(100, local_str, "gills", "gills")
                astate_100 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = amphibians_exit()

        elif point_value == "200":
            if astate_200 == False:
                loc_str = "What do amphibians have to help them swim?"
                animals_nval(200,  loc_str, "fins", "fins")
                astate_200 = True    
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = amphibians_exit()
                
        elif point_value == "300"     :
            if astate_300 == False:
                loc_string = "All amphibians are (Hint: Think blood type!):"
                animals_nval(300, loc_string, "cold blooded", "cold-blooded")
                astate_300 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = amphibians_exit()
                
        elif point_value == "400":
            if astate_400 == False:
                animals_nval(400, "All adult amphibians are (Hint: Think" \
                             " food type!):", "carnivores", "carnivores")
                astate_400 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = amphibians_exit()
                
        elif point_value == "500":
            if astate_500 == False:
                animals_nval(500, "As they get older, what process do" \
                             " amphibians undergo?", "metamorphosis", \
                             "metamorphosis")
                astate_500 = True
                question = False
            else:
                print "You've answered this question already! Choose a new one."
                question = amphibians_exit()
                
        else: 
            print "It isn't possible to earn that many points. Choose a new" \
                  " option."
            question = amphibians_exit()
            
def category_input():
    '''This asks the player what category they would like to choose and calls 
    the related function based on their choice. There is an opportunity to exit
    the game if the player would like, and if they mistype or choose a category
    that does not exist, they are asked the question again.'''
    go = True
    while go == True:
        print "Which category would you like? (Mammals, Reptiles, Amphibians," \
              " or Exit)"
        category = raw_input("")
        category = category.lower()
        if category == "mammals":
            mammals()
        elif category == "reptiles":
            reptiles()
        elif category == "amphibians":
            amphibians()
        elif category == "exit":
            print "Goodbye! See you next time :)"
            go = False
        else:
            print "That's not an option. Please choose a valid category."

def welcome():
    '''This function provides the introduction to the game and asks the player
    whether or not they would like to play. If yes, the game initiates and if 
    not, they would exit the terminal. If they type something otherwise, they
    are asked the initiation question again.'''
    game_init()
    entrance = True
    start_questions = False
    while entrance == True:
        print "Welcome to Jeopardy, a mind-boggling game designed to test " \
              "your knowledge! Are you willing to give it a shot? (Yes or No)"
        greetings = raw_input("")
        greetings = greetings.lower()
        if greetings == "yes":
            print "Great! Today's topic is Animals. There are three different" \
                  " categories, which are: Mammals, Reptiles, and Amphibians." \
                  " Each category has 5 different questions, ranging from " \
                  "100-500 points. Your goal is to earn as many points " \
                  "as possible within 3 minutes. Your time starts now. " \
                  "Good luck!"
            entrance = False
            start_questions = True
        elif greetings == "no":
            print "That's a shame. Maybe next time."
            entrance = False
        else:
            print "I'm sorry, but I don't understand. Please try again."
            
    return start_questions

def start_game():
    '''This initializes the welcome function, and if the player would like to
    proceed, the category_input function is called, which sets the game in
    motion.'''
    wel_ret = welcome()
    if wel_ret == True:
        category_input()
        
def begin_again():
    '''This function causes the timer to initiate, and after 3 minutes, the 
    end_game() function is called, bringing an end to the game.'''
    signal.signal(signal.SIGALRM, sig_handler)
    signal.alarm(180)
    try: 
        start_game()
        signal.alarm(0)
    except:
        end_ret = end_game()
        if end_ret == "no":
            return True
        else:
            return False

def sig_handler(signum, frame):
    '''This function helps in defining the signal, yet as there is no error to
    be accounted for, a blank string is raised.'''
    raise ""

if __name__ == '__main__':
    game_on = True
    
    while game_on == True:
        game_on = begin_again()