# EasyInit
A tool for Tabletop GMs to more easily determine initiative orders in encounters with multiple copies of an enemy.

## Usage
There are two ways to use this script.

The first way is to run the script with no command line options specified, have your players roll for initiative as normal. When prompted, type in their names and the results of their rolls (after applying any bonuses).
Once all players have been entered in, press Enter at the prompt.

The second is to store each player's name and their initiative bonus in a file, one player per line, in this format:

`Player Name,Bonus`

Then run the script with the `--file, -f` option and the name of this file. The script will automatically roll a d20 for initiative for each player and apply their bonus.

Now, enter the names of the enemy you want to add to your encounter, for example 'Guard' or 'Bandit', their initiative bonus, and their quantity.
The script will automatically roll a d20 for initiative for each one of the enemies, then display a list, sorted in descending order, of each character and their initiatives.
