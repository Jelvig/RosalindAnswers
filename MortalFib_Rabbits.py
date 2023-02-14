"""Mortal Fibonacci Rabbits, first make a list of all the generations that will happen,
    Then as each generation gets summed one at time, 
    what is the total after the inputed months?"""

def fib(month, age):
    generation = [0]*age  # list of all generations that will happen
    generation[0], generation[1] = 0,1  # will always start with 0 and 1
    for _ in range(2,month): 
        temp = list(generation)
        generation[0] = sum(generation[1:]) # sum of new borns
        for i in range(1,age): 
            generation[i] = temp[i-1]  # count down of the number of generations
    return sum(generation)

print(fib(83,16))

"""More pythonic answer from online"""
# def fib(n,k=1):
#   ages = [1] + [0]*(k–1)
#   for i in xrange(n–1):
#     ages = [sum(ages[1:])] + ages[:–1]
#   return sum(ages)
