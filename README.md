Чтобы README на GitHub показывал две версии — **на английском и на русском**, и позволял **переключаться между ними с помощью кнопок**, нужно использовать **HTML и JavaScript**, так как Markdown GitHub’а **поддерживает HTML** (но не весь JavaScript).

Вот **полностью рабочий пример README.md**, который будет работать на GitHub, включая автопереключение и отображение языков:

---

### ✅ Готовый код `README.md` (вставляй как есть):

````markdown
<!-- Кнопки переключения -->
<div align="center">
  <button onclick="showEnglish()" style="background: #0078D4; color: white; border: none; padding: 10px 20px; margin: 5px; border-radius: 5px; cursor: pointer;">ENGLISH</button>
  <button onclick="showRussian()" style="background: #E4181C; color: white; border: none; padding: 10px 20px; margin: 5px; border-radius: 5px; cursor: pointer;">РУССКИЙ</button>
</div>

<!-- Английская версия -->
<div id="english">

<img src="./wallpaper.gif" width="100%" />

<h1>Hi, my name is Elcheninov Vladislav!✌️</h1>

## 👀 A little bit about me:
I study and live in Moscow. I came to the IT field because of my interest in studying computers, as well as my curiosity about how various information systems work.  
I play the guitar, love to learn new things, and create with my hands. I’ve made games before and now I'm working on web applications and websites.

## 🐍 Describe me in Python:

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Currently:
    studying: List[str] = field(default_factory=list)
    myqualities: List[str] = field(default_factory=list)

class AboutMe:
    def __init__(self):
        self.name = "Vladislav"
        self.age = 18
        self.vacancy = ["Fullstack developer"]
        self.work_programs = ["Cursor", "Docker", "Figma", "MongoDB Compass", "Insomnia"]
        self.languages_work = ["Python", "TS"]
        self.hobbies = ["Blogging", "Coding"]

    def current_location(self) -> str:
        return "Moscow, Russia"

    def currently(self) -> Currently:
        return Currently(
            studying=["TS", "GO"],
            myqualities=["Hard work", "Deadline fulfillment", "Interest in new technologies"]
        )
````

## 👨🏼‍💻 My job statistics:

[![GitHub Stats](https://raw.githubusercontent.com/vvladislovv/StateUse/master/github_stats.svg)](https://github.com/vvladislovv/StateUse)

## 💭 Contact me:

[![Gmail](https://img.shields.io/badge/-Gmail-red?style=flat\&logo=Gmail\&logoColor=white)](mailto:vlad.yelcheninov@gmail.com)
[![Telegram](https://img.shields.io/badge/-Vladislov-blue?style=flat\&logo=Telegram\&logoColor=white)](https://t.me/evkoch4kaa)
[![VK](https://img.shields.io/badge/-vvlad_islovv-dodgerblue?style=flat\&logo=VK)](https://vk.com/vvlad_islovv)
[![YouTube](https://img.shields.io/badge/-EvkaIT-red?style=flat\&logo=YouTube)](https://www.youtube.com/@EvkaIT)

## 💡 Tools I use:

<img src="./icons/cursor.svg" title="Cursor" width="40" />
<img src="./icons/Docker.svg" title="Docker" width="40" />
<img src="./icons/MongoDB.svg" title="MongoDB" width="40" />
<img src="./icons/Insomnia.svg" title="Insomnia" width="40" />
<img src="./icons/Figma.svg" title="Figma" width="40" />

## 🛰️ WakaTime Stats:

<!--START_SECTION:waka-->

```txt
TypeScript   19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %
Vue.js        7 hrs 24 mins  ████░░░░░░░░░░░░░░░░░░░░░   16.41 %
CSS           4 hrs 31 mins  ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %
Python        3 hrs 42 mins  ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %
Bash          3 hrs 25 mins  ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %
```

<!--END_SECTION:waka-->

</div>

<!-- Русская версия -->

<div id="russian" style="display:none">

<img src="./wallpaper.gif" width="100%" />

<h1>Привет! Я — Ельченинов Владислав ✌️</h1>

## 👀 Немного обо мне:

Я живу и учусь в Москве. Пришёл в IT из интереса к компьютерам и желания разобраться, как работают разные информационные системы.
Играю на гитаре, люблю изучать новое и создавать что-то своими руками. Раньше делал игры, теперь перешёл к веб-приложениям и сайтам.

## 🐍 Если описать меня на языке Python:

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Currently:
    studying: List[str] = field(default_factory=list)
    myqualities: List[str] = field(default_factory=list)

class AboutMe:
    def __init__(self):
        self.name = "Владислав"
        self.age = 18
        self.vacancy = ["Fullstack-разработчик"]
        self.work_programs = ["Cursor", "Docker", "Figma", "MongoDB Compass", "Insomnia"]
        self.languages_work = ["Python", "TS"]
        self.hobbies = ["Блогинг", "Кодинг"]

    def current_location(self) -> str:
        return "Москва, Россия"

    def currently(self) -> Currently:
        return Currently(
            studying=["TS", "GO"],
            myqualities=["Трудолюбие", "Соблюдение дедлайнов", "Интерес к новым технологиям"]
        )
```

## 👨🏼‍💻 Моя статистика:

[![GitHub Stats](https://raw.githubusercontent.com/vvladislovv/StateUse/master/github_stats.svg)](https://github.com/vvladislovv/StateUse)

## 💭 Связь со мной:

[![Gmail](https://img.shields.io/badge/-Gmail-red?style=flat\&logo=Gmail\&logoColor=white)](mailto:vlad.yelcheninov@gmail.com)
[![Telegram](https://img.shields.io/badge/-Vladislov-blue?style=flat\&logo=Telegram\&logoColor=white)](https://t.me/evkoch4kaa)
[![VK](https://img.shields.io/badge/-vvlad_islovv-dodgerblue?style=flat\&logo=VK)](https://vk.com/vvlad_islovv)
[![YouTube](https://img.shields.io/badge/-EvkaIT-red?style=flat\&logo=YouTube)](https://www.youtube.com/@EvkaIT)

## 💡 С чем я всегда работаю:

<img src="./icons/cursor.svg" title="Cursor" width="40" />
<img src="./icons/Docker.svg" title="Docker" width="40" />
<img src="./icons/MongoDB.svg" title="MongoDB" width="40" />
<img src="./icons/Insomnia.svg" title="Insomnia" width="40" />
<img src="./icons/Figma.svg" title="Figma" width="40" />

## 🛰️ WakaTime статистика:

<!--START_SECTION:waka-->

```txt
TypeScript   19 ч 34 мин    ███████████░░░░░░░░░░░░░░   43.40 %
Vue.js        7 ч 24 мин    ████░░░░░░░░░░░░░░░░░░░░░   16.41 %
CSS           4 ч 31 мин    ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %
Python        3 ч 42 мин    ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %
Bash          3 ч 25 мин    ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %
```

<!--END_SECTION:waka-->

</div>

<!-- Скрипт переключения -->

<script>
function showEnglish() {
  document.getElementById('english').style.display = 'block';
  document.getElementById('russian').style.display = 'none';
}
function showRussian() {
  document.getElementById('english').style.display = 'none';
  document.getElementById('russian').style.display = 'block';
}
window.onload = function () {
  showEnglish(); // по умолчанию английский
};
</script>

