local DataSave = require(game.ServerScriptService.ServerGame.DataStoreGame)
local HiveFolder = workspace.Hive
local Client = game:GetService("Players")
local TweenService = game:GetService("TweenService")


local HS = {}

    function GetHiveNime(NamePLR1,NamePLR2, Client, PData)
        NamePLR1.NamePlayer.Text = Client.Name
        NamePLR2.TextUser.Text = Client.Name
    end

    local function TweenSlot(NumStart,NumStop)
        local RandomSlot = math.random(NumStart,NumStop)

        if RandomSlot then
            
        end
    end

    function HS:GetSlotSpawn(NumberSlot, Num)
        for i, HiveNumber in pairs(HiveFolder.SlotHive:GetChildren()) do
            for v, NumberSlot in pairs(HiveNumber[NumberSlot]) do
               local Start = table.find(NumberSlot, 1)
               local Stop = table.find(NumberSlot, 32)
                if Start == tostring(Start) then
                    return Start
                end
                if Stop == tostring(Stop) then
                    return Stop
                end
               if NumberSlot:IsA("MeshPart") then
                    if NumberSlot.Transparency == 1 then
                        TweenSlot(Start, Stop)
                        return v
                    elseif NumberSlot.Transparency == 0 then
                        TweenSlot:Stop()
                    end
                end
            end
        end
    end

    function HS:PlatformName(HumberHive)
        
        for _, Platform in pairs(HiveFolder.PlatformHive[HumberHive].Text) do -- Platform Пустая
             Platform.Touched:Connect(function()
                Platform.TextGui.TextUser.Text = Client.Name
                print("FF")
             end)

            
        end



    end

    function HS:StartScript()
       -- HS:GetSlotSpawn()
        HS:PlatformName()
    end

    

return HS
