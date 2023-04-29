import pandas as pd
from wow_spec_specs import initialize_spec_objects

# Load CSV into a Pandas DataFrame with ";" as the delimiter
filename = "wow_items_s2"
df = pd.read_csv(f'{filename}.csv', sep=';')
# Print the first 5 rows of the DataFrame
#print(df.head())
name = '*Item'
catagory = 'Dungeon'
itemtype = '*Slot'
armor_tier = 'Type'
catagory_mainstat = ['Main Stat']


#%%

def matching_main_stat(trinket_mainstat, primary_stat):
    return (primary_stat in trinket_mainstat)


def loot_type_compatibility(armor_type, slot, mainstat, instance):
    # Check if cloth/leather/mail/plate
    lst_of_armor_tiers = ['cloth', 'leather', 'mail', 'plate']
    lst_of_accessories = ['back', 'neck', 'ring']
    lst_of_weapon_slots = ['one hand', 'two hand', 'off-hand']
    if str(armor_type).lower() in lst_of_accessories:
        return True
    if str(armor_type).lower() in lst_of_armor_tiers:
        if str(armor_type).lower() == str(instance.armor):
            return True
        else:
            return False
    if str(slot).lower() in lst_of_weapon_slots:
        for weapon_og in instance.weapons:
            weapon = str(weapon_og).lower()
            weapon = weapon.lower().replace('off-hand', 'oh - int')
            weapon = weapon.lower().replace('axe 1h', '1h axe')
            weapon = weapon.lower().replace('mace 1h', '1h mace')
            weapon = weapon.lower().replace('sword 1h', '1h sword')
            weapon = weapon.lower().replace('axe 2h', '2h axe')
            weapon = weapon.lower().replace('mace 2h', '2h mace')
            weapon = weapon.lower().replace('sword 2h', '2h sword')
            if weapon in str(armor_type).lower():
                if ' - ' in str(armor_type).lower():
                    if str(instance.primary_stat) in str(armor_type).lower():
                        return True
                else:
                    return True

    if str(slot).lower() == 'trinket':
        trinket_type = str(armor_type).lower()
        trinket_mainstat = str(mainstat).lower()
        role = str(instance.role)
        primary_stat = str(instance.primary_stat)
        if trinket_type == 'all':
            return True
        elif trinket_type == 'tank' and role == 'tank':
            return True
        elif trinket_type == 'healer' and role == 'healer':
            return True
        elif trinket_type == 'caster' and primary_stat == 'int':
            return True
        elif trinket_type == 'mdps' and (primary_stat in trinket_mainstat):
            return True
        elif trinket_type == 'rdps' and (primary_stat in trinket_mainstat):
            return True
        elif trinket_type == 'mdps' and primary_stat == 'str' and trinket_mainstat == 'mastery':
            return True
        elif trinket_type == 'mdps' and primary_stat == 'str' and trinket_mainstat == 'crit':
            return True
        elif trinket_type == 'mdps' and primary_stat == 'agi' and trinket_mainstat == 'crit':
            return True
        elif trinket_type == 'rdps' and primary_stat == 'agi' and trinket_mainstat == 'mastery':
            return True
        elif trinket_type == 'rdps' and primary_stat == 'int' and trinket_mainstat == 'mastery':
            return True
    return False

# Define the Filter() function
def filter_loot(df, instance, item_name):
    # get relevant df row
    row = df[df[name] == item_name]
    if not row.empty:
        armor_type = row.iloc[0][armor_tier]
        slot = row.iloc[0][itemtype]
        mainstat = row.iloc[0][catagory_mainstat]
    else:
        assert(False)
    if loot_type_compatibility(armor_type, slot, mainstat, instance):
        return True
    else:
        return False

def get_stats(df, item_name):
    # Find the row in the DataFrame that contains an element matching str_A in the "Name" column
    row = df[df[name] == item_name]
    if not row.empty:
        # Return the value in the "Mainstat" column of that row
        mainstat = row.iloc[0][catagory_mainstat]
        #operator = row.iloc[0]['Operator']
        operator = '>'
        secondarystat = row.iloc[0]['Sec Stat']
        return f'{mainstat} {operator} {secondarystat}'
    else:
        # If no row contains the specified element, return None
        return None

def generate_table(df, instance):
    # Apply the Filter() function to each name in the DataFrame, and only add the name to the list if Filter() returns True
    df_filtered = df[df[name].apply(lambda x: filter_loot(df, instance, x))].reset_index(drop=True)
    # Rename the name of the item to its stats
    df_filtered[name] = df_filtered[name].apply(lambda x: get_stats(df_filtered, x))
    # Count number of items
    df_counts = pd.crosstab(index=df_filtered[catagory], columns=df_filtered[itemtype])
    # Group the filtered DataFrame by category and type, and apply the tolist method to the groups to get lists of names
    df_names = df_filtered.groupby([catagory, itemtype])[name].apply(list).reset_index()
    # Pivot the DataFrame to put categories on one axis and types on another axis
    df_pivot = df_names.pivot(index=catagory, columns=itemtype, values=name)
    #return df_pivot
    return df_counts
    # Print the new DataFrame
    print(df_pivot)
    print(df_counts)

def iterate_over_specs(df):
    tables = {}
    instances = initialize_spec_objects()
    for instance in instances:
        table = generate_table(df, instance)
        tables[instance.specname] = table

    print(tables['Fire Mage'])

iterate_over_specs(df)