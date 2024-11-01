# Data enligt uppgiften
data = {
    "studenter": [
        ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
        ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
        ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
        ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
        ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv": True}),
    ],
    "kurser": {
        "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
        "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
        "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
    }
}

# 1. Extrahera en tuple med namn på alla aktiva studenter
aktiva_studenter = tuple(student[0] for student in data["studenter"] if student[1]["aktiv"])
print("Aktiva studenter:", aktiva_studenter)

# 2. Skapa ett set med alla unika ämnen som de aktiva studenterna studerar
aktiva_ämnen = {ämne for student in data["studenter"] if student[1]["aktiv"] for ämne in student[1]["ämnen"]}
print("Unika ämnen för aktiva studenter:", aktiva_ämnen)

# 3. Skapa en ordbok där nycklarna är kursnamnen och värdena är antalet aktiva studenter som är inskrivna i respektive kurs
aktiva_kurser = {kurs: len(data["kurser"][kurs]["studenter"].intersection(aktiva_studenter)) for kurs in data["kurser"]}
print("Antal aktiva studenter per kurs:", aktiva_kurser)


