# Challenge Title
<!-- Description of the challenge -->
Multi-bracket Validation. Test whether the string contains both opening and closed brackets in the correct order.
## Whiteboard Process
<!-- Embedded whiteboard image -->
[stack_queue_brackets](codeChallenge13.png)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Decided to make a dictionary, and if the character in the string was inside the key values, push that into a stack. I then checked if the closing bracket was equal to the top value of the stack and if it did, pop the top value of the stack.

Time: O(n)
Space: O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->
pytest tests/code_challenges/test_stack_queue_brackets.py
python -m stack.stack_queue_brackets
