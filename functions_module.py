import re
import math
import quiz_data

quiz = quiz_data.quiz


#FUNCTION: GREET
def welcome_msg(name):
    print(f"Welcome to the Harry Potter Trivia Quiz app {name}! Ready to find out if you've got what it takes?\n...")


#FUCNTION: PROMPT AND RETURN USER ANSWER
def input_answer():
    user_ans = input("Enter your answer here: ")
    return user_ans

#FUNCTION: PRINT ANSWERS WITH NUMBERS
def print_answers(answers):
    ans_num = 1
    for answer in answers.keys():
        print(f"{ans_num}. {answer}")
        ans_num += 1


#FUNCTION: VALIDATE AND ERROR CHECK USER ANSWER
def validate_input(user_answer):
        try:
            # variable containing anything but char a-z(upper/lower) or \s white space                 
            regex = r"[^a-zA-Z/\s/0-9]"
            # return match obj if any regex chars found in  user_answer - bool(true). if only alpha , \s , digit then bool(false)
            match = bool(re.search(regex, user_answer))
            # if true raise error
            if match:
                raise ValueError(f"Error occured due to invalid character type")
            # if false return validated user answer      
            else: 
                return user_answer
        except Exception as e:
            print(f"{e} occured")
        # finally:
        #     print("validation complete")


# FUNCTION: CHECK FOR MATCH USER ANSWER/MULTICHOICE ANSWERS > IF MATCH CHECK FOR CORRECT/INCORRECT, RETURN BOOLEAN > IF NO MATCH AFTER FULL ITERATION PRINT  
def check_answer(user_answer, q_number):
    #iterate through multichoice_answers and value (correct/incorrect)
    for k, v in list(quiz.values())[q_number].items():

        # check if user_answer matches multichoice_answer
        if user_answer.lower() == k.lower():
            # if match > Correct
            if v == "Correct":
                # print(f"Answer is {v}")
                return True
            
            # if match > Incorrect
            else:           
                # print(f"Answer is {v}")
                return False
            
    # if no match after full iteration and no return, then None returned

 
# FUNCTION: MATCH SCORE, PRINT OUTCOME BASED ON SCORE
def display_score(score, total_q_num):

    match score:
        case score if score <= (math.floor(total_q_num * 0.33)):
            print(f"Score being calculated\n...\nYour final score is\n{score} out of {total_q_num}\nBetter luck next time!")

        case score if score <= (math.floor(total_q_num * 0.67)):
            print(f"Score being calculated\n...\nYour final score is\n{score} out of {total_q_num}\nYou might need a little more time at Hogwarts to brush up!")

        case score if score < total_q_num:
            print(f"Score being calculated\n...\nYour final score is\n{score} out of {total_q_num}\nNice one, you must be a Ravenclaw!")

        case score if score == total_q_num:
            print(f"Score being calculated\n...\nYour final score is\n{score} out of {total_q_num}\nPerfect Score!")


# FUNCTION: USER INPUT TO PLAY AGAIN
def play_again():
    play_answer = input("Would you like to play again? Y/N: ")
    if play_answer.lower() == "y" or play_answer == "yes":
        return True
    else:
        return False