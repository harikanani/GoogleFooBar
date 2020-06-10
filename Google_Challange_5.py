def solution(l):

    #  inputs: [1,6,7,9,12,36]
    #  outputs:
    #                              1 
    #                             /|\ 
    #          [1,9,36]          / | \ 
    #          [1,12,36]        /  |  \ 
    #          [6,12,36]       6---+   9 
    #          [1,6,12]         \ 12  / 
    #          [1,6,36]          \ | / 
    #                             \|/  
    #                             36
    # 
    # if (x divides y divides z):   
    # x ------> y -------> z 
    #    input     output
    # 
    # inputs[y] = x
    # outputs[y] = z

    inputs = {}   # count of inputs to a number
    outputs = {}  # count of outputs from a number
    counter = 0

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if(l[j] % l[i] == 0):  # l[i] divides l[j]
                inputs[j] = inputs.get(j, 0) + 1
                outputs[i] = outputs.get(i, 0) + 1
    for i in inputs:
        counter += inputs[i] * outputs.get(i, 0)

    return counter
    
# Test Cases
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))
