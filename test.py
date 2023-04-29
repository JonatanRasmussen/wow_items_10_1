input = '''
Death Knight
Death Knight

Blood


Frost


Unholy

Demon Hunter
Demon Hunter

Havoc


Vengeance

Druid
Druid

Balance


Feral


Guardian


Restoration1

Evoker
Evoker

Devastation


Preservation

Hunter
Hunter

Beast Mastery


Marksmanship


Survival

Mage
Mage

Arcane


Fire


Frost1

Monk
Monk

Brewmaster


Mistweaver


Windwalker

Paladin
Paladin

Holy1


Protection1


Retribution

Priest
Priest

Discipline


Holy


Shadow

Rogue
Rogue

Assassination


Outlaw


Subtlety

Shaman
Shaman

Elemental


Enhancement


Restoration

Warlock
Warlock

Affliction


Demonology


Destruction

Warrior
Warrior

Arms


Fury


Protection
'''

specs = set()
classes = set()


for line in input.split('\n'):
    line = line.strip()
    if line:
        if line in specs:
            classes.add(line)
        else:
            specs.add(line)

specs.difference_update(classes)

print(classes)
print(specs)

def process_string(my_string, set_class, set_spec):
    my_list = []
    name_of_class = ''
    name_of_spec = ''
    for line in my_string.split("\n"):
        if line.strip() in set_class:
            name_of_class = line.strip()
        elif line.strip() in set_spec:
            name_of_spec = line.strip()
            name_of_spec = name_of_spec.replace('1', '')
            my_list.append(f'{name_of_spec} {name_of_class}')
    return my_list

lst = process_string(input, classes, specs)
print(lst)
