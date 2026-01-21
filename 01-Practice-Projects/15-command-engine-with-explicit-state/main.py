"""
🎯 Goal
Build a command-driven program that processes text commands and updates
state explicitly, with no hidden side effects.

The program should behave like a small, auditable CLI tool where all
state changes are visible at the call site and no function relies on
global variables.

📥 Inputs
The user repeatedly enters commands as text.

Supported commands:
- add <number>     → adds the number to the total
- remove <number>  → subtracts the number from the total
- clear            → resets the total to 0
- total            → prints the current total
- quit             → exits the program

Rules:
- <number> must be a valid integer
- Commands are case-sensitive
- Any invalid command or malformed input should be rejected

📤 Outputs
- The `total` command prints:
  Total: <current total>

- Invalid commands print:
  Invalid command

- The program runs until `quit` is entered

⚠️ Constraints
- No global state
- No hidden mutation
- No external libraries
- Use a while loop for input handling
- Use explicit return values to update state
- Prioritise clarity and auditability over cleverness

thoughts... have string_parser return a tuple, tuple[1] to int, validation check
"""

def command_parser(user_input: str) -> tuple | None:
    split_input = user_input.split()
    if len(split_input) == 2:
        if split_input[0] in ("add", "remove"):
            try:
                split_input[1] = int(split_input[1])
                return tuple(split_input)
            except ValueError:
                return None

    if len(split_input) == 1 and split_input[0] in ("clear", "total", "quit"):
        return (split_input[0],)
    else:
        return None


def apply_command(total: int, command: tuple) -> tuple[int, bool]:
    cmd = command[0]

    if cmd == "add":
        return total + command[1], False
    elif cmd == "remove":
        return total - command[1], False
    elif cmd == "clear":
        return 0, False
    elif cmd == "total":
        return total, True
    elif cmd == "quit":
        return total, False  # main will stop the loop

    return total, False

def main():
    total = 0
    user_input = input("Please enter a command: ")

    while user_input != "quit":
        command = command_parser(user_input)

        if command is None:
            print("Invalid command")
        else:
            total, should_print = apply_command(total, command)
            if should_print:
                print(f"Total: {total}")

        user_input = input("Please enter a command: ")




if __name__ == "__main__":
    main()



