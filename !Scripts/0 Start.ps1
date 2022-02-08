if (Test-Path '.\Export Archive\')
{
}
else
{
    $null = New-Item -Path '.\Export Archive' -ItemType 'Directory'
}

do {
            '-----------------MENU-----------------'
            ''
            'Press [1] Make copy'
            ''
            'Press [2] Export ID and copy Pixiv ID'
            ''
            'Press [3] Open list export (Optional)'
            ''
            'Press [4] Start download'
            ''
            'Press [5] Delete db.sqlite (Optional)'
            ''
            'Press [6] Delete pixivutil.log (Optional)'
            ''
            'Press [7] Convert ugoira to webm (Optional)'
            ''
            'Press [8] Delete ugoira zip file (Optional)'
            ''
Write-Host  'Press Enter to Quit' -ForegroundColor DarkRed -BackgroundColor Black
            ''

    $Option = [console]::ReadKey($true)

    if ($Option.KeyChar -eq '1')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process PowerShell {-File "1 Make copy.ps1"}
    }
    elseif ($Option.KeyChar -eq '2')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process PowerShell {-File "2 Export ID and copy Pixiv ID.ps1"} -Wait
    }
    elseif ($Option.KeyChar -eq '3')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process PowerShell {-File "3 Open list export.ps1"}
    }
    elseif ($Option.KeyChar -eq '4')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process PowerShell {-File "4 Start download.ps1"}
    
    }
    elseif ($Option.KeyChar -eq '5')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process -FilePath '5 Delete db.sqlite.py'
    
    }
    elseif ($Option.KeyChar -eq '6')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process -FilePath '6 Delete pixivutil.log.py'
    
    }
    elseif ($Option.KeyChar -eq '7')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process -FilePath '7 Convert ugoira to webm.py'
    
    }
    elseif ($Option.KeyChar -eq '8')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
        Start-Process -FilePath '8 Delete ugoira zip file.py'
    }
    elseif ($Option.KeyChar -eq 'q')
    {
        Clear-Host
        Write-Host 'You selected option ['$Option.KeyChar']' -ForegroundColor Green -BackgroundColor Black
    }
    elseif ($Option.Key -ne "Enter")
    {
        Clear-Host
        Write-Host 'Please select an option' -ForegroundColor Yellow -BackgroundColor Black
    }
    ''

} while ($Option.Key -ne "Enter")