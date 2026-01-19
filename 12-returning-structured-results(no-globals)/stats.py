class Stats:

    def __init__(self):
        self.total = 0
        self.min = None
        self.max = None
        self.count = 0

    def collect_stats(self):

        # handles user input
        # validates input
        # computes stats
        # returns stats
        while True:
            user_input = input("Please enter a number: ")

            if user_input == "q":
                break

            try:
                number = int(user_input)

                if number in range(-100, 101):
                    self.total += number
                    self.count += 1

                    if self.min is None:
                        self.min = number
                        self.max = number
                    else:
                        if number < self.min:
                            self.min = number
                        if number > self.max:
                            self.max = number

                else:
                    print("Number must be between -100 and 100.")

            except ValueError:
                print("Please enter a number.")


    def print_stats(self):
        print(f"Count: {self.count}")
        print(f"Total: {self.total}")
        print(f"Min: {self.min}")
        print(f"Max: {self.max}")






