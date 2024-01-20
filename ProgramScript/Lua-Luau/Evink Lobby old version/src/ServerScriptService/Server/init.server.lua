local Data = require(script.DataStore)
local Remote = game:GetService('ReplicatedStorage'):WaitForChild('Remote')
print('Start')


Remote.DataSetClient.OnServerEvent:Connect(function(plr, cut)
    print(plr)
    local PData = Data:Get(plr)
    if cut == true then
		PData.BaseSettings.CutCameraLobby = true
        print(PData)
    else
        print("No Connect")
        return
    end
end)