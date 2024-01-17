#!/usr/bin/env python3

"""
The file "distributions.npy" located at exercises/Module_01/Distributions, contains 3 1D arrays, determine the distribution types of the data in the 3 1D arrays.

Incorporate visualization methods into your solutions by either:

1.  Determining the distribution by mathematical means and confirming with visualization

2.  Determining the distribution by visualization alone
"""

import numpy as np
import matplotlib.pyplot as plt

labels = ["Normal", "Uniform", "Poisson"]

def display_specific_array(array, array_number):
    print(f"{labels[array_number - 1]} Array")

    # mathematical analysis
    print(f"Mean: {np.mean(array)}")
    print(f"Median: {np.median(array)}")
    print(f"Standard Deviation: {np.std(array)}")
    print(f"Variance: {np.var(array)}\n")

    # visualization
    plt.hist(array, bins=50)
    plt.title(f"{labels[array_number - 1]} Array")
    plt.show()

def main():
    
    arrays = np.load('distributions.npy')

    print("1: Normal Distribution\n"
          "2: Uniform Distribution\n"
          "3: Poisson Distribution\n"
          "4: Show All Distributions\n")
    choice = input("Enter your choice (1-4): ")

    if '1' == choice:
        display_specific_array(arrays[int(choice) - 1], int(choice))

    if '2' == choice: 
        display_specific_array(arrays[int(choice) - 1], int(choice))
    if '3' == choice: 
        display_specific_array(arrays[int(choice) - 1], int(choice))
    
    if '4' == choice:
        for i, array in enumerate(arrays):
            print(f"Array {i+1}")

            # mathematical analysis
            print(f"Mean: {np.mean(array)}")
            print(f"Median: {np.median(array)}")
            print(f"Standard Deviation: {np.std(array)}")
            print(f"Variance: {np.var(array)}\n")

            # visualization
            plt.hist(array, bins=50)
            plt.title(f"Histogram of Array {i+1}")
            plt.show()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting Program.")
