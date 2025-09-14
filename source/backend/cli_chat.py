from langgraph.graph import process_message

def main():
    """Run chatbot in CLI"""
    user = input("Username: ")
    while True:
        message = input("You: ")
        if message.lower() in {"exit", "quit"}:
            break
        response = process_message(user, message)
        print(response)

if __name__ == "__main__":
    main()
