from src.POM_Unit_Tests.Locators import Locators
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.movieNameText_name = Locators.Locators.movieNameText_name
        self.searchBtn_name = Locators.Locators.searchBtn_name

    def enterMovieName(self, movie_text):
        self.driver.find_element_by_name(self.movieNameText_name).clear()
        self.driver.find_element_by_name(self.movieNameText_name).send_keys(movie_text)

    def clickSearch(self):
        self.driver.find_element_by_name(self.searchBtn_name).click()
