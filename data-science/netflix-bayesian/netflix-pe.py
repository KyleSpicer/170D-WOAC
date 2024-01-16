#!/usr/bin/env python3

"""
Using the netflix.csv located at exercises/Module_01/Netflix/:

1. Construct a 2x2 probability matrix with the axises of "PG/Not PG" Ratings and "Above Median User Rating/At or Below Median User Rating".

2. Should disregard any entries missing the rating or user_rating_score fields

3. Determine the probability that an item has an above average rating given that it has a PG Rating.
"""

import pandas as pd

def main():
    # populate data frame
    df = pd.read_csv("netflix.csv")

    # drop missing fields
    df = df.dropna(subset=['rating', 'user_rating_score'])

    total_count = len(df)
    pg_count = df['rating'].value_counts()['PG']
    non_pg_count = total_count - pg_count 

    pg_probability = pg_count / total_count
    non_pg_probability = non_pg_count / total_count

    total_urs_median = df['user_rating_score'].median()

    pg_above_count = 0
    pg_at_below_count = 0
    not_pg_above_count = 0
    not_pg_at_below_count = 0

    # for frame in df:
    for _, rating in df.iterrows():
        curr_rating = rating['rating']
        curr_user_score = rating['user_rating_score']
        if 'PG' == curr_rating:
            if curr_user_score > total_urs_median:
                pg_above_count += 1
            else:
                pg_at_below_count += 1
        else:
            if curr_user_score > total_urs_median:
                not_pg_above_count += 1
            else:
                not_pg_at_below_count += 1

    pg_at_below = pg_at_below_count / total_count
    pg_above = pg_above_count / total_count
    not_pg_at_below = not_pg_at_below_count / total_count
    not_pg_above = not_pg_above_count / total_count
    ab_total = pg_at_below + not_pg_at_below
    above_total = not_pg_above + pg_above


    print("\nRating   |  At/Below            | Above               | Total")
    print("---------------------------------------------------------------------------")
    print(f"PG       |  {pg_at_below} | {pg_above} | {pg_count / total_count}")
    print(f"Not PG   |  {not_pg_at_below} | {not_pg_above}  | {non_pg_count / total_count}")
    print(f"Total    |  {ab_total}  | {above_total} | {total_count / total_count}")

    print("\n")


    

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting Program.")
