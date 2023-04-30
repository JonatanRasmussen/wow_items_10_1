import pandas as pd

# Load CSV into a Pandas DataFrame with ";" as the delimiter
filename = "wow_weapon_proficiencies"
df = pd.read_csv(f'{filename}.csv', index_col=0, sep=';')
# Print the first 5 rows of the DataFrame
#print(df.head())

death_knight_blood = 'Blood Death Knight'
death_knight_frost = 'Frost Death Knight'
death_knight_unholy = 'Unholy Death Knight'
demon_hunter_havoc = 'Havoc Demon Hunter'
demon_hunter_vengeance = 'Vengeance Demon Hunter'
druid_balance = 'Balance Druid'
druid_feral = 'Feral Druid'
druid_guardian = 'Guardian Druid'
druid_restoration = 'Restoration Druid'
evoker_devastation = 'Devastation Evoker'
evoker_preservation = 'Preservation Evoker'
hunter_beast_mastery = 'Beast Mastery Hunter'
hunter_marksmanship = 'Marksmanship Hunter'
hunter_survival = 'Survival Hunter'
mage_arcane = 'Arcane Mage'
mage_fire = 'Fire Mage'
mage_frost = 'Frost Mage'
monk_brewmaster = 'Brewmaster Monk'
monk_mistweaver = 'Mistweaver Monk'
monk_windwalker = 'Windwalker Monk'
paladin_holy = 'Holy Paladin'
paladin_protection = 'Protection Paladin'
paladin_retribution = 'Retribution Paladin'
priest_discipline = 'Discipline Priest'
priest_holy = 'Holy Priest'
priest_shadow = 'Shadow Priest'
rogue_assassination = 'Assassination Rogue'
rogue_subtlety = 'Subtlety Rogue'
rogue_outlaw = 'Outlaw Rogue'
shaman_elemental = 'Elemental Shaman'
shaman_enhancement = 'Enhancement Shaman'
shaman_restoration = 'Restoration Shaman'
warlock_affliction = 'Affliction Warlock'
warlock_demonology = 'Demonology Warlock'
warlock_destruction = 'Destruction Warlock'
warrior_arms = 'Arms Warrior'
warrior_fury = 'Fury Warrior'
warrior_protection = 'Protection Warrior'

number_of_specs = 38

death_knight = [death_knight_blood, death_knight_frost, death_knight_unholy]
demon_hunter = [demon_hunter_havoc, demon_hunter_vengeance]
druid = [druid_balance, druid_feral, druid_guardian, druid_restoration]
evoker = [evoker_devastation, evoker_preservation]
hunter = [hunter_beast_mastery, hunter_marksmanship, hunter_survival]
mage = [mage_arcane, mage_fire, mage_frost]
monk = [monk_brewmaster, monk_mistweaver, monk_windwalker]
paladin = [paladin_holy, paladin_protection, paladin_retribution]
priest = [priest_discipline, priest_holy, priest_shadow]
rogue = [rogue_assassination, rogue_subtlety, rogue_outlaw]
shaman = [shaman_elemental, shaman_enhancement, shaman_restoration]
warlock = [warlock_affliction, warlock_demonology, warlock_destruction]
warrior = [warrior_arms, warrior_fury, warrior_protection]

#%%

spec_weapon_catagory = {}
for element in (monk):
    spec_weapon_catagory[element] = 'Monk'
for element in (demon_hunter):
    spec_weapon_catagory[element] = 'Dh'
for element in (evoker):
    spec_weapon_catagory[element] = 'Evoker'
for element in (mage):
    spec_weapon_catagory[element] = 'Mage'
for element in (priest):
    spec_weapon_catagory[element] = 'Priest'
for element in (warlock):
    spec_weapon_catagory[element] = 'Warlock'
