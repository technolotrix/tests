from element import BasePageElement

from locators import HomePageLocators
from locators import PageHeaderLocators
from locators import PageFooterLocators

from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def is_title_matches(self):
        return "LNS | QA Consulting" in self.driver.title

    def is_copyright_matches(self):
        return "Lauren Nicole Smith 2015" in self.driver.page_source

    def click_quote_button(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_QUOTE_BUTTON)
        element.click()
        return "/contact" in self.driver.current_url

    def hover_over_nav(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_HOVER_NAV)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click_home_button(self):
        element = self.driver.find_element(*PageHeaderLocators.GET_HOME_BUTTON)
        element.click()
        return "/" in self.driver.current_url

    def click_projects_link(self):
        self.hover_over_nav()
        element = self.driver.find_element(*PageHeaderLocators.GET_PROJECTS_LINK)
        element.click()
        return "/projects" in self.driver.current_url

    def click_services_link(self):
        self.hover_over_nav()
        element = self.driver.find_element(*PageHeaderLocators.GET_SERVICES_LINK)
        element.click()
        return "/services" in self.driver.current_url

    def click_about_link(self):
        self.hover_over_nav()
        element = self.driver.find_element(*PageHeaderLocators.GET_ABOUT_LINK)
        element.click()
        return "/about" in self.driver.current_url

    def click_github_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_GITHUB_BUTTON)
        element.click()
        return "https://github.com/technolotrix" in self.driver.current_url

    def click_linkedin_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_LINKEDIN_BUTTON)
        element.click()
        return "https://www.linkedin.com/in/nicolelns" in self.driver.current_url

    def click_twitter_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_TWITTER_BUTTON)
        element.click()
        return "" in self.driver.current_url

    def click_gplus_button(self):
        element = self.driver.find_element(*PageFooterLocators.GET_GPLUS_BUTTON)
        element.click()
        return "" in self.driver.current_url

    def click_html5up_link(self):
        element = self.driver.find_element(*PageFooterLocators.GET_HTML5UP_LINK)
        element.click()
        return "http://html5up.net" in self.driver.current_url