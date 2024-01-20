local Players = game:GetService("Players")
local TW = game:GetService("TweenService")
local ItemsFolder = game.Workspace:WaitForChild("ItemsFolder"):GetChildren()
local Remotes = game:GetService("ReplicatedStorage"):WaitForChild("Remotes")
--local Data = require(game:GetService("ServerScriptService").Server.Data)
local Workspace = game:GetService("Workspace")
local ItemsBag = {
    BagMin = 0,
    BagMax = 15,
}

local CoulDown = 5

local items = {}
    function AppItems()
        for i, Items in pairs(ItemsFolder) do
            Items.Proxy.Triggered:Connect(function(Itm)
			local plr = Itm.Parent:FindFirstChild("Humanoid")
                    if ItemsBag["BagMin"] == ItemsBag["BagMax"] then
                        print("STOOPPP")
                    elseif ItemsBag["BagMin"] <= ItemsBag["BagMax"] then
                        plr:WaitForChild("leaderstats").Coins = plr:WaitForChild("leaderstats").Coins
							BagItems()
                    Itm = Items
                        TW:Create(Itm, TweenInfo.new(0.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {Transparency = 1}):Play()
                        Itm.Proxy.Enabled = false
						--BagItems()
                        task.wait(CoulDown)
                        TW:Create(Items, TweenInfo.new(0.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {Transparency = 0}):Play()
                        Items.Proxy.Enabled = true
                        end
                    end)
                --BagItems()
        end
    end


    function BagItems()
	
	        
		
	end
    

    function items.StartSystems()
        AppItems()
        --BagItems()
    end
return items