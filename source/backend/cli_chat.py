from source.ui.app import process_message

def main():
    """Run chatbot in CLI"""
    user = input("Username: ")
    while True:
        message = input("\nYou: ")
        if message.lower() in {"exit", "quit"}:
            break
        response = process_message(user, message)
        print("\n\nAI:", response)

if __name__ == "__main__":
    main()
