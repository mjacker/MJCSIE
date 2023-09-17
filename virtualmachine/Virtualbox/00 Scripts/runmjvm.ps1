Write-Host "Getting virtual machine list..."
# $virtualmachines = Vboxmanage list vms | Select-String -Pattern '"([^"]+)"' -AllMatches
# Write-Host $virtalmachines

$pattern = '"([^"]+)"'
$headless = $false

# loag virtual machine list
$virtualMachineList = New-Object System.Collections.ArrayList
$matches = Vboxmanage list vms | Select-String -Pattern $pattern -AllMatches
foreach($match in $matches.Matches){
	Write-Host "found: $match"
	$virtualMachineList.Add("$match")
}

Write-Host "Choose virtual machine:"
$choice = Read-Host
Write-host "Headless mode? [yes|no]"
$head = Read-Host

$selected = $virtualMachineList[[int]$choice]
Write-Host "Selected $selected"
Write-Host $head

if ($head -eq "yes")
{
	$headless = $true
}

if (($firstargument -eq "--headless") -or ($firstargument -eq "-hl") -or ($headless -eq $true))
{
        Write-Host "Starting headless virtual machine..."
        powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "vboxmanage startvm $selected --type headless"
}
else
{
        Write-Host "Starting virtual machine..."
        powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "vboxmanage startvm $selected"
}

