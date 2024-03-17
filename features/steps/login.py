from behave import *
from selenium.webdriver.common.by import By
import allure


@given(u'Masuk ke login page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")


@when(u'memasukan username dan password valid berupa "{username}" dan "{password}"')
def step_impl(context,username,password):
    context.driver.find_element(By.ID,"user-name").send_keys(username)
    context.driver.find_element(By.ID,"password").send_keys(password)


@when(u'menekan tombol login')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@id='login-button']").click()


@then(u'masuk dan menampilkan produk yang dijual')
def step_impl(context):
    try:
        assert context.driver.find_element(By.XPATH,"//a[@id='item_4_title_link']").is_displayed(),"produk tidak ditampikan"
    except AssertionError as e:
        allure.attach(str(e), name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name="Gagal Login", attachment_type=allure.attachment_type.PNG)
        raise e


@when(u'memasukan username invalid berupa "{username}"')
def step_impl(context,username):
    context.driver.find_element(By.ID,"user-name").send_keys(username)
    context.driver.find_element(By.ID,"password").send_keys("secret_sauce")


@then(u'menampilkan alert bahwa username and password not match')
def step_impl(context):
    try:
        assert context.driver.find_element(By.XPATH,"//h3[@data-test='error' and text()='Epic sadface: Username and password do not match any user in this service']").is_displayed(),"alert tidak muncul"
    except AssertionError as e:
        allure.attach(str(e), name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name="alert tidak muncul", attachment_type=allure.attachment_type.PNG)
        raise e


@when(u'memasukan password invalid berupa "{password}"')
def step_impl(context,password):
    context.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    context.driver.find_element(By.ID,"password").send_keys(password)


@when(u'tidak memasukan username')
def step_impl(context):
    context.driver.find_element(By.ID,"password").send_keys("secret_sauce")


@then(u'menampilkan alert bahwa Username is required')
def step_impl(context):
    try:
        assert context.driver.find_element(By.XPATH,"//h3[@data-test='error' and text()='Epic sadface: Username is required']").is_displayed(),"alert tidak muncul"
    except AssertionError as e:
        allure.attach(str(e), name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name="alert tidak muncul", attachment_type=allure.attachment_type.PNG)
        raise e

@when(u'tidak memasukan password')
def step_impl(context):
    context.driver.find_element(By.ID,"user-name").send_keys("standard_user")

@then(u'menampilkan alert bahwa password is required')
def step_impl(context):
    try:
        assert context.driver.find_element(By.XPATH,"//h3[@data-test='error' and text()='Epic sadface: Password is required']").is_displayed(),"alert tidak muncul"
    except AssertionError as e:
        allure.attach(str(e), name="Error Message", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.driver.get_screenshot_as_png(), name="alert tidak muncul", attachment_type=allure.attachment_type.PNG)
        raise e