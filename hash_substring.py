# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 

    choice = input().rstrip()
    
    if "I" in choice:
        pattern = input()
        text = input()
    if "F" in choice:
        with open("tests/06") as f:
            pattern = f.readline()
            text = f.readline()

    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    occurences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)]==pattern:
            occurences.append(i)
    return occurences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

