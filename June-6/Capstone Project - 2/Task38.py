import numpy as np
import pandas as pd
df=pd.read_csv("players.csv")
def player_analysis():
    print("\n================= PLAYER ANALYSIS =================")
    print(df.sort_values(by="runs", ascending=False).to_string(index=False))
    print("-" * 52)
    runs_array = df["runs"].to_numpy()
    print(f"Highest Score: {np.max(runs_array)}")
    print(f"Lowest Score:  {np.min(runs_array)}")
    print(f"Median Score:  {np.median(runs_array)}")
    print(f"Std Deviation: {np.std(runs_array):.2f}")

    # High/Low filter conditions
    print("\n-> Players with > 600 runs:")
    print(df[df["runs"] > 600][["player_name", "team", "runs"]].to_string(index=False))

    print("\n-> Players with < 500 runs:")
    print(df[df["runs"] < 500][["player_name", "team", "runs"]].to_string(index=False))


def team_analysis():
    print("\nTEAM ANALYSIS ")
    team_grouped = df.groupby("team").agg(
        Total_Runs=("runs", "sum"),
        Avg_Runs=("runs", "mean"),
        Squad_Size=("player_name", "count")
    )
    print(team_grouped)
    print("-" * 52)
    top_team = team_grouped["Total_Runs"].idxmax()
    top_runs = team_grouped["Total_Runs"].max()
    bottom_team = team_grouped["Total_Runs"].idxmin()
    bottom_runs = team_grouped["Total_Runs"].min()

    print(f"Highest Performing Team: '{top_team}' with {top_runs} runs.")
    print(f"Lowest Performing Team:  '{bottom_team}' with {bottom_runs} runs.")


def generate_team_summary(filename="team_summary.csv"):
    print("\n--- Generating Team Summary Reports ---")
    try:
        summary_df = df.groupby("team").agg(
            Total_Runs=("runs", "sum"),
            Average_Runs=("runs", "mean"),
            Player_Count=("name", "count")
        ).reset_index()
        summary_df["Average_Runs"] = summary_df["Average_Runs"].round(2)
        summary_df.columns = ["Team", "Total Runs", "Average Runs", "Player Count"]
        summary_df.to_csv(filename, index=False)
        print(f"[Success] has been generated perfectly.")
        report_txt_file = "cricket-report.txt"
        with open(report_txt_file, "w") as f:
            f.write(f"Total Players: {len(df)}\n")
            f.write(f"Total Runs: {df['runs'].sum()}\n")
            f.write(f"Average Runs: {df['runs'].mean()}\n")
            f.write(f"Top Team: {df.groupby('team')['runs'].sum().idxmax()}\n")
        print(f"[Success] Descriptive text report '{report_txt_file}' generated.")
    except Exception as e:
        pass
def boundary_analysis():
    print(" BOUNDARY ANALYSIS")
    idx_max_fours = df["fours"].idxmax()
    idx_max_sixes = df["sixes"].idxmax()

    print(f"Most Fours: {df.loc[idx_max_fours, 'player_name']} ({df.loc[idx_max_fours, 'fours']} fours)")
    print(f"Most Sixes: {df.loc[idx_max_sixes, 'player_name']} ({df.loc[idx_max_sixes, 'sixes']} sixes)")
    print("-" * 52)

    total_fours = df["fours"].sum()
    total_sixes = df["sixes"].sum()
    boundary_runs = (total_fours * 4) + (total_sixes * 6)

    print(f"Tournament Total Fours:     {total_fours}")
    print(f"Tournament Total Sixes:     {total_sixes}")
    print(f"Total Runs from Boundaries: {boundary_runs}")


def main_menu():
    while True:
        print("    CRICKET TOURNAMENT ANALYTICS  ")
        print("1. Player Analysis")
        print("2. Team Analysis")
        print("3. Boundary Analysis")
        print("4. Export Reports (Task 37)")
        print("5. Exit")

        choice = input("Select a menu option (1-5): ").strip()

        if choice == "1":
            player_analysis()
        elif choice == "2":
            team_analysis()
        elif choice == "3":
            boundary_analysis()
        elif choice == "4":
            generate_team_summary()
        elif choice == "5":
            print("\nExiting program gracefully. See you next tournament!")
            break
        else:
            print("\n[Invalid Selection] Please choose an integer between 1 and 5.")


if __name__ == "__main__":
    main_menu()