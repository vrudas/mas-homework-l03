import uuid

from agent import agent


def main():
    print("Research Agent (type 'exit' to quit)")
    print("-" * 40)

    # Create a unique thread ID for this conversation session
    thread_id = str(uuid.uuid4())

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        for chunk in agent.stream(
                {"messages": [("user", user_input)]},
                config={"configurable": {"thread_id": thread_id}}
        ):
            print(chunk)


if __name__ == "__main__":
    main()
