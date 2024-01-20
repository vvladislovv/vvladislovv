local Data = {}

local RunService = game:GetService("RunService")
local Players = game:GetService("Players")

local Remotes = game.ReplicatedStorage:WaitForChild("Remote")
--local Modules = game.ReplicatedStorage:WaitForChild("Modules")
--local Items = require(Modules.Items)

Data.PlayerData = {}

function Data.new(Player)
	local PData = {}

	PData.BaseSettings = { 
		teset = false
	}

	Data.PlayerData[Player.Name] = PData
	return PData
end

function Data:Get(Player)
	if game:GetService("RunService"):IsServer() then
		return Data.PlayerData[Player.Name]
	else
		return Remotes.GetDataSave:InvokeServer()
	end
end

local AutoSaves = {}

local MainKey = 'Wtf21255312..е4526637e'
local ClientKey = 'Wtf21552312..е4256637e'

local DataStore2 = require(game.ServerScriptService.DataStore2)

function LoadData(Client)
	DataStore2.Combine(MainKey, ClientKey)
	local PData = Data.new(Client)
	local DataStorage = DataStore2(ClientKey, Client):GetTable(PData)
	PData = GetDataFromDataStorage(Client, DataStorage)
	AutoSaves[Client.Name] = Client
end

function SaveData(client, PData)
	DataStore2(ClientKey, client):Set(PData)
	print(PData)
end

function GetDataFromDataStorage(Client, DataStorage)
	local PData = Data:Get(Client)
	
	for i,v in pairs(DataStorage.BaseSettings) do
		PData.BaseSettings[i] = DataStorage.BaseSettings[i]
	end

	--for i,v in pairs(DataStorage.Achievements) do
	--	PData.Achievements[i].Amount = DataStorage.Achievements[i].Amount
	--	PData.Achievements[i].Opened = DataStorage.Achievements[i].Opened
	--	PData.Achievements[i].Claimed = DataStorage.Achievements[i].Claimed
	--end
	--for i,v in pairs(DataStorage.FieldTotems) do
	--	PData.FieldTotems[i].Time = DataStorage.FieldTotems[i].Time
	--	PData.FieldTotems[i].Active = DataStorage.FieldTotems[i].Active
	--end
	--if #DataStorage.Amulets > 0 then
	--	for i,v in pairs(DataStorage.Amulets) do
	--		PData.Amulets[i] = DataStorage.Amulets[i]
	--	end
	--end
	--if #DataStorage.OldAmulets > 0 then
	--	for i,v in pairs(DataStorage.OldAmulets) do
	--		PData.OldAmulets[i] = DataStorage.OldAmulets[i]
	--	end
	--end
end

do
	Players.PlayerAdded:Connect(LoadData)
	Players.PlayerRemoving:Connect(function(Client)
		SaveData(Client, Data:Get(Client))
		AutoSaves[Client.Name] = nil
	end)
	--Players.PlayerRemoving:Connect(function(Client) SaveData(Client, Data:Get(Client)) AutoSaves[Client.Name] = nil end)

	game.ReplicatedStorage.Remote.GetDataSave.OnServerInvoke = function(client)
		local PData = Data:Get(client)
		return PData
	end
end

local TotalDelta = 0
spawn(function()
	while wait(1) do
		TotalDelta += 1
		if TotalDelta > 3 then
			TotalDelta = 0
			for _, Player in pairs(AutoSaves) do
				local PData = Data:Get(Player)
				SaveData(Player, PData)
			end
		end
	end
end)

return Data
