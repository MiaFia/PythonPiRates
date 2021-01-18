#Some code goes here

import json

with open ('People\People\A_people.json') as file:
    real_people= filter(json.load(file), 'label'=='person')


#use SelectString in CLI to only use data that you need
# So these are probably things to do in the shell
#Get-Content 'people.zip'
#Select-String label 'person'
# Write-Output > 'new file with a name, that only includes non-fictional people
