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
            list_line =line.rstrip().split("|")
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

# print(all_names_by_hobby('villagers.csv'))    




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

    with open("villagers.csv") as file:
        file_content = file.readlines()

        for line in file_content:
            file_line = line.rsplit("|")
            all_data.append(tuple(file_line))    

    return all_data
# print(all_data("villagers.csv"))    


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
    villager_name = villager_name.lower()
    with open("villagers.csv") as file:
        file_content = file.readlines()

        for line in file_content:
            villager = line.lower().split("|")

            name_to_compare = villager[0]
            
            if name_to_compare == villager_name:
                return villager
   
    return None
# print(find_motto("villagers.csv", "Motto"))                    



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
    villagers_with_similar_personality = []
    villager_name = villager_name.lower()
    
    with open("villagers.csv") as file:
        file_content = file.readlines()

        for line in file_content:
            villager = line.lower().rsplit("|")

            if villager[0] == villager_name:
                personality_to_compare = villager[2]
                # print(personality_to_compare)             
                break

    with open("villagers.csv") as file2:
        file_content2 = file2.readlines()    

        for line2 in file_content2:
            villager2 = line2.lower().rsplit("|")            
            current_villager_personality = villager2[2]            

            if personality_to_compare == current_villager_personality:                
                villagers_with_similar_personality.append(villager2[0])
                        
        

    return set(villagers_with_similar_personality)


print(find_likeminded_villagers("villagers.csv", "Wendy"))        
