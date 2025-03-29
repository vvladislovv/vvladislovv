
<h1> Hi, my name is Vladislav!✌️</h1>

<img  style="margin-top: 10px" src="https://cs13.pikabu.ru/post_img/2024/06/23/10/1719161244164571834.jpg" width="100%" height: auto>



<h2>
    🎓I'm a coding programmer who learns new skills every day. I wrote my first code at the age of 18<img src="https://media.giphy.com/media/bGgsc5mWoryfgKBx1u/giphy.gif" width="25px">, and since then, everything has evolved. I enjoy taking on new and interesting challenges and often approach them with unconventional solutions. I've taken courses in programming, but I prefer self-learning<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2RxanpkMmowdWw3OXpzcWl1ZzhjbzB0M2huaDc4aDBzc2lxcXJ6ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MT5UUV1d4CXE2A37Dg/giphy.gif" width="25px">.
</h2>

<h4>
 💭I'm ready to take on an interesting project. If you are interested in my GitHub and my projects, please contact me. 
</h4>
<!--[![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:vlad.yelcheninov@gmail.com)-->

<!--START_SECTION:waka-->
![Code Time](http://img.shields.io/badge/Code%20Time-78%20hrs%2021%20mins-blue)

![Profile Views](http://img.shields.io/badge/Profile%20Views-143-blue)

**🐱 My GitHub Data** 

> 📦 ? Used in GitHub's Storage 
 > 
> 🏆 107 Contributions in the Year 2025
 > 
> 🚫 Not Opted to Hire
 > 
> 📜 30 Public Repositories 
 > 
> 🔑 0 Private Repositories 
 > 
**I'm an Early 🐤** 

```text
🌞 Morning                18 commits          █░░░░░░░░░░░░░░░░░░░░░░░░   02.21 % 
🌆 Daytime                392 commits         ████████████░░░░░░░░░░░░░   48.22 % 
🌃 Evening                272 commits         ████████░░░░░░░░░░░░░░░░░   33.46 % 
🌙 Night                  131 commits         ████░░░░░░░░░░░░░░░░░░░░░   16.11 % 
```
📅 **I'm Most Productive on Tuesday** 

```text
Monday                   82 commits          ███░░░░░░░░░░░░░░░░░░░░░░   10.09 % 
Tuesday                  256 commits         ████████░░░░░░░░░░░░░░░░░   31.49 % 
Wednesday                85 commits          ███░░░░░░░░░░░░░░░░░░░░░░   10.46 % 
Thursday                 57 commits          ██░░░░░░░░░░░░░░░░░░░░░░░   07.01 % 
Friday                   74 commits          ██░░░░░░░░░░░░░░░░░░░░░░░   09.10 % 
Saturday                 160 commits         █████░░░░░░░░░░░░░░░░░░░░   19.68 % 
Sunday                   99 commits          ███░░░░░░░░░░░░░░░░░░░░░░   12.18 % 
```


📊 **This Week I Spent My Time On** 

```text
🕑︎ Time Zone: Europe/Moscow

💬 Programming Languages: 
No Activity Tracked This Week

🔥 Editors: 
No Activity Tracked This Week

🐱‍💻 Projects: 
No Activity Tracked This Week

💻 Operating System: 
No Activity Tracked This Week
```

**I Mostly Code in Python** 

```text
Python                   40 repos            ████████████░░░░░░░░░░░░░   46.51 % 
Lua                      18 repos            █████░░░░░░░░░░░░░░░░░░░░   20.93 % 
JavaScript               7 repos             ██░░░░░░░░░░░░░░░░░░░░░░░   08.14 % 
CSS                      4 repos             █░░░░░░░░░░░░░░░░░░░░░░░░   04.65 % 
TypeScript               2 repos             █░░░░░░░░░░░░░░░░░░░░░░░░   02.33 % 
```



**Timeline**

![Lines of Code chart](https://raw.githubusercontent.com/vvladislovv/vvladislovv/main/assets/bar_graph.png)


 Last Updated on 29/03/2025 14:24:35 UTC
<!--END_SECTION:waka-->


[![Telegram Badge](https://img.shields.io/badge/-Vladislov-blue?style=flat&logo=Telegram&logoColor=white)](https://t.me/evka_rek) 
[![Discrod Badge](https://img.shields.io/badge/-vvlad_islovv-darkslateblue?style=flat&logo=Discord&logoColor=#4B0082)](https://discordapp.com/users/1144549294813224960/)
[![Discrod Badge](https://img.shields.io/badge/-vvlad_islovv-dodgerblue?style=flat&logo=VK&logoColor=#4B0082)](https://vk.com/vvlad_islovv)
  
<h1>How I'd define myself...literally</h1>

```C++
#include <iostream>
#include <string>
#include <vector>

class Vladislov : public Person {
private:
    std::string name;
    std::vector<std::string> vacancy;
    int age;
    std::vector<std::string> workPrograms;
    std::vector<std::string> languagesWork;
    std::vector<std::string> hobbies;

public:
    Vladislov() {
        name = "Vladislav";
        age = 18;
        vacancy.push_back("Backend Developer");
        workPrograms = {"Roblox Studio", "Visual Studio Code", "Visual Studio"};
        languagesWork = {"Luau", "Python", "C++"};
        hobbies = {"Blogging", "Coding"};
    }

    std::string currentLocation() {
        return "Moscow, Russia";
    }

    struct Currently {
        std::vector<std::string> studying;
        std::vector<std::string> myqualities;
    };

    Currently currently() {
        return {
            {"Python", "C++"},
            {"Hard work", "Deadline fulfillment", "Interest in new technologies"}
        };
    }
};

int main() {
    Vladislov vlad;
    
    std::cout << "Name: " << vlad.currentLocation() << std::endl;

    Vladislov::Currently info = vlad.currently();
    
    std::cout << "Studying: ";
    for (const auto& subject : info.studying) {
        std::cout << subject << " ";
    }
    
    std::cout << "\nQualities: ";
    for (const auto& quality : info.myqualities) {
        std::cout << quality << " ";
    }

    return 0;
}

```

<h2>What I always play with
<div>
</p>
  <img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/visualstudio/visualstudio-original.svg" title="Visual Studio" alt="" width="40" height="40"/>&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/vscode/vscode-original.svg" title="Visual Studio" alt="" width="40" height="40"/>&nbsp;
  <img src="https://github.com/vvladislovv/vvladislovv/assets/133252067/78c5b7b3-58bd-4ed6-bd49-fe687c4b4da4" title="Roblox Studio" alt="" width="40" height="40"/>&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/unity/unity-original.svg" title="Unity" alt="" width="40" height="40"/>&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/6910f0503efdd315c8f9b858234310c06e04d9c0/icons/intellij/intellij-original.svg" title="IntelliJ IDEA" alt="" width="40" height="40"/>&nbsp;
  <!--<img src="" title="YouTube" alt="" width="40" height="40"/>&nbsp; -->
</div>

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=vvladislovv&show_icons=true&theme=solarized-dark)
<!--
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=vvladislovv&hide_progress=truetheme=solarized-dar) 
 
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=anuraghazra&repo=github-readme-stats)](https://github.com/vvladislovv/TWWRR)-->




