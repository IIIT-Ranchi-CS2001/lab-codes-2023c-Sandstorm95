singers = {"Ram", "Sonu", "Arjit", "Pankaj", "Master"}
dancers = {"Prabhu", "Master", "Teren", "Arjit", "Pankaj"}

all_artist = singers | dancers
print(f"Artists ", all_artist)

allrounder = singers & dancers
print(f"All rounder ", allrounder)

onlydancers = all_artist - singers
print(f"Dancers but not singers ", onlydancers)



