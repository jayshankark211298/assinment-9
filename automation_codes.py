"""
Selenium Web Scraping Class for Automating Web Actions

"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class ShankarTestingClass :
    # Initialize the class with the URL and set up the Chrome WebDriver

   def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




   def booting_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False



   def shutdown(self):
       self.driver.quit()
    # Method to log in to the website with provided username and password
   def login(self, username, password):
       if self.booting_function():
           try:
               # Locate the username and password fields and the login button
               username_field = self.driver.find_element(By.ID, "user-name")
               password_field = self.driver.find_element(By.ID, "password")
               login_button = self.driver.find_element(By.ID, "login-button")
               # Enter the username and password and click the login button

               username_field.send_keys("standard_user")
               password_field.send_keys("secret_sauce")
               login_button.click()

               # Wait for the page to load
               time.sleep(5)
               return True
           except Exception as e:
               print(f"ERROR : {e}")
               return False
       else:
           return False
    # Method to fetch the title of the webpage

   def fetch_title(self):
       if self.booting_function() == True:
           return self.driver.title
       else:
           return False

    # Method to fetch the current URL of the webpage

   def fetch_url(self):
       if self.booting_function():
           return self.driver.current_url
       else:
           return False

    # Method to fetch the HTML source of the webpage

   def fetch_webpage(self):
       if self.booting_function():
           return self.driver.page_source
       else:
           return False


if __name__ == "__main__":
   ShankarTestingClass = ShankarTestingClass("https://www.guvi.in")
   ShankarTestingClass.booting_function()
   print(ShankarTestingClass.fetch_title())
   print(ShankarTestingClass.fetch_url())
   print(ShankarTestingClass.fetch_webpage())
   ShankarTestingClass.shutdown()


