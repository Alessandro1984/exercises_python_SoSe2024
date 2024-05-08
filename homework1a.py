import plotly.express as px
import pandas as pd
from plotly.offline import plot

def spar_funktion(AK, SR, r, lz):
    kapital = AK # Anfangskapital
    sparen = AK # Anfangskapital
    zinsen = 0 # Anfängliche Zinsen, also Null
    gesamt_kapital = []
    gesamt_zinsen = []
    gesamt_einzahlungen = []

    for k in range (1, lz + 1):
        # Zinsberechnung
        zinsen = zinsen + kapital * r
        # Einzahlungen
        sparen = sparen + SR
        # Gesamtkapital (nur um zu prüfen...)
        kapital = kapital * (1 + r) + SR
        # Werte in die jeweiligen leeren Listen hinzufügen
        gesamt_kapital.append(round(kapital, 2))
        gesamt_zinsen.append(round(zinsen, 2))
        gesamt_einzahlungen.append(round(sparen, 2))

    # Die Funktion gibt eine Liste mit drei Listen darin zurück
    return [gesamt_kapital, gesamt_einzahlungen, gesamt_zinsen]

ergebnisse = spar_funktion(AK = 10000, SR = 1000, r = 0.01, lz = 10)

# Zuerst erstellen wir ein Dictionary
d = {'Zeit': range(1, 11),
     'Zinsen': ergebnisse[2],
     'Einzahlungen': ergebnisse[1]}

# Dann speichern wir das Dictionary als Pandas Dataframe
df = pd.DataFrame(data=d)

# Zum Schluss erstellen wir das Balkendiagramm mit Plotly
fig = px.bar(df,
       x = "Zeit",
       y = ["Einzahlungen", "Zinsen"],
       labels = {"value": "Euro",
                 "Zeit": "Jahr",
                 "variable": "Kapital"},
       title = "Sparplan")

# Speichern und öffnen das Plotly-Diagramm als .html-Datei
plot(fig, filename='homework1a.html')
