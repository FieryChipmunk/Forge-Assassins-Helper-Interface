import random
import json
import os
from datetime import date, datetime

def create_list(names, numbers):
    
    player_list = []
    
    for name in names:
        
        player_list.append([None]*4)
        player_list[names.index(name)][0] = name
        split_name = name.split();
        player_list[names.index(name)][1] = (split_name[0][0] + split_name[1]).lower()
        player_list[names.index(name)][2] = numbers[names.index(name)]
        player_list[names.index(name)][3] = True

        
    random.shuffle(player_list)
    
    for player in player_list:
        
        if player_list.index(player)+1 == len(player_list):
        
            player.append(0)
            
        else:
            
            player.append(player_list.index(player)+1)
            
        player.append(str(date.today()))
    
    return player_list

def eliminate_player(player_list, player_tag):
    
    player_to_eliminate = None

    for player in player_list:
        
        if player[1] == player_tag:
            
            player_to_eliminate = player
            break
        
    if player_to_eliminate and player_to_eliminate[3] == True:
        
        player_to_eliminate[3] = False
        previous_hunter = None
        for player in player_list:
            
            if player[4] == player_list.index(player_to_eliminate):
                
                previous_hunter = player
                break

        if previous_hunter:
            
            previous_hunter[4] = player_to_eliminate[4]
            previous_hunter[5] = str(date.today())
            print(player_to_eliminate[0] + " has been eliminated, " + previous_hunter[0] + " is now hunting " + player_list[previous_hunter[3]][0] + "\n")
    
        else:
            
            print("Could not find hunter\n")
        
    else:
        
        print("Could not locate find to eliminate\n")
        
def display_list(player_list):
    
    print(str(player_list) + "\n")
    
def show_alive(player_list):
    
    living = 0
    alive_list = [];
    
    for player in player_list:
        
        if player[3] == True:
            
            living += 1
            
            alive_list.append((player[0]))
            
    print("There are " + str(living) + " players alive")
            
    for alive in alive_list:
        
        print(alive)
            
    print("\n")
    
def show_dead(player_list):
    
    deceased = 0
    dead_list = [];
    
    for player in player_list:
        
        if player[3] == False:
            
            deceased += 1
            
            dead_list.append((player[0]))
            
    print("There are " + str(deceased) + " players dead")
            
    for dead in dead_list:
        
        print(dead)
            
    print("\n")
    
def player_status(player_list, query, is_tag):
    
    player_to_show_status = None
    if is_tag:
        
        for player in player_list:
        
            if player[1].lower() == query:
            
                player_to_show_status = player
                break
    else:
        
        for player in player_list:
        
            if player[0].lower() == query:
            
                player_to_show_status = player
                break
        
    print("Name: " + player_to_show_status[0])
    print("Phone Number: " + player_to_show_status[2][:3] + "-" + player_to_show_status[2][3:6] + "-" + player_to_show_status[2][6:])

    if player_to_show_status:
        
        if player_to_show_status[3] == False:
    
            print(player_to_show_status[0] + " was eliminated\n")
            
        else:
            
            hunting_player = None
            for player in player_list:
                
                if player[4] == player_list.index(player_to_show_status) and player[3] == True:
                    
                    hunting_player = player
                    break
            
            print("Hunting: " + player_list[player_to_show_status[4]][0])
            print("Hunted by: " + hunting_player[0])
            print("Last kill was on " + player_to_show_status[5] + "\n")
        
    else:
        
        print("Could not find player\n")
        
def check_player_deadlines(player_list):
    
    players_over_deadline = []

    for player in player_list:
        
        player_date = datetime.strptime(player[5], '%Y-%m-%d').date()
        delta = date.today() - player_date
        
        if delta.days > 0:
            
            if player[3] == True:
            
                players_over_deadline.append(player[0])
                
    if (len(players_over_deadline) > 0):
        
        print("Players over deadline:\n")
            
        for player in players_over_deadline:
        
            print(player)
            
    else:
        
        print("No players are currently over the deadline")
        
    print("\n")
        
        
new_list = []
        
if os.path.isfile("assassins.json"):
    
    f = open('assassins.json')
    new_list = json.load(f)
    f.close()
    
else:
    
    f1 = open("assassins.json", "x")
    f1.close()
    if os.path.isfile("names.txt"):
        
        f2 = open("names.txt")
        
    else:

        f2 = open("names.txt", "x")
        
    if os.path.isfile("numbers.txt"):
        
        f3 = open("numbers.txt")
        
    else:

        f3 = open("numbers.txt", "x")
    
    lines = f2.read().split("\n")
    pns = f3.read().split("\n")
    
    list_from_text = []
    list_from_numbers = []
    
    for line in lines:
        
        list_from_text.append(line)
        
    for number in pns:
        
        list_from_numbers.append(str(number))
        
    new_list = create_list(list_from_text, list_from_numbers)
    f2.close()
    f3.close()
    
running = True

print("Welcome to the Forge Assassins Helper Interface\n")
print("Possible commands:")
print("eliminate (playertag)")
print("displaylist")
print("showalive")
print("showdead")
print("status (playertag)")
print("deadlines")
print("quit\n")

while running:
    
    u_input = input("Input command:\n")
    u_input = u_input.split()
    print("\n")
    if u_input[0] == "eliminate":
        eliminate_player(new_list, u_input[1])
            
    elif u_input[0] == "displaylist":
        display_list(new_list)
            
    elif u_input[0] == "showalive":
        show_alive(new_list)
            
    elif u_input[0] == "showdead":
        show_dead(new_list)
                      
    elif u_input[0] == "status":
        
        if len(u_input) == 3:
            
            player_status(new_list, (u_input[1] + " " + u_input[2]).lower(), False)
            
        else:
            
            player_status(new_list, u_input[1].lower(), True)
            
    elif u_input[0] == "deadlines":
        check_player_deadlines(new_list)
       
    elif u_input[0] == "quit":
        running = False
        print("Quitting...")
            
    else:
        print("Unknown command")
        

    with open("assassins.json", "w") as outfile:
        json.dump(new_list, outfile)
    
        outfile.close()
        
os.system("PAUSE")