Using module '.\Scripts settings.psm1'

$Settings = [Settings]::new()

if($Settings.ProblematicID.count -gt 0)
{
    Set-Location '..\PixivUtil2 - Problematic'
    Start-Process -FilePath '..\PixivUtil2 - Problematic\PixivUtil2.py' -ArgumentList $Settings.PixivArg -Wait
    Start-Process -FilePath '..\PixivUtil2 - Problematic\PixivUtil2.py' -ArgumentList $Settings.FanboxArg
}

$FanboxDownload = Get-ChildItem -Directory .. | Where-Object {$_ -match 'PixivUtil2 - Fanbox'}
$PixivDownload = Get-ChildItem -Directory .. | Where-Object {$_ -match 'PixivUtil2 - Copy'}

ForEach($Path in $FanboxDownload)
{
    Set-Location "..\$Path"
    Start-Process -FilePath "..\$Path\PixivUtil2.py" -ArgumentList $Settings.FanboxArg
}
ForEach($Path in $PixivDownload)
{
    Set-Location "..\$Path"
    Start-Process -FilePath "..\$Path\PixivUtil2.py" -ArgumentList $Settings.PixivArg
}