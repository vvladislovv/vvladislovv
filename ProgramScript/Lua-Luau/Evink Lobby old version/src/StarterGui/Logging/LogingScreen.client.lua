
--[[local Loging = script.Parent.Frame1
local TextLoging = Loging.Text
local image = Loging.ImageLabel
Loging.Visible = true
local CouldTime = task.wait(0.3)
GuiScreen = true
local Lobby = script.Parent.Lobby
--GuiScreen = true
local TW = game:GetService("TweenService")
--local Lobby = script.Parent.Lobby

function Text()
	local TextL = 0
	repeat
		TextLoging.Text = "Loading"
		wait(CouldTime)
		TextLoging.Text = "Loading."
		wait(CouldTime)
		TextLoging.Text = "Loading.."
		wait(CouldTime)
		TextLoging.Text = "Loading..."
		wait(CouldTime)
		TextL += 1
	until TextL == 5
end
Text()

TW:Create(Loging, TweenInfo.new(1.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {Transparency = 1}):Play()
TW:Create(image, TweenInfo.new(1.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {ImageTransparency = 1}):Play()
TW:Create(TextLoging, TweenInfo.new(1.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {Transparency = 1}):Play()


print('fsadfasdf')

]]



	

