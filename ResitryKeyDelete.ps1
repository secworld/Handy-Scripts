$Servers = “<COMPUTER NAME-1>",”<COMPUTER NAME-2>",”<COMPUTER NAME-3>","<COMPUTER NAME-4>","<COMPUTER NAME-5>"

$credential = Get-Credential -Credential Administrator

Invoke-Command -ComputerName $Servers -Credential $credential -ScriptBlock {Remove-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system\LocalAccountTokenFilterPolicy}
