import csv

from plotly import offline

filename = "./data/nswl_season_25_data.csv"
with open(filename) as f:
    read_csv = csv.reader(f)
    table_row = next(read_csv)

    # Get teams and total goals scored per team
    teams, goals_scored = [], []
    for row in read_csv:
        teams.append(row[0])
        goals_scored.append(int(row[1]))

    # Visual data
    data = [{"type": "bar", "x": teams, "y": goals_scored}]
    layout = {
        "title": {
            "text": "Goals Scored Per Each Team",
            "font": {"size": 24},
            "x": 0.5,
        },
        "xaxis": {"title": {"text": "Teams", "font": {"size": 16}}},
        "yaxis": {"title": {"text": "Goals", "font": {"size": 16}}},
    }
    fig = {"data": data, "layout": layout}

    offline.plot(fig, filename="goals_scored_per_team.html")
