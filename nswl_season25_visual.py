import csv

from plotly import offline

team_colors = {
    "Angel City FC": "#F1B1A5",
    "Chicago Stars": "#3AB5E8",
    "Houston Dash": "#FF6900",
    "Kansas City Current": "#CF3339",
    "Gotham FC": "#A9F1FD",
    "NC Courage": "#AB0033",
    "Reign": "#292431",
    "Orlando Pride": "#61259E",
    "Portland Thorns": "#99242B",
    "Racing Louisville": "#C5B5F2",
    "San Diego Wave": "#032E62",
    "Washington Spirit": "#000000",
    "Royals": "#0E1735",
    "Bay FC": "#0D2032",
}

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
    colors = [team_colors.get(team, "#888888") for team in teams]
    data = [
        {
            "type": "bar",
            "x": teams,
            "y": goals_scored,
            "marker": {"color": colors, "line": {"color": "black", "width": 1}},
        }
    ]
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
