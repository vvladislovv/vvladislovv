импорт requests
импорт os
импорт re

# Получение секретов
CODETIME_API_KEY = OS.хотеть("CODETIME_API_KEY")
gh_token = os.хотеть("Gh_token")

# Параметр API -Time
заголовки = {
    "Авторизация": F "носитель {CODETIME_API_KEY}",
    "Контент-тип": "Приложение/JSON"
}

# Запрос к API CodeTime
Пытаться:
    Ответ = запросы.ПОЛУЧАТЬ("https://api.codetime.com/v1/stats", Заголовки = заголовки)
    Ответ.Raise_for_status()
    данные = ответ.JSON()
кроме запросы.Исключения.RequestException как Эн:
    печать(f"Ошибка API: {Эн}")
    exit(1)

# Формирование Markdown-таблицы
stats_md = "| Язык | Время |\n|-------|-------|\n"
Для lang в данные.ПОЛУЧАТЬ("Языки", []):
    stats_md += фон"| {lang.get ('name', 'неизвестно')} | {lang.get ('time', '0')} | \ n"

# Обновление readme.md
С открыть("README.md", "р+") как фон:
    Содержание = f.читать()
    start_marker = "<!--Start_section: Codetime-->"
    End_marker = "<!--End_section: Codetime-->"
    
    Если start_marker нет в содержание или End_marker нет в содержание:
        печать("Метки не найдены в README.md")
        Выход(1)

    start_idx = content.находить(start_marker) + Лен(start_marker)
    end_idx = контент.находить(End_marker)
    updated_content = content[:start_idx] + "\не" + stats_md + "\не" + содержание[end_idx:]
    
    фон.искать(0)
    фон.Писать(updated_content)
    фон.входить()
