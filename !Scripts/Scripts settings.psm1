Class Settings
    {
        #(Instances) Folder count
        [int]$FanboxCopy = 1

        #(Instances) Folder count
        [int]$PixivCopy = 1

        #Fanbox download arguments
        [string]$FanboxArg = '-s f5 -x'

        #Pixiv download arguments
        [string]$PixivArg = '-s 4 -f list.txt --include_sketch -x'

        #Pixiv export arguments
        [string]$PixivExportArg = '-s e -p y -x "2 Pixiv ID.txt"'

        #Remove
            ###Export date: ###
            ###END-OF-FILE###
        [string]$Scrub = 'true'

        #Archive date format
        [string]$DateFormat = 'MM-dd-yyyy_HH-mm-ss'

        #Add Pixiv ID to remove. Separate ID with comma
        [array]$BlacklistID = $null
        
        #Problematic ID, If there are some ID that uses OAuth to continue
        #You can add here to make their own instance and not affect the other instance
        #This will download both Pixiv (Sketch if it's included in $PixivArg) and Fanbox
        [array]$ProblematicID = $null
    }