import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

# Read in the data
movies = pd.read_csv("movies.csv")

# Review the data

movies.head(2)

# Checking to see if there is any missing data
for col in movies.columns:
   pct_missing = np.mean(movies[col].isnull())
   print('{} - {}%'.format(col, pct_missing))

# Check for null values
movies_isnull = movies.isnull().any().any()
movies_isnull

# Check Column datatype
movies.dtypes

# Changing float data types to integers for some columns
#movies['budget'] = movies['budget'].astype('int64')

#movies['gross'] = movies['gross'].astype('int64')

# using following because the above did not work due to nulls
movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')
# Now replace NaN with 0 or another value if needed
movies.fillna({"budget":0}, inplace=True)
#movies['budget'].fillna(0, inplace=True)
movies['budget'] = movies['budget'].astype('int64')


movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')
# Now replace NaN with 0 or another value if needed
movies.fillna({"gross":0}, inplace=True)

movies['gross'] = movies['gross'].astype('int64')


# Checking released year column 
movies['released'] = movies['released'].fillna('').astype(str)

# Step 2: Remove the extra text "(United States)" using a regular expression
movies['released'] = movies['released'].str.replace(r'\s\(.+?\)', '', regex=True)

# Step 3: Convert the cleaned-up date column to datetime format
movies['released'] = pd.to_datetime(movies['released'], format='%B %d, %Y', errors='coerce')

# Step 4: Extract the year
movies['released_year'] = movies['released'].dt.year

movies['released_year'] = movies['year'].fillna(0).astype(int)

# Sorting values
movies_sort = movies.sort_values(by=['gross'], inplace=False, ascending=False)
movies_sort.head(2)

pd.set_option('display.max_rows', None)

# Drop any duplicates in column company
movies['company'].drop_duplicates().sort_values(ascending=False)

# Create scatter plot with budget vs. gross

plt.scatter(x=movies['budget'], y=movies['gross'])

plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')

plt.show()

# Plot the budget vs gross using seaborn --> regression plot with added detail to dots and line

sns.regplot(x='budget', y='gross', data=movies, scatter_kws={'color': 'red'}, line_kws={'color':'blue'})

# Checking correlation
# Get numerical columns as correlation can only be done on numerical columns
numeric_cols = ['budget', 'gross', 'runtime', 'score', 'votes', 'released_year']

# Now calculate the correlation for numeric columns only - default/pearon method
corr_matrix = movies[numeric_cols].corr(method='pearson')

corr_matrix

corr_matrix = movies[numeric_cols].corr(method='pearson')

sns.heatmap(corr_matrix, annot=True)

plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.show()

movies_numerized = movies

for col in movies_numerized:
    if (movies_numerized[col].dtype == 'object'):
        movies_numerized[col] = movies_numerized[col].astype('category')
        movies_numerized[col] =  movies_numerized[col].cat.codes

movies_numerized.head(2)


# using movies numerized
corr_matrix_numerized = movies_numerized.corr(method='pearson')

sns.heatmap(corr_matrix_numerized, annot=True)

plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.show()


corr_matrix_numerized = movies_numerized.corr(method='pearson')

# separating the list to show pairs without being under specific categories
corr_pairs = corr_matrix_numerized.unstack()

sorted_pairs = corr_pairs.sort_values()

high_corr = sorted_pairs[(sorted_pairs) > 0.5]

high_corr

# Votes and Budget have the highest correlation to Gross Earnings,