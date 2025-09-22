import random
import numpy as np
import pandas as pd

def round_robin_schedule(team_names):
    names = list(team_names)
    if len(names) % 2 == 1:
        names.append(None)
    n = len(names)
    rounds = []
    for r in range(n - 1):
        pairs = []
        for i in range(n // 2):
            t1, t2 = names[i], names[n - 1 - i]
            if t1 and t2:
                pairs.append((t1, t2))
        rounds.append(pairs)
        names = [names[0]] + [names[-1]] + names[1:-1]
    return rounds

def play_match(home, away, home_adv=0.12):
    ovr_h, ovr_a = home["OVR"], away["OVR"]
    base = 1.15
    mean_h = base + (ovr_h - 75) / 50 + home_adv
    mean_a = base + (ovr_a - 75) / 50
    mean_h, mean_a = max(0.2, mean_h), max(0.2, mean_a)
    goals_h = np.random.poisson(mean_h)
    goals_a = np.random.poisson(mean_a)

    home["MP"] += 1; away["MP"] += 1
    home["GF"] += goals_h; home["GA"] += goals_a
    away["GF"] += goals_a; away["GA"] += goals_h

    if goals_h > goals_a:
        home["W"] += 1; home["Pts"] += 3; away["L"] += 1
    elif goals_a > goals_h:
        away["W"] += 1; away["Pts"] += 3; home["L"] += 1
    else:
        home["D"] += 1; away["D"] += 1
        home["Pts"] += 1; away["Pts"] += 1

    return goals_h, goals_a

def simulate_season(teams_dict):
    team_names = list(teams_dict.keys())
    first_leg = round_robin_schedule(team_names)
    second_leg = [[(b, a) for (a, b) in r] for r in first_leg]
    full_rounds = first_leg + second_leg

    match_history = []
    for round_no, matches in enumerate(full_rounds, 1):
        for home, away in matches:
            gh, ga = play_match(teams_dict[home], teams_dict[away])
            match_history.append({
                "Matchday": round_no,
                "Home": home, "Away": away, "HG": gh, "AG": ga
            })
    return match_history

def final_table(teams_dict):
    rows = []
    for t in teams_dict.values():
        rows.append({
            "Team": t["name"], "MP": t["MP"], "W": t["W"], "D": t["D"], "L": t["L"],
            "GF": t["GF"], "GA": t["GA"], "GD": t["GF"] - t["GA"], "Pts": t["Pts"], "OVR": t["OVR"]
        })
    df = pd.DataFrame(rows)
    df = df.sort_values(by=["Pts", "GD", "GF", "OVR"], ascending=[False, False, False, False]).reset_index(drop=True)
    return df.drop(columns=["OVR"]), df
