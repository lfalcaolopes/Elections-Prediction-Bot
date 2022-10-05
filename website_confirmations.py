from selenium.webdriver.common.by import By
from time import sleep

class WebsiteConfirmation:
    def __init__(self, driver):
        self.next_btn = "/html/body/app-root/ion-app/ion-router-outlet/ng-component/ion-footer/div/ion-button"
        self.terms = "/html/body/app-root/ion-app/ion-router-outlet/ng-component/ion-content/div/div[2]/ion-button"
        self.driver = driver

    def nextClick(self):
        next_page = self.driver.find_element(By.XPATH, self.next_btn)
        next_page.click()

        sleep(0.5)

    def termsClick(self):
        terms = self.driver.find_element(By.XPATH, self.terms)
        terms.click()

        sleep(1)

    def websiteConfirmations(self):
        self.nextClick()
        self.nextClick()
        self.termsClick()
