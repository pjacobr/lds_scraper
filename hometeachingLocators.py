from selenium.webdriver.common.by import By


class DistrictLocators:
    """A container class for locators necessary for navigation through amazon's website"""
    DISTRICTS = (By.XPATH, '//*[@id="organizeList"]/accordion/div/div')
    DISTRICT_LEADER = (By.XPATH, '//*[@id="organizeList"]/accordion/div/div[1]/div[2]/div/div[1]/a')
    # //*[@id="organizeList"]/accordion/div/div[1]/div[2]/div/div[1]/a
    # //*[@id="organizeList"]/accordion/div/div[2]/div[2]/div/div[1]/a
    # //*[@id="organizeList"]/accordion/div/div[3]/div[2]/div/div[1]/a
    # //*[@id="organizeList"]/accordion/div/div[4]/div[2]/div/div[1]/a
    #
    COMPANIONSHIP = (By.XPATH, './/*[@id="companionship-list"]/div')
    # //*[@id="companionship-list"]/div[3]/div[1]
    # //*[@id="companionship-list"]/div[4]/div[1]/ul
    COMPANION_1 = (By.XPATH, '//*[@id="timePeriodForm"]')
    # Beatty, Connor
    # //*[@id="companionship-list"]/div[2]/div[1]/ul/li[1]/a
    # Billings, Joseph
    # //*[@id="companionship-list"]/div[2]/div[1]/ul/li[2]/a
    # Burton, Matthew
    # //*[@id="companionship-list"]/div[3]/div[1]/ul/li[1]/a
    # Mautz, Adam
    # //*[@id="companionship-list"]/div[3]/div[1]/ul/li_
    COMPANION_2 = (By.XPATH, '//*[@id="timePeriodForm"]')
    HOMETEACHEES = (By.ID, 'a-autoid-1')
    # //*[@id="companionship-list"]/div[2]/div[3]/div[3]/div[1]/a
    # //*[@id="companionship-list"]/div[2]/div[3]/div[5]/div[1]/a
    # //*[@id="companionship-list"]/div[2]/div[3]/div[4]/div[1]/a
    MONTHS = (By.PARTIAL_LINK_TEXT, 'View All Orders:')
    TAUGHT = (By.XPATH, '//*[@id="companionship-list"]/div[2]/div[3]/div[3]/div[2]/div[1]/div/span[11]/span'

    # def get_invoice_link(self, which):
    #     return (By.XPATH, '//*[@id="ordersContainer"]/div[' + str(which + 1) + ']/div[1]/div/div/div/div[2]/div[2]/ul/a[2]')
    # def get_invoice_link_business(self, which):
    #     return (By.XPATH, '//*[@id="ordersContainer"]/div[' + str(which + 1) + ']/div[1]/div/div/div/div[2]/div[2]/ul/span[1]/a')
    # def get_year_link(self, year):
    #     return (By.LINK_TEXT, str(year))

class SignInLocators:
    """A container class for locators on the sign-in page"""
    EMAIL_FIELD = (By.ID, 'IDToken1')
    PASS_FIELD = (By.ID, 'IDToken2')
    SUBMIT_BTN = (By.NAME, 'Login.Submit')
