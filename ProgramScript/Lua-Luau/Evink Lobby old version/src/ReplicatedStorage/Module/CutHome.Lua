local Home = {}

local TweenService = game:GetService("TweenService")
local FodelHome = game.Workspace:WaitForChild('CutCamera'):WaitForChild("Home")

function CutHome()
    for _, Folder in next, FodelHome:GetChildren() do
        Folder.Platform.Touched:Connect(function()
            print('asddfasdfasdf')
        end)
    end
end

return Home