import numpy as np
import random
from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

row_contents = ['participant_id', 'day', 'prompts', 'answers', 'ema']  

append_list_as_row('participant_data.csv', row_contents)

participant_id = 1

mu, sigma = 12, 1.2 # mean and standard deviation
s_prompts = np.random.normal(mu, sigma, 30)

n, p = 10, .8
s_answers = np.random.binomial(n, p, 30)

ema_options = [0,1]

for i in range(30):
    p_list = []

    p_list.append(participant_id)
    p_list.append(i+1)
    p_list.append(int(round(s_prompts[i])))
    p_list.append(s_answers[i])
    p_list.append(random.choice(ema_options))

    append_list_as_row('participant_data.csv', p_list)

# print(p_list)