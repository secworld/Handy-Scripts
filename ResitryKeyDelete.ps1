$servers = “<COMPUTER NAME-1>",”<COMPUTER NAME-2>",”<COMPUTER NAME-3>","<COMPUTER NAME-4>","<COMPUTER NAME-5>"

$credential = Get-Credential -Credential <USER-NAME>

Invoke-Command -ComputerName $servers -Credential $credential -ScriptBlock {Remove-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system\LocalAccountTokenFilterPolicy}
