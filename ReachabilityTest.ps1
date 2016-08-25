$servers =  get-content "ip_addresses.txt"
foreach ($server in $servers) {

    $output = Test-Connection -ComputerName $server -quiet
    "{0},{1}" -f $server, $output | Out-File -FilePath Reachability.txt -Append
}
