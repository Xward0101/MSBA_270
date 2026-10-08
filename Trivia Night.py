questionnaire = [
    {
        "question":"What is the capital of Japan?",
        "answer":"Tokyo",
        "category":"Geography"
    },
    {
        "question":"What is the largest planet in our solar system?",
        "answer":"Jupiter",
        "category":"Science"
    },
    {
        "question":"Who wrote 'Romeo and Juliet'?",
        "answer":"William Shakespeare",
        "category":"Literature"
    },
    {
        "question":"What is the chemical symbol for gold?",
        "answer":"Au",
        "category":"Chemistry"
    },
    {
        "question":"In which year did the Titanic sink?",
        "answer":"1912",
        "category":"History"
    },
    {
        "question":"Which planet is known as the Red Planet?",
        "answer":"Mars",
        "category":"Science"
    },
    {
        "question":"What is the largest ocean on Earth?",
        "answer":"Pacific Ocean",
        "category":"Geography"
    },
    {
        "question":"How many sides does a hexagon have?",
        "answer":"6",
        "category":"Mathematics"
    },
    {
        "question":"Which musical instrument typically has 88 keys?",
        "answer":"Piano",
        "category":"Music"
    },
    {
        "question":"What gas do plants absorb from the atmosphere?",
        "answer":"Carbon dioxide",
        "category":"Science"
    },
    {
        "question":"Which country is traditionally credited with inventing paper?",
        "answer":"China",
        "category":"History"
    },
    {
        "question":"What is the currency of Japan?",
        "answer":"Yen",
        "category":"Geography"
    },
    {
        "question":"What is the largest mammal in the world?",
        "answer":"Blue whale",
        "category":"Nature"
    }
]

def ask_question(q):
    """Ask one question and return True if the answer is correct, otherwise False."""
    print(f"\n{q['category']}: {q['question']}")
    
    try:
        user_answer = input("Your answer: ")
    except EOFError:
        print("No input received. This answer will be marked as incorrect.")
        user_answer = ""

    if user_answer.strip() == "":
        print("A blank answer will count as incorrect.")
        return False

    if user_answer.strip().lower() == q["answer"].strip().lower(): 
        print("Correct!")
        return True
    else:
        print(f"Incorrect!! The answer was {q['answer']}.")
        return False


def main():
    """Run the trivia game and keep track of the score."""
    print("Welcome to Trivia Night!")
    print("You will be asked a series of questions. Try to answer them correctly.")
    print("\nLet's begin!")    
    score = 0
    for q in questionnaire:
        if ask_question(q):
            score += 1

    print(f"\nYou got {score} out of {len(questionnaire)} questions correct.")


main()
