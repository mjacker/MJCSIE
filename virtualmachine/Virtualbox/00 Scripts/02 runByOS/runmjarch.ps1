# Get first argument
$firstargument = $args[0]

if (($firstargument -eq "--headless") -or ($firstargument -eq "-hl"))
{
	Write-Host "Starting headless virtual machine..."
	powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "vboxmanage startvm MJArch --type headless"
}
else
{
	Write-Host "Starting virtual machine..."
	powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "vboxmanage startvm MJArch"
}
