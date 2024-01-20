local Data = {} 

    game.Players.PlayerAdded:Connect(function(player)
        local leaderstats = Instance.new("Folder", player)
        leaderstats.Name = "leaderstats"

        local ItemsBag = Instance.new("IntValue", leaderstats)
        ItemsBag.Name = "ItemsBag"
        ItemsBag.Value = 0

        local Coins = Instance.new("IntValue", leaderstats)
        Coins.Name = "Coins"
        Coins.Value = 0
    end)
    
return Data