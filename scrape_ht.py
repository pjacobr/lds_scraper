from lds_scraper import HometeachingScraper as hs
username = str(input("what is your username?"))
password = str(input("What is your password?"))
spec = {
    'username': username,
    'password': password,
}

scraper = hs(spec['username'], spec['password'])

print('Starting browser...')
scraper.open_browser()

print('Navigating to hometeaching...')
scraper.sign_in()

print('Beginning scrape...')
scraper.scrape()

# get the number of districts
print(scraper.districts)
print('data')
#scraper.by_district_to_csv()
#scraper.companionships_to_csv()
scraper.csv_database_format()
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
