
		$VulnerableServices=@()

        $Services = Get-WmiObject -Class win32_service -Property name,pathname
        
        $UnquotedPath = $Services | Where-Object {$_.PathName -notmatch '"'} | Where-Object {$_.PathName -ne $null} | Select Name,PathName
		Write-Output ("Installed Services are :   ")
		$UnquotedPath
        foreach ($Path in $UnquotedPath) {
		try{
            $Drive = $Path.PathName | Split-Path -Qualifier
            $Executable = $Path.PathName | Split-Path -Leaf

            #Space Check and Quote Check
            if( ($Path.PathName -match ' ') -and ($Executable -notmatch ' ') -and ($Path.PathName -notmatch './') ) {
                
                # Vulnerability Found
                Write-Warning ("Unquoted Service Path Discovered for " + $Path.Name + "    PATH: " + $Path.PathName)
                $VulnerableServices += New-Object PSObject -Property @{
                    ServiceName = $Path.Name
                    ServicePath = $Path.PathName
                    HostName = $env:COMPUTERNAME
                } 

            } 
			}
			catch {Write-Warning "My coding skills may not be so good"}
			
        } 

	