spec_weapon_catagory[shaman_elemental] = 'Sham_Int'
spec_weapon_catagory[shaman_restoration] = 'Sham_Int'
spec_weapon_catagory[shaman_enhancement] = 'Sham_Agi'
spec_weapon_catagory[druid_balance] = 'Druid_Int'
spec_weapon_catagory[druid_restoration] = 'Druid_Int'
spec_weapon_catagory[druid_guardian] = 'Druid_Agi'
spec_weapon_catagory[druid_feral] = 'Druid_Agi'
spec_weapon_catagory[rogue_outlaw] = 'Outlaw'
spec_weapon_catagory[rogue_subtlety] = 'Stabby'
spec_weapon_catagory[rogue_assassination] = 'Stabby'
spec_weapon_catagory[death_knight_frost] = 'Dk_1h'
spec_weapon_catagory[death_knight_unholy] = 'Dk_2h'
spec_weapon_catagory[death_knight_blood] = 'Dk_2h'
spec_weapon_catagory[warrior_protection] = 'War_Prot'
spec_weapon_catagory[warrior_fury] = 'War_Fury'
spec_weapon_catagory[warrior_arms] = 'War_Arms'
spec_weapon_catagory[paladin_protection] = 'Pala_Prot'
spec_weapon_catagory[paladin_holy] = 'Pala_Holy'
spec_weapon_catagory[paladin_retribution] = 'Pala_Ret'
spec_weapon_catagory[hunter_beast_mastery] = 'Hunt_R'
spec_weapon_catagory[hunter_marksmanship] = 'Hunt_R'
spec_weapon_catagory[hunter_survival] = 'Hunt_M'

def get_weapon_proficiency(weapon_catagory, spec):
    translated_row_name = spec_weapon_catagory[spec]
    value = df.loc[translated_row_name, weapon_catagory]
    if str(value) == '0':
        return False
    elif str(value) == '1':
        return True
    else:
        assert(False)

assert(get_weapon_proficiency('Axe 2h', shaman_elemental))

def get_columns_with_ones(spec):
    translated_row_name = spec_weapon_catagory[spec]
    # Get the specified row as a Pandas Series
    row = df.loc[translated_row_name]

    # Find the column names where the row has a value of 1
    columns_with_ones = list(row[row == 1].index)

    return columns_with_ones

#%%

cloth = mage + priest + warlock
leather = demon_hunter + druid + monk + rogue
mail = evoker + hunter + shaman
plate = death_knight + paladin + warrior
assert(len(cloth + leather + mail + plate) == number_of_specs)

armor_types = {'cloth': cloth,
               'leather': leather,
               'mail': mail,
               'plate': plate}

#%%

strength = [paladin_protection,
            paladin_retribution] + death_knight + warrior
agility = [monk_brewmaster, monk_windwalker, shaman_enhancement,
           druid_feral, druid_guardian] + rogue + demon_hunter + hunter
intellect = [monk_mistweaver, shaman_elemental, shaman_restoration,
             druid_balance, druid_restoration,
             paladin_holy] + evoker + mage + priest + warlock
assert(len(strength + agility + intellect) == number_of_specs)

primary_stats = {'str': strength,
                 'agi': agility,
                 'int': intellect}

#%%

tank = [death_knight_blood, demon_hunter_vengeance, druid_guardian,
        monk_brewmaster, paladin_protection, warrior_protection]
healer = [druid_restoration, evoker_preservation, monk_mistweaver,
          paladin_holy, priest_discipline, priest_holy, shaman_restoration]
mdps = [death_knight_frost, death_knight_unholy, demon_hunter_havoc,
        druid_feral, monk_windwalker, hunter_survival, paladin_retribution,
        shaman_enhancement, warrior_arms, warrior_fury] + rogue
rdps = [druid_balance, hunter_beast_mastery, hunter_marksmanship,
        shaman_elemental, evoker_devastation, priest_shadow] + mage + warlock
assert(len(tank + healer + mdps + rdps) == number_of_specs)

roles = {'tank': tank,
        'healer': healer,
        'mdps': mdps,
        'rdps': rdps,
        'dps': mdps + rdps}


