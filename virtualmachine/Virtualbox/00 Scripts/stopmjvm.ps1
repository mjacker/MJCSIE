Write-Host "Getting running virtual machine list..."
# $virtualmachines = Vboxmanage list vms | Select-String -Pattern '"([^"]+)"' -AllMatches
# Write-Host $virtalmachines

$pattern = '"([^"]+)"'
$virtualMachineList = New-Object System.Collections.ArrayList
$matches = Vboxmanage list runningvms | Select-String -Pattern $pattern -AllMatches
foreach($match in $matches.Matches){
	Write-Host "found: $match"
	$virtualMachineList.Add("$match")
}

if ($virtualMachineList.ToArray().Length -eq 0)
{
	Write-Host "No running virtual machines."
	return 1
}
else
{

	Write-Host "Choose virtual machine:"
	$choice = Read-Host
	Write-host "force shutdown? [yes|no]"
	$head = Read-Host

	$selected = $virtualMachineList[[int]$choice]
	Write-Host "Selected $selected"
	Write-Host $head

	if (($firstargument -eq "--headless") -or ($firstargument -eq "-hl"))
	{
			  Write-Host "Starting headless virtual machine..."
			  powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "vboxmanage startvm $selected --type headless"
	}
	else
	{
			  Write-Host "Stoping virtual machine..."
			  powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "vboxmanage controlvm $selected poweroff"
			  
			  
	}

}
