#!/usr/bin/env python3
"""
Using the Movielens Dataset located:  exercises/Module_01/MovieLens/

Make a Script that preforms Chi-Square on the ratings of any genre category with over 2000 entries in the dataset.

The comparison should be between the distribution of ratings above, equal to, and below the median rating of the dataset.

Note:  The first step will be to determine the median rating of the dataset

Test to 99% confidence.

Optional:  Incorporate a Matplotlib barplot into the script to visualize the category against the expected ratings from the population_ratings distribution

"""

import pandas as pd
import numpy as np
from scipy import stats
from collections import defaultdict

def pop_list_with_values(ratings_list, median):
    list_to_pop = [0, 0, 0]
    for item in ratings_list:
        if item < median:
            list_to_pop[0] += 1
        elif item == median:
            list_to_pop[1] += 1
        else:
            list_to_pop[2] += 1

    return list_to_pop

def determine_percentages_list(data, median):
    below_count = 0
    at_count = 0
    above_count = 0
    total_entries = len(data)

    for rating in data:
        if rating < median:
            below_count += 1
        elif rating == median:
            at_count += 1
        else:
            above_count += 1

    below = below_count / total_entries
    at = at_count / total_entries
    above = above_count / total_entries

    return [below, at, above]

def calc_actual_list(percent_list, total):
    ret_list = [0,0,0]

    for i in range(3):
        ret_list[i] = percent_list[i] * total

    return ret_list

def generated_expected_values(entry_len, observered_list):
    expected_list = [0.0, 0.0, 0.0]

    for i in range(3):
        expected_list[i] = observered_list[i] * entry_len
    
    return expected_list

def main():
    # populate and merge data frames
    movies_df = pd.read_csv('files/movies.csv')
    ratings_df = pd.read_csv('files/ratings.csv')
    df = pd.merge(movies_df, ratings_df)

    # list of all ratings
    population_ratings = df['rating'].tolist()

    # populate genre/ratings dictionary
    genre_ratings = defaultdict(list)
    for _, movie in df.iterrows():
        movie_genres = movie['genres'].split("|")
        for genre in movie_genres:
            genre_ratings[genre].append(movie['rating'])

    # determine the median rating of the dataset
    total_median = df['rating'].median()

    # critical_value = stats.chi2.ppf(q=0.99, df=2)
    # print(f"\n{critical_value = }")

    observed_percentages = determine_percentages_list(population_ratings, total_median)

    observed_actual = calc_actual_list(observed_percentages, len(population_ratings))

    for genre, ratings_list in genre_ratings.items():
        if len(ratings_list) > 2000:
            # perform chi-square
            expected = generated_expected_values(len(ratings_list), observed_percentages)

            actual = pop_list_with_values(ratings_list, total_median)

            print(f"Genre:        {genre}")
            print(f"Observed %:   {observed_percentages}")
            print(f"Expected %:   {expected}")
            print(f"Obsereved:    {observed_actual}")
            print(f"Actual:       {actual}")
            print(f"Sum Observed: {sum(expected)}")
            print(f"Sum Actual:   {sum(expected)}")
            
            # conduct the chi-squared
            curr_critical, p_value = stats.chisquare(np.array(actual), np.array(expected))
            print(f"P Value:      {p_value}")
            print("\n")

if __name__=="__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("Exiting Program.")
