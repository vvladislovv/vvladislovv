local TweenService = game:GetService("TweenService")
local Camera = game.Workspace.CurrentCamera
--local BlurLoging = game.Lighting.BlurLoging
local Player = game:GetService("Players").LocalPlayer
local Char = Player.Character or Player.CharacterAdded:Wait()
local CameraGui = game.Workspace.CutCamera.Cameras:WaitForChild("CameraGui")
local Loggin = Player:WaitForChild('PlayerGui'):WaitForChild('Logging')
--local Black = Loggin:WaitForChild('Black')
local Remote = game:GetService('ReplicatedStorage'):WaitForChild('Remote')
local TextLoging = Loggin.Frame1.Text
Loggin.Frame1.Visible = true
local ButttonGui = Loggin.Lobby.Lobby2.TextButton
local CouldTime = task.wait(0.3)
_G.PData = game.ReplicatedStorage.Remote.GetDataSave:InvokeServer()
print(_G.PData)
local GuiFrame = {}

function LoggingGui()
	--print('fasdfasdf')
	local TextL = 0
	repeat
		TextLoging.Text = "Loading"
		task.wait(CouldTime)
		TextLoging.Text = "Loading."
		task.wait(CouldTime)
		TextLoging.Text = "Loading.."
		task.wait(CouldTime)
		TextLoging.Text = "Loading..."
		task.wait(CouldTime)
		TextL += 1
	until TextL == 5
	
	if TextL == 5 then
		TextLoging.Text = "Start game!"
	end
	
	task.wait(0.5)
	TweenService:Create(Loggin.Frame1, TweenInfo.new(1.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {Transparency = 1}):Play()
	TweenService:Create(Loggin.Frame1.ImageLabel, TweenInfo.new(1.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {ImageTransparency = 1}):Play()
	TweenService:Create(TextLoging, TweenInfo.new(1.5, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut), {Transparency = 1}):Play()
end

-- Screen black
local UnBlack = TweenService:Create(Loggin:FindFirstChild("Black"),TweenInfo.new(1, 
	Enum.EasingStyle.Linear,
	Enum.EasingDirection.Out),
	{BackgroundTransparency = 1})

local Black = TweenService:Create(Loggin:FindFirstChild("Black"),TweenInfo.new(1, 
	Enum.EasingStyle.Linear,
	Enum.EasingDirection.Out),
	{BackgroundTransparency = 0})

function TweenCamera(Camera1,Camera2)
	local Teewin = TweenInfo.new(8,Enum.EasingStyle.Quad,Enum.EasingDirection.InOut,0)

	Camera.CameraType = Enum.CameraType.Scriptable
	Camera.CFrame = Camera1.CFrame

	local Tween = TweenService:Create(Camera, Teewin, {CFrame = Camera2.CFrame})
	Tween:Play()
	task.wait(8)
	--Camera.CameraType = Enum.CameraType.Custom
end

function CameraGet()
	task.spawn(function()
		local CutYes = false
		task.wait()
		print(_G.PData.BaseSettings.CutCameraLobby)
		if _G.PData.BaseSettings.CutCameraLobby == false then
			Char.HumanoidRootPart.Anchored = true
			--Char.Humanoid.WalkSpeed = 0
			TweenCamera(CameraGui.Camera1,CameraGui.Camera2)
			--TweenCamera(CameraGui.Camera2,CameraGui.Camera3)
			--TweenCamera(CameraGui.Camera3,CameraGui.Camera4)
			--TweenCamera(CameraGui.Camera4,CameraGui.Camera5)
			--TweenCamera(CameraGui.Camera5,CameraGui.Camera6)
			--TweenCamera(CameraGui.Camera6,CameraGui.Camera7)
			--TweenCamera(CameraGui.Camera7,CameraGui.Camera8)
			--TweenCamera(CameraGui.Camera8,CameraGui.Camera9)
			--TweenCamera(CameraGui.Camera9,CameraGui.Camera10)
			--TweenCamera(CameraGui.Camera10,CameraGui.Camera11)
			--	TweenCamera(CameraGui.Camera11,CameraGui.Camera1)
			Loggin.Lobby.Visible = true
			
			CutYes = true
			--_G.PData.BaseSettings.CutCameraLobby = true 
			Char.HumanoidRootPart.Anchored = false
			Remote.DataSetClient:FireServer(CutYes)
		else
			Char.HumanoidRootPart.Anchored = false
			TweenCamera(CameraGui.Camera11,CameraGui.Camera1)
			Loggin.Lobby.Visible = true
		end
	end)
end
ButttonGui.MouseButton1Click:Connect(function()
	Black:Play()
	task.wait(2)
	Char.HumanoidRootPart.Anchored = false
	Camera.CameraType = Enum.CameraType.Custom
	ButttonGui:Destroy()
	Loggin.Lobby:Destroy()
	Loggin.Frame1:Destroy()
	UnBlack:Play()
end)

LoggingGui()
CameraGet()

return GuiFrame