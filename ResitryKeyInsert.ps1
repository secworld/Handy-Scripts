$servers = “New-IndusDirect-Web-W2K8",”Meridian",”CFDINDUSLOAN","HHTFTP","PROGENIE"

$credential = Get-Credential -Credential iblvaadmin

Invoke-Command -ComputerName $servers -Credential $credential -ScriptBlock {New-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system -Name LocalAccountTokenFilterPolicy -Value “1”}