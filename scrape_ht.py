
from lds_scraper import HometeachingScraper as hs

spec = {
        'username': 'jacobp1794',
        'password': 'twinsrock1',
    }

scraper = hs(spec['username'], spec['password'])

print('Starting browser...')
scraper.open_browser()

print('Navigating to hometeaching...')
scraper.sign_in()

print('Beginning scrape...')
scraper.scrape()
#get the number of districts
print(scraper.districts)
print('data')
scraper.districts_all_to_csv()

# //*[@id="companionship-list"]/div[2]/div[1]/ul/li[2]/a
# #scraper.close()
# //*[@id="companionship-list"]/div[2]
# //*[@id="companionship-list"]/div[3]
# //*[@id="companionship-list"]
# //*[@id="organizeList"]/accordion/div/div[1]/div[2]/div
# //*[@id="organizeList"]/accordion/div/div[2]/div[2]/div

# //*[@id="companionship-list"]/div[2]
print('Scrape completed!')
# //*[@id="companionship-list"]/div[2]
