$servers = “New-IndusDirect-Web-W2K8",”CTFS-Meridian",”CFDINDUSLOAN","HHTFTP","PROGENIE"

$credential = Get-Credential -Credential iblvaadmin

Invoke-Command -ComputerName $servers -Credential $credential -ScriptBlock {Remove-Item -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system\LocalAccountTokenFilterPolicy}