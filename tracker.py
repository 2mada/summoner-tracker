
import requests

def getID(region, summonerName, APIKey):
    # make url
    URL1 = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    # requests.get goes to the url we made and gives us back a json
    response1 = requests.get(URL1)
    return response1.json()

def getRankedData(region, ID, APIKey):
    URL2 = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + APIKey
    response2 = requests.get(URL2)
    print(URL2)
    return response2.json()

def main():
    print("Welcome!\n")
    print("Type in one the following regions for the player you wish to search for:\n")
    print("NA1 | EUW1 | EUN1 | BR1 | KR1 | JP1 | LA1 | LA2 | OC1 | TR1 | RU1\n")

    # ask the user for region, summoner name, and API Key
    # only three things I need from them in order to get create my URL and grab their ID

    region = (str)(input('Type in one of the regions above: '))
    summonerName = (str)(input('Type your Summoner Name here (do not include any spaces): '))
    APIKey = (str)(input('Copy and paste your API Key here:'))

    # send these three pieces off to getRankedData function which creates URL and gives me back a JSON that has the ID for that specific summoner
    response1 = getID(region, summonerName, APIKey)

    ID = response1['id']

    response2 = getRankedData(region, ID, APIKey)
    print("\nSUMMONER NAME =", response2[1]["summonerName"])
    print("\nQUEUE =", response2[1]["queueType"])
    print("\nRANK =", response2[1]["tier"], response2[1]["rank"])
    print("\nLP =", response2[1]["leaguePoints"])
    print("\nWINS =", response2[1]["wins"])
    print("\nLOSSES =", response2[1]["losses"])
    print("\nWIN RATE =", round(((response2[1]["wins"])/(response2[1]["losses"]+response2[1]["wins"])) * 100))


if __name__ == "__main__":
    main()
    input('\nPress ENTER to exit')
