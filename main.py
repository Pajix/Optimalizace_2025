import pandas as pd
import openpyxl

# Načti data z Excel souboru
df = pd.read_excel('Zakaznici.xlsx')

# Prevedeme data na JSON formát
data_json = df.to_json(orient='records')

# Uložení dat do JSON souboru
with open('zakaznici.json', 'w', encoding='utf-8') as f:
    f.write(data_json)

print("Data byla úspěšně exportována do zakaznici.json")