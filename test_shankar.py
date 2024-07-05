"""
test_shankar.py
Pytest test file which comprises various positive and negative test-cases
"""

from automation_codes import ShankarTestingClass
import  pytest


url = "https://www.saucedemo.com/"
shankar = ShankarTestingClass(url)


def test_positive_url():
   testing_url = "https://www.saucedemo.com/"
   assert shankar.fetch_url() == testing_url
   print("SUCCESS : URL is correct")




def test_negative_url():
   testing_url = "https://www.zenclass.in/class"
   assert shankar.fetch_url() == testing_url
   print("SUCCESS : URL is correct")


def test_closing():
   shankar.shutdown()
