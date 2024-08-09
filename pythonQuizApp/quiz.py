# importing the get_questions function from the questions.py file
from questions import get_questions


# function that takes name as argument when user types and greets
def welcome_message(name):
    print(f"Welcome, {name}, to the Quiz!")
    print("Pick a correct options from 1-4 and test ypur knowledge.")
    print("")


# function takes a question dictionary as an argument and displays the question and choices.
def ask_question(question):
    # print question first followed by choices
    print(question["question"])
    for i, choice in enumerate(question["choices"], 1):
        # print the choices, since index starting at 0, adding +1 to start from 1 like 1.Berlin, 2.Madrid soon.
        print(f"{i + 1}. {choice}")
    
    answer = input("Your answer (1-4): ")
    while not answer.isdigit() or int(answer) not in range(1, 5):
        # If the input is invalid (not a digit or out of range 1 to 4), ask again.
        print("Invalid input. Please select a number between 1 and 4.")
        answer = input("Your answer (1-4): ")

    return int(answer) # Return the user's answer as an integer.


# function takes list of questions and user's answers, compares them and calculates score.
def calculate_score(questions, answers):
    score = 0
    for i, question in enumerate(questions):
        if answers[i] == question["correct"]:
            # If the user's answer matches the correct answer, increment the score.
            score += 1
    return score  # Return the total score.

# function displays final score and feedback
def display_results(score, total):
    print(f"\nYour final score is {score} out of {total}.")
    if score == total:
        print("Excellent! You got all the answers right!")
    elif score >= total / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time!")

# fuction for thank you message at last.
def thank_you_message():
    print("\nThank you for taking the quiz!")

# main function that will start the test
def main():
    
    # First, ask to enter name
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    
    # ask to enter if user want to play or not
    play_quiz = input("Do you want to play the quiz? (yes/no): ").strip().lower()
    
    if play_quiz == "yes":
        welcome_message(name)
        questions = get_questions() # Get question list
        answers = []
        
        # Loop through each question, ask the user, and store their answer.
        for question in questions:
            answer = ask_question(question)
            answers.append(answer)

        # calculate the score and display the results after all questions answered.
        score = calculate_score(questions, answers)
        display_results(score, len(questions))
        thank_you_message()
    else:
        # for input other than yes, exit the game 
        print("See you next time!!")

# This checks if the current file is being run directly (not imported as a module). if true calls main function
if __name__ == "__main__":
    main()
