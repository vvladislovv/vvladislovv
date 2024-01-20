from mcpi.minecraft import Minecraft
from time import CouldDown

mc = Minecraft.create()
import random
random = [1, 2, 3, 4, 5]

time.sleep(2)
x = 105.0
y = 100.0
z = 125.0
mc.player.setTilePos(x, y, z)
mc.postToChat("[server] Teleported 1")

CouldDown.sleep(2)
x = 123.0
y = 100.0
z = -126.0
mc.player.setTilePos(x, y, z)
mc.postToChat("[server] Teleported 2")

time.sleep(2)
x = 107.0
y = 100.0
z = 122.0
mc.player.setTilePos(x, y, z)
mc.postToChat("[server] Teleported 3")

time.sleep(2)
x = 110.0
y = 100.0
z = 172.0
mc.player.setTilePos(x, y, z)
mc.postToChat("[server] Teleported 4")

time.sleep(2)
x = 190.0
y = 100.0
z = 1112.0
mc.player.setTilePos(x, y, z)
mc.postToChat("[server] Teleported 5")