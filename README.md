this is just a simple python interface to make running a game of assassins much simpler by tracking and saving all the relevant information for you.

yes, making this with objects would have been smarter.

no, I'm not going to change it.

also for this to work properly you need the file to be in a directory containing files named names.txt and numbers.txt, 
with names.txt having names stored in Firstname Lastname format, with each line having one name. The other file, numbers.txt,
must have 10 digit phone numbers with no decoration, just 0123456789, with the line they are on corresponding to the line of the name
of the person they belong to in names.txt. If you need to restart the assassins game for whatever reason, just delete the assassins.json file.

PLEASE NOTE THAT THIS WILL COMPLETELY AND IRRETRIEVABLY WIPE YOUR CURRENT PROGRESS. YOU HAVE BEEN WARNED.

if a command takes a tag input, that just means the first initial of the player and the last name of the palyer, all lowercase and with 
no spaces.
