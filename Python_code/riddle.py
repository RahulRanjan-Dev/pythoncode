import random

def replace_question_marks(S):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    S = list(S)

    for i in range(len(S)):
        if S[i] == "?":
            prev = S[i - 1] if i > 0 else None
            next = S[i + 1] if i < len(S) - 1 else None

            for letter in letters:
                if letter != prev and letter != next:
                    S[i] = letter
                    break
            else:
                S[i] = random.choice(letters)

    return "".join(S)
S = "*?b?c?d?e"
result = replace_question_marks(S)
print(result)