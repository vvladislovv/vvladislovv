<img style="margin-top: 10px" src="./wallpaper.gif" width="100%" height="auto">

# Hi, my name is Elcheninov Vladislav!✌️

## 👀 A little bit about me:
#### I study and live in Moscow. I came to the IT field because of my interest in studying computers, as well as my curiosity about how various information systems work. I play the guitar and I like to learn something new, as well as create something with my own hands. I've created games in the past, and now I'm diving into writing web applications and developing websites.

# 🐍 If I describe myself in Python language:

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

## 👨🏼‍💻 My job statistics:
[![GitHub Stats](https://raw.githubusercontent.com/vvladislovv/StateUse/master/github_stats.svg)](https://github.com/vvladislovv/StateUse)

## 💭 Would you like to contact me? Here are my contacts:
[![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:vlad.yelcheninov@gmail.com)
[![Telegram Badge](https://img.shields.io/badge/-Vladislov-blue?style=flat&logo=Telegram&logoColor=white)](https://t.me/evkoch4kaa) 
[![Vk Badge](https://img.shields.io/badge/-vvlad_islovv-dodgerblue?style=flat&logo=VK&logoColor=#4B0082)](https://vk.com/vvlad_islovv)
[![YouTube Badge](https://img.shields.io/badge/-EvkaIT-red?style=flat&logo=YouTube&logoColor=#FF0000)](https://www.youtube.com/@EvkaIT)

## 💡 What I always work with:
<div>
  <img src="./icons/cursor.svg" title="Cursor" alt="" width="40" height="40"/>&nbsp;
  <img src="./icons/Docker.svg" title="Docker" alt="" width="40" height="40"/>
  <img src="./icons/MongoDB.svg" title="MongoDB" alt="" width="40" height="40"/>
  <img src="./icons/Insomnia.svg" title="Insomnia" alt="" width="40" height="40"/>
  <img src="./icons/Figma.svg" title="Figma" alt="" width="40" height="40"/>
</div>

## 🛰️ A little bit about my work:
```txt
TypeScript                 19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %
Vue.js                     7 hrs 24 mins   ████░░░░░░░░░░░░░░░░░░░░░   16.41 %
CSS                        4 hrs 31 mins   ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %
Python                     3 hrs 42 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %
Bash                       3 hrs 25 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %
```

<button onclick="toggleLanguage()">Toggle Language (RU/EN)</button>

<script>
function toggleLanguage() {
    const elements = document.querySelectorAll('h1, h2, h4');
    elements.forEach(el => {
        const currentText = el.textContent;
        if (currentText === getRussianText(el)) {
            el.textContent = getEnglishText(el);
        } else {
            el.textContent = getRussianText(el);
        }
    });
    
    const codeBlock = document.querySelector('pre code');
    if (codeBlock) {
        const lines = codeBlock.textContent.split('\n');
        const updatedLines = lines.map(line => {
            const enLine = getEnglishText(line);
            const ruLine = getRussianText(line);
            return line === enLine ? ruLine : enLine;
        });
        codeBlock.textContent = updatedLines.join('\n');
    }
}

function getEnglishText(text) {
    switch(text) {
        case 'Привет, меня зовут Ельченинов Владислав!✌️':
            return 'Hi, my name is Elcheninov Vladislav!✌️';
        case '👀 Немного обо мне:':
            return '👀 A little bit about me:';
        case 'Я учусь и живу в Москве. Я пришел в сферу IT из-за интереса к изучению компьютеров, а также из любопытства к тому, как работают различные информационные системы. Я играю на гитаре, люблю узнавать что-то новое и создавать что-то своими руками. Ранее я создавал игры, а теперь погружаюсь в разработку веб-приложений и создание сайтов.':
            return 'I study and live in Moscow. I came to the IT field because of my interest in studying computers, as well as my curiosity about how various information systems work. I play the guitar and I like to learn something new, as well as create something with my own hands. I\'ve created games in the past, and now I\'m diving into writing web applications and developing websites.';
        case '🐍 Если описать меня на языке Python:':
            return '🐍 If I describe myself in Python language:';
        case '👨🏼‍💻 Моя статистика работы:':
            return '👨🏼‍💻 My job statistics:';
        case '💭 Хотите связаться со мной? Вот мои контакты:':
            return '💭 Would you like to contact me? Here are my contacts:';
        case '💡 С чем я всегда работаю:':
            return '💡 What I always work with:';
        case '🛰️ Немного о моей работе:':
            return '🛰️ A little bit about my work:';
        case 'TypeScript                 19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %':
            return 'TypeScript                 19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %';
        case 'Vue.js                     7 hrs 24 mins   ████░░░░░░░░░░░░░░░░░░░░░   16.41 %':
            return 'Vue.js                     7 hrs 24 mins   ████░░░░░░░░░░░░░░░░░░░░░   16.41 %';
        case 'CSS                        4 hrs 31 mins   ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %':
            return 'CSS                        4 hrs 31 mins   ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %';
        case 'Python                     3 hrs 42 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %':
            return 'Python                     3 hrs 42 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %';
        case 'Bash                       3 hrs 25 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %':
            return 'Bash                       3 hrs 25 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %';
        default:
            return text;
    }
}

function getRussianText(text) {
    switch(text) {
        case 'Hi, my name is Elcheninov Vladislav!✌️':
            return 'Привет, меня зовут Ельченинов Владислав!✌️';
        case '👀 A little bit about me:':
            return '👀 Немного обо мне:';
        case 'I study and live in Moscow. I came to the IT field because of my interest in studying computers, as well as my curiosity about how various information systems work. I play the guitar and I like to learn something new, as well as create something with my own hands. I\'ve created games in the past, and now I\'m diving into writing web applications and developing websites.':
            return 'Я учусь и живу в Москве. Я пришел в сферу IT из-за интереса к изучению компьютеров, а также из любопытства к тому, как работают различные информационные системы. Я играю на гитаре, люблю узнавать что-то новое и создавать что-то своими руками. Ранее я создавал игры, а теперь погружаюсь в разработку веб-приложений и создание сайтов.';
        case '🐍 If I describe myself in Python language:':
            return '🐍 Если описать меня на языке Python:';
        case '👨🏼‍💻 My job statistics:':
            return '👨🏼‍💻 Моя статистика работы:';
        case '💭 Would you like to contact me? Here are my contacts:':
            return '💭 Хотите связаться со мной? Вот мои контакты:';
        case '💡 What I always work with:':
            return '💡 С чем я всегда работаю:';
        case '🛰️ A little bit about my work:':
            return '🛰️ Немного о моей работе:';
        case 'TypeScript                 19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %':
            return 'TypeScript                 19 hrs 34 mins  ███████████░░░░░░░░░░░░░░   43.40 %';
        case 'Vue.js                     7 hrs 24 mins   ████░░░░░░░░░░░░░░░░░░░░░   16.41 %':
            return 'Vue.js                     7 hrs 24 mins   ████░░░░░░░░░░░░░░░░░░░░░   16.41 %';
        case 'CSS                        4 hrs 31 mins   ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %':
            return 'CSS                        4 hrs 31 mins   ██▓░░░░░░░░░░░░░░░░░░░░░░   10.02 %';
        case 'Python                     3 hrs 42 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %':
            return 'Python                     3 hrs 42 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   08.21 %';
        case 'Bash                       3 hrs 25 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %':
            return 'Bash                       3 hrs 25 mins   ██░░░░░░░░░░░░░░░░░░░░░░░   07.60 %';
        default:
            return text;
    }
}
</script>
