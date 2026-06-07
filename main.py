# Import pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# code
decade_year = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999) 
& (netflix_df['type'] == 'Movie')]

duration = decade_year['duration'].mode()[0]
print(duration)

short_movie_count = netflix_df[(netflix_df['release_year'] >= 1990) & 
(netflix_df['release_year'] <= 1999) &
(netflix_df['type'] == 'Movie') &
(netflix_df['genre'] == 'Action') &
(netflix_df['duration'] < 90)].shape[0]
print(short_movie_count)

plt.scatter(type, genre, marker="o", color="blue")
plt.title("TV Shows that shows all genres")
plt.xlabel("TV Show")
plt.ylabel("Genre")
plt.grid(True, alpha=0.4)
plt.show()