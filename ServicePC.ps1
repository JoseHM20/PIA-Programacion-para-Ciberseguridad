write-host("===============================")
write-host("Tool to view system information")
write-host("===============================")

write-host("BIOS information...")
Get-CimInstance -ClassName Win32_BIOS

write-host("Loading processor information...")
Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty "CIM*"

write-host("Showing available disk information...")
Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3"


write-host("Operation of the services...")
$service = Read-Host -Prompt "Type the service to be verified"
$infoserv = Get-Service -Name $service
write-host("The current status of the service is:")
$infoserv
write-host("Options: [1] Start service, [2] Stop service")
$process = Read-Host -Prompt "Choose the desired option"
switch($process){
                 1{Start-Service -Name $service
                   write-host("Service has been restarted")
                   break}
                 1{Stop-Service -Name $service
                   write-host("The service has been stopped")
                   break}
                   }

write-host("Network information")
Get-NetIPAddress -AddressFamily IPV4