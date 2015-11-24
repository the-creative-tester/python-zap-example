from lettuce import step, world
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to Gruyere')
def step_impl(step):
    world.driver.get("http://google-gruyere.appspot.com/start")
    
@step('I choose to Agree & Start')
def step_impl(step):
	world.driver.find_element(By.LINK_TEXT, "Agree & Start").click()

@step('I am taken to "([^"]*)"')
def step_impl(step, page_title):
	assert_equal(world.driver.title, page_title)

@step('I choose to Sign Up')
def step_impl(step):
	world.driver.find_element(By.LINK_TEXT, "Sign up").click()

@step('I choose to Create Account with user name "([^"]*)" and password "([^"]*)"')
def step_impl(step, user_name, password):
    world.driver.find_element(By.NAME, "uid").send_keys(user_name)
    world.driver.find_element(By.NAME, "pw").send_keys(password)
    world.driver.find_element(By.XPATH, "//input[@value='Create account']").click()

@step('I choose to Sign In')
def step_impl(step):
	world.driver.find_element(By.LINK_TEXT, "Sign in").click()

@step('I choose to Login with user name "([^"]*)" and password "([^"]*)"')
def step_impl(step, user_name, password):
    world.driver.find_element(By.NAME, "uid").send_keys(user_name)
    world.driver.find_element(By.NAME, "pw").send_keys(password)
    world.driver.find_element(By.XPATH, "//input[@value='Login']").click()
