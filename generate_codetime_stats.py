import os
import requests

CODETIME_API_KEY = os.getenv("CODETIME_API_KEY")
GH_TOKEN = os.getenv("GH_TOKEN")

headers = {"Authorization": f"Bearer {CODETIME_API_KEY}"}

# Получение данных из CodeTime API
try:
    response = requests.get("https://api.codetime.dev/v1/stats", headers=headers)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"Ошибка: {e}")
    exit(1)

# Генерация таблицы
stats_table = "### 🕒 CodeTime Stats\n"
stats_table += "| Язык | Время |\n|-------|-------|\n"
for lang in data.get("languages", []):
    stats_table += f"| {lang['name']} | {lang['time']} |\n"

# Обновление README.md
with open("README.md", "r+") as f:
    content = f.read()
    start = content.find("<!--START_SECTION:codetime-->")
    end = content.find("<!--END_SECTION:codetime-->") + len("<!--END_SECTION:codetime-->")
    
    if start == -1 or end == -1:
        print("Метки не найдены в README.md!")
        exit(1)
    
    new_content = content[:start] + f"<!--START_SECTION:codetime-->\n{stats_table}\n" + content[end:]
    f.seek(0)
    f.write(new_content)
    f.truncate()
