def create_journey_note(date:str, team_a:str, team_b:str, ranked:bool):
    new_journey = {
        "date": date,
        "team_a": team_a,
        "team_b": team_b,
        "gol_a": 0,
        "gol_b": 0,
        "ranked": ranked
    }
    return new_journey

def set_gol(jorney:dict, team_name:str, gol_number:int):
    new_jorney = jorney
    if team_name == jorney.get("team_a"):
        new_jorney["gol_a"] = gol_number
    if team_name == jorney.get("team_b"):
        new_jorney["gol_b"] = gol_number
    return new_jorney

def show_journey(jorney:dict):
    print(jorney)

other_jounery = create_journey_note("12/12/2026", "barcelona", "madrid", False)
show_journey(other_jounery)
other_jounery = set_gol(other_jounery, "barcelona", 2)
show_journey(other_jounery)