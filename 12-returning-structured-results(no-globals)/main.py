from stats import Stats
'''
🎯 Goal

Write a program that collects validated user input, computes statistics, and returns the result from a function, instead of relying on global variables.

(TYLER: DECIDED TO CHANGE BRIEF TO CHANGE TO OBJECT-ORIENTED AS WANTED TO EXPERIMENT WITH CLASSES)
📥 Inputs

Same rules as before:
User enters text repeatedly
Input ends when the user enters: q

A valid number:
can be converted to int
is between -100 and 100 inclusive

Invalid input prints:
Invalid input

Assume at least one valid number will be entered.

📤 Outputs

After quitting, print exactly:

Count: <count>
Total: <total>
Min: <min_value>
Max: <max_value>
'''
def main():
    stats_object = Stats()
    stats_object.collect_stats()
    stats_object.print_stats()

main()



