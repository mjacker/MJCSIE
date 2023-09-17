# checking is argument `pato` is used

$check = $args[0]

if ($check -eq "pato")
{
	Write-Host "cuak cuak"
	write-Host $head
	powershell.exe -NoLogo -ExecutionPolicy Bypass -Command "calc.exe"
}
else
{
	Write-Host "miau"
	write-Host $head
}
