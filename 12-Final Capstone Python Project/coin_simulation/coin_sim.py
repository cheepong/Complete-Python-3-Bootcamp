import random
import numpy as np
import pandas as pd
import matplotlib

%matplotlib

def get_input():
    while True:
        try:
            prob_head = float(input('What is the probability of head? (Give decimal ranging from 0 to 1)'))
        except:
            print('You did not entered a number. Please try again.')
        else:
            if prob_head > 0 and prob_head < 1:
                break
            else:
                print('You did not entered a decimal number between 0 to 1. Please try again.')

    while True:
        try:
            no_of_flips = int(input('For each trials, what is the number of flips? (Best to give integer greater than or equal to 10)'))
        except:
            print('You did not entered a integer. Please try again.')
        else:
            if no_of_flips >= 10:
                break
            else:
                print('You did not entered a integer greater than ror equal to 10. Please try again.')

    while True:
        try:
            no_of_trials = int(input('What is the number of trials? (Give positive integer)'))
        except:
            print('You did not entered a integer. Please try again.')
        else:
            if no_of_trials >= 1:
                break
            else:
                print('You did not entered a positive integer. Please try again.')

    return prob_head, no_of_flips, no_of_trials

def simu(prob_head, no_of_flips, no_of_trials):
    ans = []
    for i in range(0, no_of_trials-1):
        i = []

        for j in range(0, no_of_flips-1):
            i.append(random.randint(0,1))

        ans.append(i)
    return ans

prob_head, no_of_flips, no_of_trials = get_input()
ans_matrix = simu(prob_head, no_of_flips, no_of_trials)

print(ans_matrix)
