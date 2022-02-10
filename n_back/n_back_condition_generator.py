import os
import csv
import time
import numpy as np

# TODO: call this script in the PsychoPy experiment to create n-back data sets for the experiment automatically

def zero_back(num_rows):
    """
    Create zero-back vectors for number stimulus and match condition
    """

    match = np.random.randint(0, 10)

    num_match_list = []
    for i in range(num_rows):
        num_match_temp = []
        num_stim = np.random.randint(0, 10)
        num_match_temp.append(num_stim)

        if num_stim == match:
            num_match_temp.append(r"['space']")
        else:
            num_match_temp.append("")
        num_match_list.append(num_match_temp)

    return match, num_match_list

def zero_back_csv(num_rows):
    """
    Save zero-back vectors in a CSV file
    """

    match, num_match_list = zero_back(num_rows)
    filename = "zero_back-" + "match_" + f"{str(match)}-" + str(time.time()).replace(".", "") + ".csv"
    print("CSV filename: ", filename)

    with open(filename, mode="w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')  
        csv_writer.writerow(["num_stim", "match"])  
        
        for num, match in num_match_list:
            csv_writer.writerow([num, match])  

def one_back(num_rows):
    """
    Create one-back vectors for number stimulus and match condition
    """

    num_match_list = []
    for i in range(num_rows):
        num_match_temp = []
        num_stim = np.random.randint(0, 10)
        num_match_temp.append(num_stim)
        
        if i == 0:
            num_match_temp.append("")
        else:
            if num_stim == num_match_list[i-1][0]:
                num_match_temp.append(r"['space']")
            else:
                num_match_temp.append("")
        num_match_list.append(num_match_temp)

    return num_match_list

def one_back_csv(num_rows):
    """
    Save one-back vectors in a CSV file
    """

    num_match_list = one_back(num_rows)
    filename = "one_back-" + str(time.time()).replace(".", "") + ".csv"
    print("CSV filename: ", filename)

    with open(filename, mode="w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')  
        csv_writer.writerow(["num_stim", "match"])  
        
        for num, match in num_match_list:
            csv_writer.writerow([num, match])  

def two_back(num_rows):
    """
    Create two-back vectors for number stimulus and match condition
    """

    num_match_list = []
    for i in range(num_rows):
        num_match_temp = []
        num_stim = np.random.randint(0, 10)
        num_match_temp.append(num_stim)
        
        if i == 0 or i == 1:
            num_match_temp.append("")
        else:
            if num_stim == num_match_list[i-2][0]:
                num_match_temp.append(r"['space']")
            else:
                num_match_temp.append("")
        num_match_list.append(num_match_temp)

    return num_match_list

def two_back_csv(num_rows):
    """
    Save two-back vectors in a CSV file
    """

    num_match_list = two_back(num_rows)
    filename = "two_back-" + str(time.time()).replace(".", "") + ".csv"
    print("CSV filename: ", filename)

    with open(filename, mode="w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')  
        csv_writer.writerow(["num_stim", "match"])  
        
        for num, match in num_match_list:
            csv_writer.writerow([num, match])  

save_dir = input("Enter N-back conditions dir: ")  # directory to save the n-back datasets in
os.chdir(save_dir)

conditions = [0, 1, 2]
num_rows = 20   # number rows in the dataset CSV file

for condition in conditions:
    if condition == 0:
        for i in range(3):
            zero_back_csv(num_rows=num_rows)
            time.sleep(0.1)
    if condition == 1:
        for i in range(3):
            one_back_csv(num_rows=num_rows)
            time.sleep(0.1)
    if condition == 2:
        for i in range(3):
            two_back_csv(num_rows=num_rows)
            time.sleep(0.1)