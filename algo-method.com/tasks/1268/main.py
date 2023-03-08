from typing import List

teams = {
    "arurus": ["aruru", "erara", "ukuku", "usisi", "totoro"],
    "algos": ["dijkstra", "prim", "kruskal"],
    "ramdoms": ["fadj", "vuiawqpv", "qpcuvauavhjzcrb"],
    "keybords": ["qwerty", "yuiop", "asdf", "ghjkl"],
    "bocchi": ["hitori"],
}


def team_has_c(c: str, list_members: List[str]) -> bool:
    return any(c in name for name in list_members)


def all_teams_have_c(c: str, team_members: List[List[str]]) -> bool:
    return all(team_has_c(c, list_members) for list_members in team_members)


for c_num in range(ord("a"), ord("z") + 1):
    # "a" から "z" までの文字が順番に格納される
    c = chr(c_num)

    if all_teams_have_c(c, list(teams.values())):
        print(c)
