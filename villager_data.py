"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    with open('villagers.csv') as file:
        contents = file.readlines()

        for line in contents:
            list_line =line.rsplit("|")
            species.add(list_line[1])
    return species     
  
# print(all_species('villagers.csv'))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    with open('villagers.csv') as file:
        file_lines = file.readlines()

        for line in file_lines:
            list_line = line.rsplit("|")
            if search_string == list_line[1]:
                villagers.append(list_line[0])
            else:
                villagers.append(list_line[0])    

    return sorted(villagers)
# print(get_villagers_by_species('villagers.csv', "Bear"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

   
    with open('villagers.csv') as file:
        file_content = file.readlines()

        for line in file_content:
            lines_file = line.rsplit("|")
            hobby = lines_file[3]
            name = lines_file[0]


            if hobby == "Fitness":
                fitness.append(name)
            elif hobby == "Nature":
                nature.append(name) 
            elif hobby == "Education":
                education.append(name) 
            elif hobby == "Music":
                music.append(name) 
            elif hobby == "Fashion":
                fashion.append(name) 
            elif hobby == "Play":
                play.append(name)     

    villagers_group_by_hobby = [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]                         
       
    return villagers_group_by_hobby

print(all_names_by_hobby('villagers.csv'))    




def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
