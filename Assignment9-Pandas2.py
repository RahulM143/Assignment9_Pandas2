import pandas as pd

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
bname = pd.read_csv (url)
bname.head()

#1. Delete unnamed columns
print ('Columns before deletion of unnamed: \n', bname.columns)
del bname ['Unnamed: 0'] 
print ('Columns after deletion of unnamed: \n', bname.columns)

#2. Show the distribution of male and female
sf = bname.groupby(['Gender','State','Year']).Count.sum()
print('Distribution of male and females in the dataset:\n',sf)
 
#3. Show the top 5 most preferred names
pn = bname.groupby ('Name').Count.sum()
pt = pd.DataFrame(pn)
pt = pt.sort_values(['Count'], ascending = False)
print ('Top 5 most preferred names are:\n ', pt.head() )

#4. What is the median name occurence in the dataset
val = bname['Name'].value_counts()
med = val.median()
print('The median name occurence in the dataset is',int(med))

#5. Distribution of male and female born count by states
mf = bname.pivot_table(index='Gender', columns='State', values='Count', aggfunc='sum')
print ('Distribution of male and female born count by states \n', mf)




