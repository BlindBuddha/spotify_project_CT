# Week 2 - Genres - Yunus Turer #


# Making variables to store data

fields = []
rows = []

pop = []
rock = []
techno = []

# Import and opening CSV with data
import csv

with open('spotify-dataset.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
    for row in csvreader:
        
        
        # Going through all songs in CSV file if certain words are in the genre, then record name in respective var
        # First pop, only need one if statement since pop is a large genre
        if "pop" in row[2]:
            pop.append(row[0])
            
        # Next rock and band for rock songs
        if "rock" in row[2]:
            rock.append(row[0])
        if "band" in row[2]:
            rock.append(row[0])
            
        # Lastly techno and electr for techno songs
        if "techno" in row[2]:
            techno.append(row[0])
        if "electr" in row[2]:
            techno.append(row[0])

users = {}
with open('users_database.txt') as txtfile:
    for line in txtfile:
        ######### WHAT TO PUT HERE? ############
        # Having trouble with putting the users_database.txt
        # into a python dictionary... currently stuck on this
        
        
        
        

# List of users and songs that they have listened to prior to week 2


# There are only 3 types of categories for music
# Rock
# Pop
# Techno
# Assigning every song to one of these, else N/A

