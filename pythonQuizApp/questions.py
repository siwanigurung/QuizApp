# creating separate file for questions and importing in quiz.py file.
def get_questions():
    return [
        {
            "question": "What is the capital of France?",
            "choices": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct": 2
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct": 1
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "choices": ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"],
            "correct": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "choices": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
            "correct": 2
        },
        {
            "question": "What is the chemical symbol for water?",
            "choices": ["H2O", "O2", "CO2", "NaCl"],
            "correct": 0
        }
    ]