class WoWspec:

    def __init__(self, specname):

        self.specname = specname
        self.armor = WoWspec.get_armor(self)
        self.role = WoWspec.get_role(self)
        self.primary_stat = WoWspec.get_primary_stat(self)
        self.weapons = WoWspec.get_weapon_list(self)

    def get_armor(self):
        for armor_type in armor_types:
            for spec in armor_types[armor_type]:
                if spec == self.specname:
                    return armor_type
        print(self.specname)
        assert(False)

    def get_role(self):
        for role in roles:
            for spec in roles[role]:
                if spec == self.specname:
                    return role
        print(self.specname)
        assert(False)

    def get_primary_stat(self):
        for primary_stat in primary_stats:
            for spec in primary_stats[primary_stat]:
                if spec == self.specname:
                    return primary_stat
        print(self.specname)
        assert(False)

    def get_weapon_list(self):
        return get_columns_with_ones(self.specname)

    def print_info(self):
        print(f'Name of spec: {self.specname}')
        print(f'Armor type: {self.armor}')
        print(f'Primary stat: {self.primary_stat}')
        print(f'Role: {self.role}')
        print(f'List of weapons: {self.weapons}')
        print()

def initialize_spec_objects():
    l = []
    l.append(WoWspec('Blood Death Knight'))
    l.append(WoWspec('Frost Death Knight'))
    l.append(WoWspec('Unholy Death Knight'))
    l.append(WoWspec('Havoc Demon Hunter'))
    l.append(WoWspec('Vengeance Demon Hunter'))
    l.append(WoWspec('Balance Druid'))
    l.append(WoWspec('Feral Druid'))
    l.append(WoWspec('Guardian Druid'))
    l.append(WoWspec('Restoration Druid'))
    l.append(WoWspec('Devastation Evoker'))
    l.append(WoWspec('Preservation Evoker'))
    l.append(WoWspec('Beast Mastery Hunter'))
    l.append(WoWspec('Marksmanship Hunter'))
    l.append(WoWspec('Survival Hunter'))
    l.append(WoWspec('Arcane Mage'))
    l.append(WoWspec('Fire Mage'))
    l.append(WoWspec('Frost Mage'))
    l.append(WoWspec('Brewmaster Monk'))
    l.append(WoWspec('Mistweaver Monk'))
    l.append(WoWspec('Windwalker Monk'))
    l.append(WoWspec('Holy Paladin'))
    l.append(WoWspec('Protection Paladin'))
    l.append(WoWspec('Retribution Paladin'))
    l.append(WoWspec('Discipline Priest'))
    l.append(WoWspec('Holy Priest'))
    l.append(WoWspec('Shadow Priest'))
    l.append(WoWspec('Assassination Rogue'))
    l.append(WoWspec('Subtlety Rogue'))
    l.append(WoWspec('Outlaw Rogue'))
    l.append(WoWspec('Elemental Shaman'))
    l.append(WoWspec('Enhancement Shaman'))
    l.append(WoWspec('Restoration Shaman'))
    l.append(WoWspec('Affliction Warlock'))
    l.append(WoWspec('Demonology Warlock'))
    l.append(WoWspec('Destruction Warlock'))
    l.append(WoWspec('Arms Warrior'))
    l.append(WoWspec('Fury Warrior'))
    l.append(WoWspec('Protection Warrior'))
    #for instance in l:
    #    instance.print_info()
    return l


#print(f'Tanks: {tank}')
#print(f'Healers: {healer}')
#print(f'DPS: {rdps + mdps}')

specs = ['Blood Death Knight', 'Frost Death Knight', 'Unholy Death Knight',
         'Havoc Demon Hunter', 'Vengeance Demon Hunter',
         'Balance Druid', 'Feral Druid', 'Guardian Druid', 'Restoration Druid',
         'Devastation Evoker', 'Preservation Evoker',
         'Beast Mastery Hunter', 'Marksmanship Hunter', 'Survival Hunter',
         'Arcane Mage', 'Fire Mage', 'Frost Mage',
         'Brewmaster Monk', 'Mistweaver Monk', 'Windwalker Monk',
         'Holy Paladin', 'Protection Paladin', 'Retribution Paladin',
         'Discipline Priest', 'Holy Priest', 'Shadow Priest',
         'Assassination Rogue', 'Outlaw Rogue', 'Subtlety Rogue',
         'Elemental Shaman', 'Enhancement Shaman', 'Restoration Shaman',
         'Affliction Warlock', 'Demonology Warlock', 'Destruction Warlock',
         'Arms Warrior', 'Fury Warrior', 'Protection Warrior']
