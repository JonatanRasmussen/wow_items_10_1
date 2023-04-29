import pandas as pd

# Load CSV into a Pandas DataFrame with ";" as the delimiter
filename = "wow_items_s2"
df = pd.read_csv(f'{filename}.csv', sep=';')
# Print the first 5 rows of the DataFrame
print(df.head())
name = '*Item'
catagory = 'Dungeon'
itemtype = '*Slot'

#%%

# Create an empty dictionary
category_dict = {}

# Iterate over the DataFrame and add the names of each row to the appropriate category list
for index, row in df.iterrows():
    source = row[catagory]
    my_name = row[name]
    if source in category_dict:
        category_dict[source].append(my_name)
    else:
        category_dict[source] = [my_name]

#%%


# Print the dictionary
df_counts = pd.crosstab(index=df[catagory], columns=df[itemtype])

# Print the new DataFrame
print(df_counts)

#%%


# Group the DataFrame by category and type, and apply the tolist method to the groups to get lists of names
df_names = df.groupby([catagory, itemtype])[name].apply(list).reset_index()

# Pivot the DataFrame to put categories on one axis and types on another axis
df_pivot = df_names.pivot(index=catagory, columns=itemtype, values=name)

# Print the new DataFrame
print(df_pivot)

#%%

# Define the Filter() function
def Filter(name):
    # Your filtering logic here
    if len(name) > 10:
        return True
    else:
        return False


# Apply the Filter() function to each name in the DataFrame, and only add the name to the list if Filter() returns True
df_filtered = df[df[name].apply(Filter)].reset_index(drop=True)

# Group the filtered DataFrame by category and type, and apply the tolist method to the groups to get lists of names
df_names = df_filtered.groupby([catagory, itemtype])[name].apply(list).reset_index()

# Pivot the DataFrame to put categories on one axis and types on another axis
df_pivot = df_names.pivot(index=catagory, columns=itemtype, values=name)

# Print the new DataFrame
print(df_pivot)

#%%

def get_stats(df, item_name):
    # Find the row in the DataFrame that contains an element matching str_A in the "Name" column
    row = df[df[name] == item_name]
    if not row.empty:
        # Return the value in the "Mainstat" column of that row
        mainstat = row.iloc[0]['Main Stat']
        operator = row.iloc[0]['Operator']
        secondarystat = row.iloc[0]['Sec Stat']
        return mainstat+' '+operator+' '+secondarystat
    else:
        # If no row contains the specified element, return None
        return None

# Example usage of the get_mainstat function
item_name = "Crechebound Soldier's Boots"
mainstat_value = get_stats(df, item_name)
if mainstat_value is not None:
    print(f"The mainstat value for element {item_name} is {mainstat_value}.")
else:
    print(f"No element with the name {item_name} was found.")
