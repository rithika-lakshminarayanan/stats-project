import numpy as np
import random
from csv import writer
import os

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

row_contents = ['participant_id', 'day', 'prompts', 'answers', 'sleep_hours', 'ema']

path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/participant_data.csv'))

append_list_as_row(path, row_contents)

participant_id = 1
num_participants = 100
days = 30

while participant_id <= num_participants:

    mu = random.uniform(9, 13)
    sigma = random.uniform(0.7, 2.1)
    n = random.randint(5, 12)
    p = random.uniform(0.2, 0.8)

    s_prompts = np.random.normal(mu, sigma, days)

    s_answers = np.random.binomial(n, p, days)

    sleep_hours = np.random.uniform(4.5, 10.6, days)

    round_sleep = [round(num, 1) for num in sleep_hours]

    ema = np.random.randint(2, size=days)

    for i in range(days):
        p_list = []
        if s_answers[i]>int(round(s_prompts[i])):
            s_answers[i] = int(round(s_prompts[i]))

        p_list.append(participant_id)
        p_list.append(i+1)
        p_list.append(int(round(s_prompts[i])))
        p_list.append(s_answers[i])
        p_list.append(round_sleep[i])
        p_list.append(ema[i])

        append_list_as_row(path, p_list)

    participant_id += 1

# print(p_list)