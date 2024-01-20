local RS = game:GetService('ReplicatedStorage')
require(RS.Module.Fireflies)
require(RS.Module.GuiFrame)
require(RS.Module.CutHome)
_G.PData = game.ReplicatedStorage.Remote.GetDataSave:InvokeServer()

--remote.GetDataSave
print("START CLIENT SCRIPT")