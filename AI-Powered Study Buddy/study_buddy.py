def greet_student():
    print("👋 Hello! I am your Study Buddy. Ask me anything or type 'exit' to quit.")


def answer_question(question):
    question = question.lower()
    if "python" in question:
        return "Python is a versatile programming language used for many purposes."
    elif "data structures" in question:
        return "Data structures are ways to organize and store data efficiently."
    elif "algorithm" in question:
        return "An algorithm is a step-by-step procedure to solve a problem."
    else:
        return "Hmm 🤔 I don’t know that yet. Try a simpler question!"


def run_study_buddy():
    greet_student()
    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("👋 Goodbye! Keep studying!")
            break
        response = answer_question(question)
        print(f"Study Buddy: {response}")


if __name__ == "__main__":
    run_study_buddy()
