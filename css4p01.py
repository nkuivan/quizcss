# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Data importation using pandas

import pandas as pd
dat = pd.read_csv("movie_dataset.csv")

print(dat)
print(dat.info())

# The columns Revenue (Millions) and Metascore have 128 and 64 missing values respectively.

# Correcting the column names, replace spaces with an underscore then filling NANs with means

dat.columns = dat.columns.str.strip().str.replace(" ", "_")

x=dat["Revenue_(Millions)"].mean()
dat["Revenue_(Millions)"].fillna(x, inplace = True) 

y=dat["Metascore"].mean()
dat["Metascore"].fillna(y, inplace = True)

# Qn1

highest_rated_movies = dat.nlargest(5, 'Rating')

print(highest_rated_movies)

# Qn2 

average_revenue = dat['Revenue_(Millions)'].mean()

print(f"The average revenue of all movies is: {average_revenue}")

# Qn 3

filter_dat = dat[(dat['Year'] >= 2015) & (dat['Year'] <= 2017)]
avg_rev = filter_dat['Revenue_(Millions)'].mean()

print(f"The average revenue of movies between 2015 and 2017 is: {avg_rev}")

# Qn4
num_movies_2016 = dat['Year'].value_counts()[2016]

print(f"The number of movies released in 2016 is: {num_movies_2016}")

# Qn5
num_mov_nolan = dat['Director'].value_counts()["Christopher Nolan"]

print(f"The number of movies directed by Christopher Nolan is: {num_mov_nolan}")

#Qn6

num_atleast_8 = (dat['Rating'] >= 8.0).sum()

print(f"The number of movies with a rating of at least 8.0 is: {num_atleast_8}")

# Qn 7

fil_nolan= dat[(dat['Director']=="Christopher Nolan")]

med_rating= fil_nolan['Rating'].median()

print(f"The median rating of movies directed by Nolan is: {med_rating}")

# Qn 8

avg_ratings_year = dat.groupby('Year')['Rating'].mean()

yr_high_rating = avg_ratings_year.idxmax()

print(f"The year with the highest average rating is: {yr_high_rating}")

# Qn 9

num_movies_2006 = (dat['Year'] == 2006).sum()
num_movies_2016 = (dat['Year'] == 2016).sum()

percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase}%")

# Qn 10
dat['Actors'] = dat['Actors'].str.replace(', ', ',') #remove trailing blanks

actors = dat['Actors'].str.split(',', expand=True).stack() #split into singular entries per movie

most_common_actor = actors.value_counts().idxmax()

print(f"The most common actor in all the movies is: {most_common_actor}")

# Qn 11
dat['Genre'] = dat['Genre'].str.replace(', ', ',')

all_genres = dat['Genre'].str.split(',', expand=True).stack()

num_unique_genres = all_genres.nunique()

print(f"There are {num_unique_genres} unique genres in the dataset.")

# Qn 12

correlation_matrix = dat.corr(numeric_only=True)

print(correlation_matrix)

#pip install seaborn matplotlib # Install seaborn and matplotlib

import seaborn as sn
import matplotlib.pyplot as plt

# correlation matrix
plt.figure(figsize=(10, 8))  # Set the figure size

sn.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

plt.show()



