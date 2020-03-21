import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_input():
    while True:
        try:
            prob_head = float(input('What is the probability of head? (Give decimal ranging from 0 to 1)\n'))
        except:
            print('You did not entered a number. Please try again.')
        else:
            if prob_head > 0 and prob_head < 1:
                break
            else:
                print('You did not entered a decimal number between 0 to 1. Please try again.')

    while True:
        try:
            no_of_flips = int(input('For each trials, what is the number of flips? (Best to give integer greater than or equal to 10)\n'))
        except:
            print('You did not entered a integer. Please try again.')
        else:
            if no_of_flips >= 10:
                break
            else:
                print('You did not entered a integer greater than ror equal to 10. Please try again.')

    while True:
        try:
            no_of_trials = int(input('What is the number of trials? (Give positive integer)\n'))
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
    ans.append(list(range(1, no_of_flips + 1)))
    for i in range(0, no_of_trials):
        i = []

        for j in range(0, no_of_flips):
            if random.uniform(0,1) <= prob_head:
                i.append('H')
            else:
                i.append('T')

        ans.append(i)
    return ans

def coin_sim():
    prob_head, no_of_flips, no_of_trials = get_input()
    ans_matrix = simu(prob_head, no_of_flips, no_of_trials)

    data_raw = pd.DataFrame(ans_matrix).transpose()

    columns_name = ['flips']
    for i in range(1,no_of_trials+1):
        columns_name.append('trial_' + str(i))

    columns_name
    data_raw.columns = columns_name

    data_num = data_raw.copy()
    data_num[data_raw[columns_name[1:no_of_trials + 1]]=='H'] = 1
    data_num[data_raw[columns_name[1:no_of_trials + 1]]=='T'] = 0

    data_cum = pd.merge(left = data_raw['flips'], right = data_num[columns_name[1:no_of_trials + 1]].cumsum(), left_index=True, right_index=True)
    data_prob = data_cum.copy()

    for i in range(0,no_of_trials):
        data_prob[data_prob.columns[i+1]] = data_prob[data_prob.columns[i+1]] / data_prob['flips']

    prob_vec = np.ones(no_of_flips) * prob_head
    prob_vec = pd.DataFrame(prob_vec)
    prob_vec

    data_prob = pd.merge(left = data_prob, right = prob_vec, left_index=True, right_index=True)
    data_prob

    colormap = plt.cm.gist_ncar
    plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, no_of_trials))))
    plt.plot(data_prob['flips'], data_prob[data_prob.columns[1:no_of_trials + 2]])
    plt.title('Coin Simulation ({} trials with {} of getting head)'.format(no_of_trials, prob_head))
    plt.xlabel('Number of Tosses')
    plt.ylabel('Proportion of Heads')
    plt.show()

    return data_raw
