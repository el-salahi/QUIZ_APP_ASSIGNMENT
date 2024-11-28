import functions_module

import re

import quiz_data

quiz = quiz_data.quiz
total_q_num = len(quiz)


# display welcome
functions_module.welcome_msg("Ella")

# *Start play-through loop
while True:
    current_q_num = 1
    score = 0

    # iterate through quiz.items > FOR EACH QUESTION (KEY) & ANSWERS{} (VALUE):
    for question, answers in quiz.items():

        # print question (key) and current question number
        print(f"Question {current_q_num}: {question}")

        # iterate through answers{} (value) and print all answers (answers{} keys)
        functions_module.print_answers(answers)

        # *Start valid/match_answer loop
        while True:
            # > store user answer 
            user_answer = functions_module.input_answer()
            # > store valid user answer
            val_user_ans = functions_module.validate_input(user_answer)

            # check answer valid. 'any' if valid, 'none' if not valid
            if val_user_ans != None:
                # valid? Yes < continue to check correct answer
                check_answer = functions_module.check_answer(val_user_ans, (current_q_num - 1))

                # check answer matchs any answers.keys. 'bool' if match, 'none' if no match
                if check_answer != None:
                    # match? Yes > #! break valid/match_answer loop 
                    break
                # match? No > prompt again #* valid/match_answer loop end, back to start
                else:
                    print(f"The answer '{val_user_ans}' does not match any of the answers provided. Please try again")

            # valid? No > prompt again #* valid/match_answer loop end, back to start
            else:
                print(f"The answer '{user_answer}' is not a valid data type. Please try again")

        # check answer correct. if 'bool(True)' update score, add 1
        if check_answer:
            score += 1

        # increment current question number by 1. end of single iteration
        current_q_num += 1


    # display final score
    functions_module.display_score(score, total_q_num)


    # play again? if bool(false) No > display good bye msg  > #! break play-through loop
    if not functions_module.play_again():
        print("Thank you for playing the Harry Potter Trivia Quiz!")
        break
    #if bool(true) Yes > #* play-through loop end, back to start
    