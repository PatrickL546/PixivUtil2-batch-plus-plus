Using module '.\Scripts settings.psm1'

$Settings = [Settings]::new()

ROBOCOPY . '..\PixivUtil2' config.ini

if($Settings.ProblematicID.count -gt 0)
{
    ROBOCOPY /e '..\PixivUtil2' '..\PixivUtil2 - Problematic'
}

for($i=0; $i -lt $Settings.FanboxCopy; $i++)
{
    if ($i -eq '0')
    {
        ROBOCOPY /e '..\PixivUtil2' '..\PixivUtil2 - Fanbox'
    }
    elseif ($i -eq '1')
    {
        ROBOCOPY /e '..\PixivUtil2' '..\PixivUtil2 - Fanbox - Copy'
    }
    else
    {
        ROBOCOPY /e '..\PixivUtil2' "..\PixivUtil2 - Fanbox - Copy ($i)"
    }
}

for($i=1; $i -le $Settings.PixivCopy; $i++)
{
    if ($i -eq '1')
    {
        ROBOCOPY /e '..\PixivUtil2' '..\PixivUtil2 - Copy'
    }
    else
    {
        ROBOCOPY /e '..\PixivUtil2' "..\PixivUtil2 - Copy ($i)"
    }
}