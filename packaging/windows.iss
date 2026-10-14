#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif

[Setup]
AppId={{C4F23213-0796-48B8-8BE4-A8175B53E31B}
AppName=ASH Toolset
AppVersion={#AppVersion}
DefaultDirName={localappdata}\Programs\ASH-Toolset
DefaultGroupName=ASH Toolset
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir=..\artifacts
OutputBaseFilename=ASH-Toolset-Windows-Setup
SetupIconFile=..\data\raw\ash_icon_1.ico
LicenseFile=..\LICENSE
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\ASH-Toolset.exe

[Files]
Source: "..\dist\ASH-Toolset\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\ASH Toolset"; Filename: "{app}\ASH-Toolset.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\ASH-Toolset.exe"; Description: "Launch ASH Toolset"; Flags: nowait postinstall skipifsilent; WorkingDir: "{app}"
