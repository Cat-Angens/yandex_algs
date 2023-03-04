from stack import Stack


def check_symbol(c):
    return c in ('(', ')', '[', ']', '{', '}')


def check_parenthesis_sequence(sequence: str):
    stack = Stack()
    for c in sequence:
        if not check_symbol(c):
            continue
        if c in ('(', '[', '{'):
            stack.push(c)
        else:
            last_c = stack.pop()
            if last_c == '(' and c != ')':
                raise ValueError("Inconsistent parenthesis %s and %s" % last_c, c)
            if last_c == '[' and c != ']':
                raise ValueError("Inconsistent parenthesis %s and %s" % last_c, c)
            if last_c == '{' and c != '}':
                raise ValueError("Inconsistent parenthesis %s and %s" % last_c, c)
    if stack.size() != 0:
        raise ValueError("Incorrect parenthesis sequence")

    return True


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "parseq_test.dat"
    with open(filename) as file:
        s = file.readline()
        try:
            res = check_parenthesis_sequence(s)
            print("yes")
        except Exception as e:
            print("no")
