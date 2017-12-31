########################SELENIUM##################################################
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#################################################################################
from hometeachingLocators import DistrictLocators as DL, SignInLocators as SL
from hometeaching import District, Hometeacher, Hometeachee, Companionship
from urls import URLS
import datetime as dt
import unicodedata
import platform
import datetime
import csv


class HometeachingScraper:

    months = {1: ('January', 'Jan'),
              2: ('February', 'Feb'),
              3: ('March', 'Mar'),
              4: ('April', 'Apr'),
              5: ('May', 'May'),
              6: ('June', 'Jun'),
              7: ('July', 'Jul'),
              8: ('August', 'Aug'),
              9: ('September', 'Sept'),
              10: ('October', 'Oct'),
              11: ('November', 'Nov'),
              12: ('December', 'Dec')
              }

    def __init__(self, email, pass_word, csv_folder='csvs/'):
        date = dt.datetime.now()
        self.driver = None
        self.wait = None
        self.current_month = str(date.month)
        self.current_year = str(date.year)
        self.current_day = str(date.day)
        self.email = email
        self.pass_word = pass_word
        self.csv_folder = csv_folder
        self.scrape_started = False
        self.scrape_finished = False
        self.districts = []

    def get_csv_name(self, purpose=None):
        csv_name = 'hometeaching' + \
                   + '-' + self.current_month \
                   + '-' + self.current_day \
                   + '-' + self.current_year
        if purpose is not None:
            csv_name += '-' + purpose
        return csv_name

    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URLS.HOMETEACHING_PAGE)
        self.wait = WebDriverWait(self.driver, 10)

    def close(self):
        self.driver.quit()
        self.csv_file.close()

    def scrape(self):
        try:
            element = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(DL.DISTRICTS))
        finally:
            pass

        districts_len = self.driver.find_elements(*DL.DISTRICTS)
        # print(districts_len)
        # Add the district leaders to the districts
        for i in range(1, len(districts_len) + 1):
            district_leader = self.driver.find_element(
                *(By.XPATH, '//*[@id="organizeList"]/accordion/div/div[' + str(i) + ']/div[2]/div/div[1]/a')).text
            self.districts.append(District(district_leader=district_leader))
        # Look for the companionships within the district and add all that information to the district
        for i in range(len(districts_len)):
            companionships = districts_len[i].find_elements(*DL.COMPANIONSHIP)
            companionships = companionships[1:]
            for companionship in companionships:
                # extract the text from the web find_element
                # TODO: This is where I am going to want to pull out the hometaught data.
                companionship = companionship.text.split('\n')[:-1]
                comp_names = companionship[0].split(' ')
                # get the comp info
                comp = Companionship()
                # Add the hometeaching companionship
                for k in range(0, len(comp_names), 2):
                    # take off the trailing comma
                    comp_names[k] = comp_names[k][:-1]
                    f_name = comp_names[k + 1]
                    l_name = comp_names[k]
                    hometeacher = Hometeacher(f_name, l_name)
                    comp.companions.append(hometeacher)
                # Add the hometeachees
                for k in range(1, len(companionship)):
                    names = companionship[k].split(',')
                    l_name = names[0]
                    f_name = names[1]
                    comp.hometeachees.append(Hometeachee(f_name, l_name))
                # Add the companionship to the district
                self.districts[i].add_companionship(comp)

    def print_data(self):
        for district in self.districts:
            print(district.to_string())

    def by_district_to_csv(self):

        csv_headers = [
            'District Leader',
            'Companionship',
            'Assignment',
            'Home taught',
            'Hometeaching Percentage'
        ]
        months = [self.months[i][1] for i in range(1, 13)]
        csv_headers.extend(months)

        with open(self.csv_folder + self.get_csv_name('by_district'), 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            self.write_row(writer, csv_file, csv_headers)
            for district in self.districts:
                self.write_row(writer, csv_file, [district.district_leader])
                for companionship in district.companionships:
                    for companion in companionship.companions:
                        self.write_row(writer, csv_file, ['\t', companion.get_name()])
                    for hometeachee in companionship.hometeachees:
                        self.write_row(writer, csv_file,
                                       ['\t', '\t', hometeachee.get_name()])  # TODO: ADD in hometeaching here

    def companionships_to_csv(self):
        csv_headers = [
            'Companionship',
            'Assignment',
            'Hometeaching Percentage'

        ]

        with open(self.csv_folder + self.get_csv_name('companionships'), 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for district in self.districts:
                for companionship in district.companionships:
                    for companion in companionship.companions:
                        self.write_row(writer, csv_file, [companion.get_name()])
                    for hometeachee in companionship.hometeachees:
                        self.write_row(writer, csv_file,
                                       ['\t', hometeachee.get_name()])  # TODO: ADD in hometeaching here

    def asciify(self, row):
        try:
            return [unicodedata.normalize('NFKD', datum).encode('ascii', 'ignore') for datum in row]
        except TypeError:
            return row

    def sign_in(self):
        email_field = self.driver.find_element(*SL.EMAIL_FIELD)
        pass_word_field = self.driver.find_element(*SL.PASS_FIELD)
        submit_btn = self.driver.find_element(*SL.SUBMIT_BTN)
        email_field.clear()
        email_field.send_keys(self.email)
        pass_word_field.clear()
        pass_word_field.send_keys(self.pass_word)
        submit_btn.click()

    def write_row(self, writer, csv_file, row):
        row = self.asciify(row)
        # print(''.join(row))
        writer.writerow(row)
        csv_file.flush()
