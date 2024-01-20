# https://www.w3schools.com/js/js_json_intro.asp - Documentation JSON. I'm read is it.
import json # Save in Json Date, Get and set new date

with open("ScriptJSon.json", "r") as Json_file:
    a = json.load(Json_file)
    
del a["Programer"]["Lua"]

a["Doper"] = [1, "hello", {"a":1}, [5,62345,26234]]

#Dumps - Dumps позволяет создать JSON-строку из переданного в нее объекта. Loads — преобразовать строку назад в объекты языка. Dump и load используют, чтобы сохранить результат в файл или воссоздать объект.
#Dump - Если уровень отступа 0, отрицательный или "", то вместо этого будут просто использоваться новые строки. Значение по умолчанию None отражает наиболее компактное представление. Если indent - строка, то она и будет использоваться в качестве отступа.

print(json.dumps(a, indent=3))

with open("ScriptJSon.json", "w") as Json_file:
    a = json.dump(a,Json_file, indent=2) # Save File Json



