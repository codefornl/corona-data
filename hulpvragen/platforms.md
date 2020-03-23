# Platforms
List of dutch platforms for which we can figure out how to fetch or scrape data.

## Held Nodig
https://heldnodig.nl/

## NL Voor Elkaar
https://www.nlvoorelkaar.nl/
https://www.nlvoorelkaar.nl/coronahulp/?utm_campaign=Martijn%20Arets%20%28De%20Platformrevolutie%29&utm_medium=email&utm_source=Revue%20newsletter

## Gewoon Mensen
https://www.gewoonmensendiemensenwillenhelpen.nl/

**api address:**: https://api-server-271218.appspot.com/v1/tasks?zipcode=1945RP&taskTypeId=32ea2942-68be-11ea-bc55-0242ac130003
Can't query without zipcode. Doing it for each zipcode implies millions of requests. 

## Niet Alleen
https://nietalleen.nl/

As far as I can see this is a full manual matching process to organisations. There is no way to query the help requests.
## Corona Helpers
https://www.coronahelpers.nl/

**api address:**: https://www.coronahelpers.nl/api/deeds?query=&page=1&causes=&activities=&date=&pageSize=18&withOrganization=true
Uses paging where total amount of pages is returned in the response.

## Elkaar Helpen
https://nijmegen-oost.nl/elkaar-helpen
https://puurpapendrecht.nl/

Finding some traces of something called Thrive comments in the submit which is part of thrive themes (for wordpress). This is per city only and masterdam has only two requests. And Tilburg which is hit hard 0 requests. Not really worth the pursuit right now I guess.

## Corona Hulp
https://www.coronahulp.com/

Not easy to deduce how this platform works.

## Whapp
https://cooperatiewehelpen.nl/

I don't understand how this app works. I signed up. But there's not even a list of queries to been seen. So at this stage I can't even be bothered to research the backend.

## Bezorg de Zorg
https://www.bezorg-dezorg.nl/
Hier weet @janvankampen meer van


## Studenten helpen Scholeren
https://studentenhelpenscholieren.nl/

This is a simple Google form that thus has a Google sheet as data store.