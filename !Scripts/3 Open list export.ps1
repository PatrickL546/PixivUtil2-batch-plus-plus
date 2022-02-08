$ListPath = Get-ChildItem -Path .. -Name -Recurse | Where-Object {$_ -like '*\list*'}

foreach ($Path in $ListPath)
{
    Start-Process -FilePath "..\$Path"
}