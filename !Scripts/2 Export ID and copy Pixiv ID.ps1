Using module '.\Scripts settings.psm1'

$Settings = [Settings]::new()

if (Test-Path '.\2 Pixiv ID.txt')
{
}
else
{
    $null = New-Item -Path '.\2 Pixiv ID.txt' -ItemType 'File'
}

do
{
'-----------------MENU-----------------'
''
'Press Enter to skip'
''
'Press [1] Export online bookmark'
''

$Option = [console]::ReadKey($true)

    if ($Option.KeyChar -eq '1')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black

        Start-Process -FilePath '..\PixivUtil2\PixivUtil2.py' -ArgumentList $Settings.PixivExportArg -Wait
        if ($Settings.Scrub -eq 'true')
        {
            $Content = Get-Content '.\2 Pixiv ID.txt' | Where-Object {$_ -NotMatch '#'}
            $Content | Out-File -FilePath '.\2 Pixiv ID.txt' -Encoding Ascii
        }
        break
    }
    elseif ($Option.Key -ne "Enter")
    {
        Clear-Host
        Write-Host 'Please select an option' -ForegroundColor Yellow -BackgroundColor Black
        ''
    }
    else
    {
        Clear-Host
        Write-Host 'You selected skip' -ForegroundColor DarkRed -BackgroundColor Black
    }
} while ($Option.Key -ne "Enter")
''

do
{
'-----------------MENU-----------------'
''
'Press Enter to skip'
''
'Press [1] Remove blacklisted ID'
''

$Option = [console]::ReadKey($true)

    if ($Option.KeyChar -eq '1')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black

        $Content = Get-Content '.\2 Pixiv ID.txt'
        [System.Collections.ArrayList]$ListID = $Content
        ForEach($RemoveID in $Settings.BlacklistID)
        {
        $ListID.Remove($RemoveID)
        }
        $ListID | Out-File -FilePath '.\2 Pixiv ID.txt' -Encoding Ascii
        break
    }
    elseif ($Option.Key -ne "Enter")
    {
        Clear-Host
        Write-Host 'Please select an option' -ForegroundColor Yellow -BackgroundColor Black
        ''
    }
    else
    {
        Clear-Host
        Write-Host 'You selected skip' -ForegroundColor DarkRed -BackgroundColor Black
    }
} while ($Option.Key -ne "Enter")
''

do
{
'-----------------MENU-----------------'
''
'Press Enter to skip'
''
'Press [1] Archive Pixiv ID.txt'
''

$Option = [console]::ReadKey($true)

    if ($Option.KeyChar -eq '1')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black

        $Date = Get-Date -Format $Settings.DateFormat
        if (Test-Path -Path '.\Export Archive\*.txt')
        {
            $Content = Get-Content '.\2 Pixiv ID.txt'
            $RecentArchive = Get-ChildItem '.\Export Archive\PixivIDArchive*.txt' | Sort-Object LastWriteTime | Select-Object -last 1 | Get-Content
            if(Compare-Object $RecentArchive $Content)
            {
                Get-Content '.\2 Pixiv ID.txt' | Out-File -FilePath ".\Export Archive\PixivIDArchive_$Date.txt" -Encoding Ascii
            }
            else
            {
                Clear-Host
                Write-Host 'Archive already exist' -ForegroundColor Green -BackgroundColor Black
                Start-Sleep -Seconds 3
            }
        }
        else
        {
            Get-Content '.\2 Pixiv ID.txt' | Out-File -FilePath ".\Export Archive\PixivIDArchive_$Date.txt" -Encoding Ascii
        }
        break
    }
    elseif ($Option.Key -ne "Enter")
    {
        Clear-Host
        Write-Host 'Please select an option' -ForegroundColor Yellow -BackgroundColor Black
        ''
    }
    else
    {
        Clear-Host
        Write-Host 'You selected skip' -ForegroundColor DarkRed -BackgroundColor Black
    }
} while ($Option.Key -ne "Enter")
''

#Remove Problematic ID and copy list
if($Settings.ProblematicID.count -gt 0)
{
    $Content = Get-Content '.\2 Pixiv ID.txt'
    [System.Collections.ArrayList]$ListID = $Content
    ForEach($RemoveProblematicID in $Settings.ProblematicID)
    {
    $ListID.Remove($RemoveProblematicID)
    }
    $ListID | Out-File -FilePath '.\2 Pixiv ID.txt' -Encoding Ascii

    $Settings.ProblematicID | Out-File -FilePath '..\PixivUtil2 - Problematic\list.txt'
    $Settings.ProblematicID | Out-File -FilePath '..\PixivUtil2 - Problematic\listfanbox.txt'
}

#Divides Pixiv ID to (Instances) Folder count
#Fanbox Instances
$LineCount = Get-Content '.\2 Pixiv ID.txt' | Measure-Object -Line

if ($Settings.FanboxCopy | Where-Object {$_ -ne 0})
{
    $FanboxIncrement = [int][Math]::Ceiling($LineCount.Lines/$Settings.FanboxCopy)
}

for($i=0; $i -lt $Settings.FanboxCopy; $i++)
{
    if ($i -eq '0')
    {
        Get-Content '.\2 Pixiv ID.txt' -head $FanboxIncrement | Out-File -FilePath '..\PixivUtil2 - Fanbox\listfanbox.txt' -Encoding Ascii
    }
    elseif ($i -eq '1')
    {
        Get-Content '.\2 Pixiv ID.txt' | Select-Object -index ($FanboxIncrement..(($FanboxIncrement*($i+1))-1)) | Out-File -FilePath '..\PixivUtil2 - Fanbox - Copy\listfanbox.txt' -Encoding Ascii
    }
    else
    {
        Get-Content '.\2 Pixiv ID.txt' | Select-Object -index (($FanboxIncrement*$i)..(($FanboxIncrement*($i+1))-1)) | Out-File -FilePath "..\PixivUtil2 - Fanbox - Copy ($i)\listfanbox.txt" -Encoding Ascii
    }
}

#Pixiv Instances
if ($Settings.PixivCopy | Where-Object {$_ -ne 0})
{
    $PixivIncrement = [int][Math]::Ceiling($LineCount.Lines/$Settings.PixivCopy)
}

for($i=1; $i -le $Settings.PixivCopy; $i++)
{
    if ($i -eq '1')
    {
        Get-Content '.\2 Pixiv ID.txt' -head $PixivIncrement | Out-File -FilePath '..\PixivUtil2 - Copy\list.txt' -Encoding Ascii
    }
    elseif ($i -eq '2')
    {
        Get-Content '.\2 Pixiv ID.txt' | Select-Object -index ($PixivIncrement..(($PixivIncrement*$i)-1)) | Out-File -FilePath "..\PixivUtil2 - Copy ($i)\list.txt" -Encoding Ascii
    }
    else
    {
        Get-Content '.\2 Pixiv ID.txt' | Select-Object -index (($PixivIncrement*($i-1))..(($PixivIncrement*$i)-1)) | Out-File -FilePath "..\PixivUtil2 - Copy ($i)\list.txt" -Encoding Ascii
    }
}