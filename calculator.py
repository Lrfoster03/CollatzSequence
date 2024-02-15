sequence = []

def computeSequence(input):
    sequence.append(input.__int__())
    if input == 1:
        return 
    elif input % 2 == 0:
        return computeSequence(input / 2)
    else:
        return computeSequence(3 * input + 1)
    
input = input("Enter a number: ")
input = int(input)
if(input > 0):
    computeSequence(input)
    print(sequence)
else:
    print("Invalid input")