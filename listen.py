from selenium import webdriver
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed


options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("--no-sandbox");
options.add_argument("--disable-gpu");
options.add_argument("--disable-crash-reporter");
options.add_argument("--disable-extensions");
options.add_argument("--disable-in-process-stack-traces");
options.add_argument("--disable-logging");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--log-level=3");
options.add_argument("--output=/dev/null");

webhook = DiscordWebhook(url='your webhook')

browser = webdriver.Chrome(options=options)
browser.get('https://www.pinnacle.com/en/baseball/matchups/')
sleep(3)


Flag = True
xd = True
arr = [ ]
arr2 = [ ]


def ConvertToUSAOdds(odds):
    if(odds > 2.00):
        return (odds - 1) * 100
    else:
        return -100 / (odds - 1) 

while(xd):
    sleep(2)
    data = browser.find_elements_by_xpath("//span[contains(@class,'style_price__15SlF')]")
    data2 = browser.find_elements_by_xpath("//span[contains(@class,'ellipsis event-row-participant style_participant__H8-ku')]")
    remove = browser.find_elements_by_xpath("//span[contains(@class,'style_row__3q4g_ style_row__2-tWa')]")

    for index in enumerate(remove):
        browser.execute_script("document.getElementsByClassName('h2h__section section')[" + index + "].remove();")

    for index, item in enumerate(data):
        if(Flag):
            Flag = False
            try:
                arr.append({ "away_odds": round(float(data[index].text), 3), "home_odds": round(float(data[index + 1].text), 3), "away": data2[index].text, "home": data2[index + 1].text })
            except:
                print("idk")
                Flag = False
        else:
            Flag = True
    
    browser.refresh()
    sleep(8)

    data = browser.find_elements_by_xpath("//span[contains(@class,'style_price__15SlF')]")
    data2 = browser.find_elements_by_xpath("//span[contains(@class,'ellipsis event-row-participant style_participant__H8-ku')]")
    remove = browser.find_elements_by_xpath("//span[contains(@class,'style_row__3q4g_ style_row__2-tWa')]")

    for index in enumerate(remove):
        browser.execute_script("document.getElementsByClassName('h2h__section section')[" + index + "].remove();")


    for index, item in enumerate(data):
        if(Flag):
            Flag = False
            try:
                arr2.append({ "away_odds": round(float(data[index].text), 3), "home_odds": round(float(data[index + 1].text), 3), "away": data2[index].text, "home": data2[index + 1].text })
            except:
                print("idk")
                Flag = False
        else:
            Flag = True


    arr3 = [item for item in arr if item not in arr2]

    if(arr3):
        for array3 in arr3:
            for array2 in arr2:
                if(array3['home'] == array2['home'] and array3['away'] == array2['away']):
                    if(array3['away_odds'] - 0.1 > array2['away_odds']):
                        #European Odds
                        #orginal_odds = array2['away_odds']
                        #new_odds = array3['away_odds']

                        #American Odds
                        orginal_odds = int(ConvertToUSAOdds(array2['away_odds']))
                        new_odds = int(ConvertToUSAOdds(array3['away_odds']))

                        embed = DiscordEmbed(title='Pinnacle Alert', description="Away Odds Increased!", color='03b2f8')
                        embed.set_timestamp()
                        embed.add_embed_field(name='Home', value=array2['home'])
                        embed.add_embed_field(name='Away', value=array2['away'])
                        embed.add_embed_field(name='Odds', value="Was " + str(orginal_odds) + " Is " + str(new_odds))

                        webhook.add_embed(embed)

                        response = webhook.execute(remove_embeds=True)    
                        sleep(5)

                    elif(array2['away_odds'] - 0.1 > array3['away_odds']):
                        #European Odds
                        #orginal_odds = array2['away_odds']
                        #new_odds = array3['away_odds']

                        #American Odds
                        orginal_odds = int(ConvertToUSAOdds(array2['away_odds']))
                        new_odds = int(ConvertToUSAOdds(array3['away_odds']))

                        embed = DiscordEmbed(title='Pinnacle Alert', description="Away Odds Decreased!", color='03b2f8')
                        embed.set_timestamp()
                        embed.add_embed_field(name='Home', value=array2['home'])
                        embed.add_embed_field(name='Away', value=array2['away'])
                        embed.add_embed_field(name='Odds', value="Was " + str(orginal_odds) + " Is " + str(new_odds))

                        webhook.add_embed(embed)

                        response = webhook.execute(remove_embeds=True)    
                        sleep(5)

                    elif(array3['home_odds'] - 0.1 > array2['home_odds']):
                        #European Odds
                        #orginal_odds = array2['away_odds']
                        #new_odds = array3['away_odds']

                        #American Odds
                        orginal_odds = int(ConvertToUSAOdds(array2['home_odds']))
                        new_odds = int(ConvertToUSAOdds(array3['home_odds']))

                        embed = DiscordEmbed(title='Pinnacle Alert', description="Home Odds Increased!", color='03b2f8')
                        embed.set_timestamp()
                        embed.add_embed_field(name='Home', value=array2['home'])
                        embed.add_embed_field(name='Away', value=array2['away'])
                        embed.add_embed_field(name='Odds', value="Was " + str(orginal_odds) + " Is " + str(new_odds))

                        webhook.add_embed(embed)

                        response = webhook.execute(remove_embeds=True)
                        sleep(5)

                    elif(array2['home_odds'] - 0.1 > array3['home_odds']):
                        #European Odds
                        #orginal_odds = array2['away_odds']
                        #new_odds = array3['away_odds']

                        #American Odds
                        orginal_odds = int(ConvertToUSAOdds(array2['home_odds']))
                        new_odds = int(ConvertToUSAOdds(array3['home_odds']))

                        embed = DiscordEmbed(title='Pinnacle Alert', description="Home Odds Decreased!", color='03b2f8')
                        embed.set_timestamp()
                        embed.add_embed_field(name='Home', value=array2['home'])
                        embed.add_embed_field(name='Away', value=array2['away'])
                        embed.add_embed_field(name='Odds', value="Was " + str(orginal_odds) + " Is " + str(new_odds))

                        webhook.add_embed(embed)

                        response = webhook.execute(remove_embeds=True)
                        sleep(5)

    arr3.clear()
    arr2.clear()
    arr.clear()
