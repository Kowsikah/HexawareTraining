#Read a csv file:
import csv
import pandas as pd
import numpy as np
with open("players.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
#count players
count=0
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        count+=1
print("Total number of players: ",count)

#highest score
highest_score=0
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[4])>highest_score:
            highest_score=int(row[4])
print("Highest score:",highest_score)

lowest_score=highest_score
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[4])<lowest_score:
            lowest_score=int(row[4])
print("Lowest score:",lowest_score)

total_score=0
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_score+=int(row[4])
print("Average score:",total_score/count)

print("Players whose score greater than 600")
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[4])>600:
            print(row)

print("Players whose score less than 500")
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[4])<500:
            print(row)

print("Players with team members count")
players_team=dict()
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if players_team.get(row[2]):
            players_team[row[2]]+=1
        else:
            players_team[row[2]]=1

for k,v in players_team.items():
    print(k,v)

print("runs by teams")
team_runs=dict()
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if team_runs.get(row[2]):
            team_runs[row[2]]+=int(row[4])
        else:
            team_runs[row[2]]=int(row[4])

for k,v in team_runs.items():
    print(k,v)

print("Find team with highest runs.")
highest_run=0
for k,v in team_runs.items():
    if v>highest_run:
        highest_run=v
for k,v in team_runs.items():
    if v==highest_run:
        print(k)

print("Teams with lowest run")
lowest_run=highest_run
for k,v in team_runs.items():
    if v<lowest_run:
        highest_run=v
for k,v in team_runs.items():
    if v==lowest_run:
        print(k)

print("Find player with most fours.")
most_fours=0
player_name_four=""
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[5])>most_fours:
            most_fours=int(row[5])
            player_name=row[1]
print(player_name)


print("Find player with most Sixs.")
most_sixs=0
player_name_sixs=""
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if int(row[6])>most_fours:
            most_sixs=int(row[6])
            player_name_sixs=row[1]
print(player_name)

#Calculate total fours hit in tournament.
total_fours=0
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_fours+=int(row[5])

print("Total fours:",total_fours)

total_sixs=0
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_fours+=int(row[6])

print("Total sixs:",total_sixs)

players=[]
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        players.append(row[1])
players.sort()
print(players)

teams=set()
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        teams.add(row[2])

print("Unique teams:",teams)

print(team_runs)

player_runs=dict()
with open("players.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        player_runs[row[2]]=int(row[4])

print(player_runs)

def find_top_score():
    highest_score=0
    highest_score_player=""
    with open("players.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if int(row[4])>highest_score:
                highest_score=int(row[4])
                highest_score_player=row[1]
    print(highest_score_player)

def calculate_average_run():
    total_runs=0
    count=0
    with open("players.csv","r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            total_runs+int(row[4])
            count+=1
    print(total_runs/count)

def find_best_team():
    for k,v in team_runs.items():
        if v==highest_run:
            print(k)

def find_total_boundaries():
    total_boundaries=0
    with open("players.csv","r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            total_boundaries+=int(row[5])

try:
    with open("players2.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")

try:
    with open("players1.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if int(row[3])<0:
                raise ValueError("Match count cannot be negative")
            if int(row[4])<0:
                raise ValueError("Runs cannot be negative")

except ValueError as e:
    print(e)

run_data=np.genfromtxt("players.csv",delimiter=",",dtype=None,names=True)
runs=run_data["runs"]
total_run=np.sum(runs)
average_runs=total_run/(len(run_data)-1)
maximum_runs=np.max(runs)
minimum_runs=np.min(runs)
standard_deviations=np.std(runs)
median=np.median(runs)

print("Total runs:",total_run)
print("Average runs:",average_runs)
print("Maximum runs:",maximum_runs)
print("Minimum runs:",minimum_runs)
print("Standard deviations:",standard_deviations)
print("Median runs:",median)

df=pd.read_csv("players.csv")
print(df.sort_values(by="runs",ascending=False).head())

print(df.sort_values(by="runs",ascending=False))

team_runs=df.groupby("team")["runs"].sum()
print(team_runs)

team_avg=df.groupby("team")["runs"].mean()
print(team_avg)

high_scorers = df[df['runs'] > 600]

print("--- Players with more than 600 runs ---")
print(high_scorers)
print("\n")

top_team = df.groupby('team')['runs'].sum().idxmax()
total_team_runs = df.groupby('team')['runs'].sum().max()

print("--- Top Team ---")
print(f"The top team is '{top_team}' with a total of {total_team_runs} runs.")

with open("players.csv","r") as f1:
  with open("cricket-report.txt","w") as f:
       f.write("Total Players:"+str(count))
       f.write("Total Runs:"+str(total_run))
       f.write("Average Runs:"+str(average_runs))
       f.write("Highest scorer:"+str(high_scorers))
       reader=csv.reader(f1)
       next(reader)
       for row in reader:
            if int(row[4])==lowest_score:
                print(row[1])
       f.write("Team wise runs")
       for team_name,run in team_runs.items():
            f.write(team_name+str(runs))
       f.write("Top 5 players")
       f.write(str(df.sort_values(by="runs",ascending=False).head(5)))
       f.write("Most fours:"+str(player_name_four))
       f.write("Most sixs:"+str(player_name_sixs))


with open("topplayer.csv","w") as f:
    top_player=df[df["runs"]>600]
    f.write(str(top_player))

summary_df = df.groupby("team").agg(
    Total_Runs=("runs", "sum"),
    Average_Runs=("runs", "mean"),
    Player_Count=("player_name", "count")
).reset_index()

# Round average runs to 2 decimal places
summary_df["Average_Runs"] = summary_df["Average_Runs"].round(2)

# Rename columns to match target format
summary_df.columns = ["Team", "Total Runs", "Average Runs", "Player Count"]

# Save to CSV
summary_df.to_csv("cricket-summary.csv", index=False)
print(f"[Success] '{'cricketsummary'}' has been generated perfectly.")

