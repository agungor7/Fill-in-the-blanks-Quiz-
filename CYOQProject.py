blanks_to_fill=["_1_","_2_","_3_","_4_"] #blanks in each difficulty level

level_easy="Each soccer team may have _1_ players including a _2_. A player that received a _3_ card is _4_ from the game."
level_medium="_1_ is a basic soccer skill is used when the _2_ goes out of bounds on the sideline. A _3_ must be worn by players to _4_ injuries "
level_hard="_1_ is given if the attacking team gets _2_ inside the penalty box. A penalty kick is taken _3_ yards away from the _4_. "

level_easy_answers=["eleven", "goalkeeper", "red", "ejected"]     #correct answer for level_easy
level_medium_answers=["Throw in", "ball", "shin guard", "prevent"]     #correct answer for level_medium
level_hard_answers=["Penalty kick", "fouled", "twelve", "goal line"]     #correct answer for level_hard

paragraph = ""

print "This is a fun quiz about basic soccer rules. Try to fill in each blank correctly. Enjoy!"

def difficulty():
    """Behavior:
                Asks user to choose difficulty level
    Output:
            Returns the level that has been chosen and its answers
    """
    difficulty_choose=raw_input("Please select a difficulty level among easy, medium or hard: ")
    if difficulty_choose.lower()=="easy":
        #paragraph=level_easy
        print "\nLevel: Easy. Fill in what you think is the correct answer. If you need to use numbers please use in a word form. Good luck! "
        print "\nEach soccer team may have _1_ players including a _2_. A player that received a _3_ card is _4_ from the game."
        return level_easy,level_easy_answers
    if difficulty_choose.lower()=="medium":
        #paragraph=level_medium
        print "\nLevel: Medium. Fill in what you think is the correct answer. If you need to use numbers please use in a word form. Good luck!"
        print "\n_1_ is a basic soccer skill is used when the _2_ goes out of bounds on the sideline. A _3_ must be worn by players to _4_ injuries "
        return level_medium,level_medium_answers
    if difficulty_choose.lower()=="hard":
        #paragraph=level_hard
        print "\nLevel: Hard. Fill in what you think is the correct answer. If you need to use numbers please use in a word form. Good luck!"
        print "\n_1_ is given if the attacking team gets _2_ inside the penalty box. A penalty kick is taken _3_ yards away from the _4_. "
        return level_hard,level_hard_answers
    else:
        print "Please choose a valid level."
        return difficulty()



def check_answer(user_guess,answer_list,blank):
    """Inputs:
                    user_guess: User input for the blank
                    answer_list: All the correct answers
                    blank: Counter
        Behaviour:
                    Asks the question,
                    checks if the user input is correct
                    if so, prompts the correct answer
                    and goes to the next blank
                    If not, it asks the same question again
        Output:
                    It returns to itself to go to the next blank
    """
    paragraph = user_guess
    while blank<= len(answer_list):
        user_guess = raw_input("What is your guess for blank number " + str(blank) + "? ")
        if user_guess==answer_list[blank-1]:
            print "That is correct!"
            paragraph = paragraph.replace('_'+ str(blank) + '_',user_guess)
            print paragraph
            blank += 1
            return check_answer(paragraph,answer_list,blank)
        else:
            print "That is incorrect. Try again!"



def start_quiz():
    """Behaviour:
                Plays through the game
            Output:
                No return
    """
    lvl,ans =difficulty()
    check_answer(lvl,ans,1)
start_quiz()
