$servers = get-content "<Host File Path>"
foreach ($server in $servers) {
  $addresses = [System.Net.Dns]::GetHostAddresses($server)
  foreach($a in $addresses) {
    "{0},{1}" -f $server, $a.IPAddressToString | Out-File -FilePath results.txt -Append
  }
}
