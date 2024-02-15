input = input("Enter a number: ")
sequence = []

def computeSequence(input):
    sequence.append(input.__int__())
    if input == 1:
        return 1
    elif input % 2 == 0:
        return computeSequence(input / 2)
    else:
        return computeSequence(3 * input + 1)
    
computeSequence(int(input))
print(sequence)