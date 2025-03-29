импорт requests
импорт ТЫ

# Получение API-ключа из секретов
CODETIME_API_KEY = OS.хотеть("CODETIME_API_KEY")
заголовки = {"Авторизация": F "носитель {CODETIME_API_KEY}"}

# Запрос к API CodeTime для получения статистики
Ответ = запросы.ПОЛУЧАТЬ("https://api.codetime.com/v1/stats", Заголовки = заголовки)
данные = ответ.JSON()

# Формирование Markdown-таблицы для README.md
stats_md = "| Язык | Время |\n|-------|-------|\n"
Для ланг в data["Языки"]:
    stats_md += фон"| {Просто ['name']} | {Просто ['Time']} | \ n"

# Обновление README.md с данными CodeTime
С открыть("README.md", "р+") как фон:
    Содержание = f.читать()
    start_marker = "<!--Start_section: Codetime-->"
    End_marker = "<!--End_section: Codetime-->"
    start_idx = content.находить(start_marker) + Лен(start_marker)
    end_idx = контент.находить(End_marker)
    updated_content = content[:start_idx] + "\не" + stats_md + "\не" + содержание[end_idx:]
    фон.искать(0)
    фон.Писать(updated_content)
    фон.входить()
