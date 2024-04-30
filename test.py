import mystuff



loaded_array = mystuff.read_from_csv('highscore.csv')


print("\nGeladenes Array aus der CSV-Datei:")
for row in loaded_array:
    print(row)