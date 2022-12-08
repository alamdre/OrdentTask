import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Username/AppData/Local/Google/Chrome/User Data")
#driver = webdriver.Chrome(executable_path=r"C:\Users\Ade_118362\Documents\automation\chromedriver.exe")
driver = webdriver.Chrome()
#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver.maximize_window()

def test_loginEmailPositif():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("aka.alam97@gmail.com")
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Test1234")
    driver.find_element(By.XPATH, "//form/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toasted")))
    assert driver.find_element(By.CSS_SELECTOR, ".toasted").text == 'check\nMasuk berhasil'
    time.sleep(2)
    driver.get("https://bioskoponline.com/my-account")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[6]/button")))
    driver.find_element(By.XPATH, "//div[6]/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[2]/button")))
    driver.find_element(By.XPATH, "//div[2]/button").click()
    time.sleep(2)

def test_loginEmailPositif2():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("aka.alam97@gmail.com")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".text-xl:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys("aka.alam97@gmail.com")
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Test1234")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".absolute > svg").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//form/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toasted")))
    assert driver.find_element(By.CSS_SELECTOR, ".toasted").text == 'check\nMasuk berhasil'
    time.sleep(2)
    driver.get("https://bioskoponline.com/my-account")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[6]/button")))
    driver.find_element(By.XPATH, "//div[6]/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[2]/button")))
    driver.find_element(By.XPATH, "//div[2]/button").click()
    time.sleep(2)

def test_loginPonselPositif():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("087888330380")
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Test1234")
    driver.find_element(By.XPATH, "//form/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toasted")))
    assert driver.find_element(By.CSS_SELECTOR, ".toasted").text == 'check\nMasuk berhasil'
    time.sleep(2)
    driver.get("https://bioskoponline.com/my-account")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[6]/button")))
    driver.find_element(By.XPATH, "//div[6]/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[2]/button")))
    driver.find_element(By.XPATH, "//div[2]/button").click()
    time.sleep(2)

def test_loginGoogle():
    driver.get("https://bioskoponline.com/")
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.CSS_SELECTOR, ".py-2:nth-child(1)").click()
    driver.find_element(By.ID, "identifierId").send_keys("ade.kurnia.testing@gmail.com")
    driver.find_element(By.ID, "identifierId").send_keys(Keys.ENTER)
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='password']/div/div/div/input")))
    driver.find_element(By.XPATH, "//div[@id='password']/div/div/div/input").send_keys("@Test1234")
    driver.find_element(By.XPATH, "//div[@id='password']/div/div/div/input").send_keys(Keys.ENTER)
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toasted")))
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toasted")))
    assert driver.find_element(By.CSS_SELECTOR, ".toasted").text == 'check\nMasuk berhasil'
    time.sleep(2)
    driver.get("https://bioskoponline.com/my-account")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[6]/button")))
    driver.find_element(By.XPATH, "//div[6]/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[2]/div/div[2]/button")))
    driver.find_element(By.XPATH, "//div[2]/div/div[2]/button").click()
    time.sleep(2)

def test_loginFacebook():
    driver.get("https://bioskoponline.com/")
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.CSS_SELECTOR, ".py-2:nth-child(2)").click()
    driver.find_element(By.ID, "email").send_keys("ade.kurnia.testing@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("Test1234")
    driver.find_element(By.ID, "loginbutton").click()
    driver.find_element(By.CSS_SELECTOR, ".x6ikm8r").click()
    assert driver.find_element(By.CSS_SELECTOR, ".text-xxs").text == "Akses Token tidak boleh kosong."
    time.sleep(2)

def test_loginLupaKataSandi():
    driver.get("https://bioskoponline.com/")
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("aka.alam97@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".flex > .text-sm").click()
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, ".layout-forgot-wrapper .text-xl").text == 'Lupa Kata Sandi'
    time.sleep(2)

def test_loginPonselNegatif():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("6287888330380")
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, ".text-red-secondary").text == 'Nomor ponsel minimal 10 digit dan berawalan 0'

def test_loginPonselNegatif2():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("0812345")
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, ".text-red-secondary").text == 'Nomor ponsel minimal 10 digit dan berawalan 0'

def test_loginPonselNegatif3():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("08123456789012345")
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, ".text-red-secondary").text == 'Nomor ponsel minimal 10 digit dan berawalan 0'
    time.sleep(2)

def test_loginEmailNegatif():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("aka.alam97@gmail.com")
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("abcd1234")
    driver.find_element(By.XPATH, "//form/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".bg-red-secondary")))
    assert driver.find_element(By.CSS_SELECTOR, ".bg-red-secondary").text == "Email, nomor ponsel / kata sandi kamu salah."
    time.sleep(2)

def test_loginEmailNegatif2():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("ada.alam97@gmail.com")
    driver.find_element(By.XPATH, "//input[@type=\'password\']").send_keys("Test1234")
    driver.find_element(By.XPATH, "//form/button").click()
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".bg-red-secondary")))
    assert driver.find_element(By.CSS_SELECTOR, ".bg-red-secondary").text == "Email, nomor ponsel / kata sandi kamu salah"
    time.sleep(2)

def test_loginEmailNegatif3():
    driver.get("https://bioskoponline.com/")
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[3]")))
    driver.find_element(By.XPATH, "//button[3]").click()
    driver.find_element(By.NAME, "username").send_keys("aka.alam97!gmail.com")
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, ".text-red-secondary").text == 'Email harus mengandung @'
    time.sleep(2)
    driver.quit()


