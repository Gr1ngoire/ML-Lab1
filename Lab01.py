import statistics as st
import matplotlib.pyplot as plt
import pandas as pd


# TASK 1 (Taken from https://ukrstat.gov.ua/)
excel_data = pd.read_excel('innovations_dataset.xlsx')

data = pd.DataFrame(excel_data)

print("====================================")



# TASK 2 (About Other spends)

other_spends = data["Other spends"]

# Mean
mean = st.mean(other_spends)
print(f"Mean: {mean}")

# Median
median = st.median(other_spends)
print(f"Median: {median}")

# Mode (346.6 is printed out because there are no values here, wich appear more than once)
mode = st.mode(other_spends)
print(f"Mode: {mode}")

# Dispersion
dispersion = st.pvariance(other_spends)
print(f"Dispersion: {dispersion}")

# Standard deviation
standard_deviation = st.pstdev(other_spends)
print(f"Standard deviation: {standard_deviation}")

print("====================================")

'''
 # TASK 3
x = data["Year"]
y = other_spends

plt.hist(y)
plt.show()
plt.bar(x, y)
plt.show()

print("====================================")


# TASK 4

# Series
# create Series
other_spends_series = pd.Series(excel_data["Other spends"])

# Series output
print("Series output")
print(other_spends_series)

# Series with identical values
print("Series with identical values")
identical_series = pd.Series(7, range(3))

# Call the element of Series in particular index
print("Call the element of Series in particular index")
print(other_spends_series[0])

# Calculations describing statistics
print("Calculations describing statistics")
# quantity
print("quantity")
print(other_spends_series.count())
# maen
print("mean")
print(other_spends_series.mean())
# min
print("min")
print(other_spends_series.min())
# max
print("max")
print(other_spends_series.max())
# standard deviation
print("standard deviation")
print(other_spends_series.std())
# description
print("description")
print(other_spends_series.describe())

# Creation with non-standard indexes
not_standard_indexes_series = pd.Series(other_spends.values, index=data["Year"])
print("Creation with non-standard indexes")
print(not_standard_indexes_series)

# Dictionary as initializer
dict_inited_series = pd.Series({'IA-11': 27, 'IA-12': 29, 'IA-13': 29, 'IA-14': 30})
print("Dictionary as initializer")
print(dict_inited_series)

# Call with non standard indexes
print("Call with non standard indexes")
print(dict_inited_series['IA-11'])

# Create Series with strings
string_series = pd.Series(data.T.index)
print("Create Series with strings")
print(string_series)

# String check
print("String check")
print(string_series.str.contains('r'))

# To upper case
print("To upper case")
print(string_series.str.upper())

# DataFrame
print("DataFrame")
# Dict based DataFrame creation
print("Dict based DataFrame creation")
mock_data = excel_data.T.values
dict_based_dataframe = pd.DataFrame({'Year': mock_data[0], 'Other spends': mock_data[-1]})
print(dict_based_dataframe)

# Setting DataFrame indexes
dict_based_dataframe.index = [data["Year"][index] - 10 for index, _ in enumerate(data["Year"])]
print("Setting DataFrame indexes")
print(dict_based_dataframe)

# Call DataFrame columns
print("Call DataFrame columns")
print((dict_based_dataframe['Year']))
print((dict_based_dataframe.Year))

# Picking rows using loc, iloc
print("Picking rows using loc, iloc")
print(dict_based_dataframe.loc[1990])
print(dict_based_dataframe.iloc[0])

# Rows select with loc/iloc attributes
print("Rows select with loc/iloc attributes")
print(dict_based_dataframe.loc[1990:2000])
print(dict_based_dataframe.iloc[0: 10])

# Rows and columns subsets select
print("Rows and columns subsets select")
print(dict_based_dataframe.loc[1990 : 1995, ['Year', 'Other spends']])

# Logical indexing
print("Logical indexing")
print(dict_based_dataframe[dict_based_dataframe > 900])
print(dict_based_dataframe[(dict_based_dataframe > 900) & (dict_based_dataframe < 2000)])

# Call specific DataFrame part by row and column
print("Call specific DataFrame part by row and column")
print(dict_based_dataframe.at[1990, 'Other spends'])
print(dict_based_dataframe.iat[0, 1])
dict_based_dataframe.at[1990, 'Other spends'] = 500

# Describing statistics
print("Describing statistics")
print(dict_based_dataframe.describe())
pd.set_option('display.precision', 2)
print(dict_based_dataframe.describe())

# mean
print("mean")
print(dict_based_dataframe.mean())

# Transposition
print("Transposition")
print(dict_based_dataframe.T)

# Describe transposition
print("Describe transposition")
print(dict_based_dataframe.T.describe())

# Transposition mean
print("Transposition mean")
print(dict_based_dataframe.T.mean())

# Sorting rows by indexes
print("Sorting rows by indexes")
print(dict_based_dataframe.sort_index(ascending=False))

# Sorting columns by indexes
print("Sorting columns by indexes")
print(dict_based_dataframe.sort_index(axis=1))

# Sorting columns by values
print("Sorting columns by values")
print(dict_based_dataframe.sort_values(by=1998, axis=1, ascending=(False)))
print(dict_based_dataframe.T.sort_values(by=1990, ascending=False))
print(dict_based_dataframe.loc[2008].sort_values(ascending=False))

# Copying and sorting in place
print("Copying and sorting in place")
dict_based_dataframe.sort_index(ascending=False, inplace=True)
print(dict_based_dataframe)

print("====================================")




# TASK 5
# Clearing the data
print("Clearing the data")
# These columns include unconsistent data which should be replaced
print(data["Inner researches"])
print(data["Outer researches"])

def mean_out_of_inconsistent_data(column):
    mean = 0
    length_of_consistent_values = 0
    for value in column: 
        try:
            mean += float(value)
            length_of_consistent_values += 1
        except ValueError:
            continue
    return round(mean / length_of_consistent_values, 2)

# Replacing it with mean of all other valid units in column
def replace_inconsistent_values_with_mean(column):
    mean = 0
    for index, value in enumerate(column):
        try:
            column[index] = float(value)
        except ValueError:
            if (mean == 0):
                mean = mean_out_of_inconsistent_data(column)
            column.replace(column[index], mean, inplace=True)
            
replace_inconsistent_values_with_mean(data["Inner researches"])
print(data["Inner researches"])

replace_inconsistent_values_with_mean(data["Outer researches"])
print(data["Outer researches"])

# Data check
print("Data check")
print(data["Year"].gt(2000))
print(data["Year"] < 2016)

# Data reformation
print("Data reformation")
# Show only 2 last digits of the year
def get_last_two_digits_of_year(year):
    return str(year)[-2:]

formatted_phone_numbers = data['Year'].map(get_last_two_digits_of_year)
print(formatted_phone_numbers)

print("====================================")


# TASK 6/7
titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')

print("====================================")


# TASK 8
print(titanic.head())
print(titanic.tail())

print("====================================")



# TASK 9
titanic.columns = ['name', 'survived', 'sex', 'age', 'class']
print(titanic.head())

print("====================================")



# TASK 10

print(f"Quantity of records in columns {titanic.count()}")

# Youngest passenger
least_age = titanic["age"].min()
youngest_passanger_index = titanic[titanic["age"] == least_age].index[0]
youngest_passanger = titanic.iloc[youngest_passanger_index]
print(f"Youngest passanger: {youngest_passanger}")

# Oldest passenger
biggest_age = titanic["age"].max()
oldest_passanger_index = titanic[titanic["age"] == biggest_age].index[0]
oldest_passanger = titanic.iloc[oldest_passanger_index]
print(f"Oldest passenger {oldest_passanger}")

# Mean of ages
print(f"Mean of ages {titanic['age'].mean()}")

# Survived passengers general statistics
survived_passengers = titanic[titanic["survived"] == 'yes']
print(survived_passengers.describe())
quantity_of_survived_men = len(survived_passengers[survived_passengers["sex"] == 'male'].index)
quantity_of_survived_women = len(survived_passengers[survived_passengers["sex"] == 'female'].index)
print(f"Survived men: {quantity_of_survived_men}, Survived woman: {quantity_of_survived_women}")

# Women statistics
women_with_first_class_places = titanic[titanic["sex"] == 'female'][titanic[titanic["sex"] == 'female']["class"] == "1st"]
print(f"Women with first class places {women_with_first_class_places}")

youngest_of_women_with_first_class_places = women_with_first_class_places[women_with_first_class_places["age"] == women_with_first_class_places["age"].min()]
print(f"Youngest of women with first class places {youngest_of_women_with_first_class_places}")

oldest_of_women_with_first_class_places = women_with_first_class_places[women_with_first_class_places["age"] == women_with_first_class_places["age"].max()]
print(f"Oldest of women with first class places {oldest_of_women_with_first_class_places}")

quantity_of_survived_women_with_first_class_places = len(women_with_first_class_places[women_with_first_class_places["survived"] == "yes"])
print(f"Quantity of survived women with first class places {quantity_of_survived_women_with_first_class_places}")

print("====================================")


# TASK 11
# Age histogram

titanic["age"].hist()

'''