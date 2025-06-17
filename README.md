Вот обновлённая версия вашего профиля с кнопкой перевода на русский и переведённым текстом:

```html
<img style="margin-top: 10px" src="./wallpaper.gif" width="100%" height: auto>

<div style="text-align: right; margin-bottom: 10px;">
  <button onclick="toggleLanguage()">Перевести на русский / English</button>
</div>

<h1 id="title"> Hi, my name is Elcheninov Vladislav!✌️</h1>
<h2 id="about-title">👀 A little bit about me:</h2>
<h4 id="about-text">I study and live in Moscow. I came to the IT field because of my interest in studying computers, as well as my curiosity about how various information systems work. I play the guitar and I like to learn something new, as well as create something with my own hands. I've created games in the past, and now I'm diving into writing web applications and developing websites.</h4>

<h1 id="python-title"> 🐍 if me describe me in Python language:</h1>

```Python
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
        self.work_programs = ["Cursor", "Docker", "Figma", "MongoDB Compass", "Insomnia",]
        self.languages_work = ["Python", "TS"]
        self.hobbies = ["Blogging", "Coding"]

    def current_location(self) -> str:
        return "Moscow, Russia"

    def currently(self) -> Currently:
        return Currently(
            studying=["TS", "GO"],
            myqualities=["Hard work", "Deadline fulfillment", "Interest in new technologies"]
        )

```

<h2 id="stats-title">👨🏼‍💻 My job statistics: </h2>

[![GitHub Stats](https://raw.githubusercontent.com/vvladislovv/StateUse/master/github_stats.svg)](https://github.com/vvladislovv/StateUse)

<h2 id="contacts-title">💭 Would you like to contact me here are my contacts: </h2>

[![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:vlad.yelcheninov@gmail.com)
[![Telegram Badge](https://img.shields.io/badge/-Vladislov-blue?style=flat&logo=Telegram&logoColor=white)](https://t.me/evkoch4kaa) 
[![Vk Badge](https://img.shields.io/badge/-vvlad_islovv-dodgerblue?style=flat&logo=VK&logoColor=#4B0082)](https://vk.com/vvlad_islovv)
[![YouTube Badge](https://img.shields.io/badge/-EvkaIT-red?style=flat&logo=YouTube&logoColor=#FF0000)](https://www.youtube.com/@EvkaIT)

<h2 id="tools-title">💡 What I always work with:</h2>
<div>
  <img src="./icons/cursor.svg" title="Cursor" alt="" width="40" height="40"/>&nbsp;
  <img src="./icons/Docker.svg" title="Docker" alt="" width="40" height="40"/>
  <img src="./icons/MongoDB.svg" title="MongoDB" alt="" width="40" height="40"/>
  <img src="./icons/Insomnia.svg" title="Insomnia" alt="" width="40" height="40"/>
  <img src="./icons/Figma.svg" title="Figma" alt="" width="40" height="40"/>
</div>

<h2 id="work-title"> 🛰️ A little bit about my work: </h2>

<!--START_SECTION:waka-->

```txt
TypeScript                 19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %
Vue.js                     7 hrs 24 mins   ████░░░░░░░░░░░░░░░░░░░░░   16.41 %
CSS                        4 hrs 31 mins   ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %
Python                     3 hrs 42 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %
Bash                       3 hrs 25 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %
```

<!--END_SECTION:waka-->

<script>
  let isRussian = false;
  
  const translations = {
    "title": ["Привет, меня зовут Ельченинов Владислав!✌️", "Hi, my name is Elcheninov Vladislav!✌️"],
    "about-title": ["👀 Немного обо мне:", "👀 A little bit about me:"],
    "about-text": [
      "Я учусь и живу в Москве. Пришёл в IT-сферу из-за интереса к изучению компьютеров, а также из-за любопытства о том, как работают различные информационные системы. Играю на гитаре и люблю узнавать что-то новое, а также создавать что-то своими руками. Раньше создавал игры, а сейчас погружаюсь в написание веб-приложений и разработку сайтов.",
      "I study and live in Moscow. I came to the IT field because of my interest in studying computers, as well as my curiosity about how various information systems work. I play the guitar and I like to learn something new, as well as create something with my own hands. I've created games in the past, and now I'm diving into writing web applications and developing websites."
    ],
    "python-title": ["🐍 если бы я описывал себя на Python:", "🐍 if me describe me in Python language:"],
    "stats-title": ["👨🏼‍💻 Моя статистика работы:", "👨🏼‍💻 My job statistics:"],
    "contacts-title": ["💭 Хотите связаться? Вот мои контакты:", "💭 Would you like to contact me here are my contacts:"],
    "tools-title": ["💡 С чем я постоянно работаю:", "💡 What I always work with:"],
    "work-title": ["🛰️ Немного о моей работе:", "🛰️ A little bit about my work:"]
  };

  function toggleLanguage() {
    isRussian = !isRussian;
    updateText();
  }

  function updateText() {
    for (const [id, texts] of Object.entries(translations)) {
      const element = document.getElementById(id);
      if (element) {
        element.textContent = isRussian ? texts[0] : texts[1];
      }
    }
    
    const button = document.querySelector('button');
    if (button) {
      button.textContent = isRussian ? 'English version' : 'Перевести на русский';
    }
  }
</script>
```

Этот код добавляет:
1. Кнопку перевода в правом верхнем углу
2. Функцию перевода между английским и русским
3. Все текстовые элементы теперь имеют ID для перевода
4. JavaScript-логику для переключения языка

Особенности:
- При нажатии кнопки все тексты меняются на русский и обратно
- Кнопка сама меняет текст в зависимости от текущего языка
- Технические части (код Python, статистика) остаются без изменений
- Контакты (иконки соцсетей) также остаются без изменений

Вы можете настроить переводы, редактируя объект `translations` в JavaScript-коде.
