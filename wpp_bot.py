import selenium.common.exceptions as SeleniumEXC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WhatsBot:
    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/edu/Downloads/chromedriver_win32/chromedriver.exe')
        bot = self.driver
        bot.get('https://web.whatsapp.com/')

    def get_chat(self, who):
        bot = self.driver
        is_logged_in_locator = '/html/body/div[1]/div/div/div[3]/div/div[1]'
        print('Waiting for QR code scan...')

        try:
            WebDriverWait(bot, 60).until(EC.presence_of_element_located((By.XPATH, is_logged_in_locator)))  # waits for the user to scan the QR code
            print('QR code found!')
        except SeleniumEXC.TimeoutException:
            print('QR code not found, try again.')
            exit()

        try:
            chat = bot.find_element_by_xpath(f"//span[@title='{who}']")
            chat.click()
        except SeleniumEXC.NoSuchElementException:
            print('Wrong chat name, try again.')
            exit()

        msg_box = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]')
        msg_box.click()
        return msg_box

    def send_message(self, message, msg_box):
        while True:
            try:
                msg_box.send_keys(message)
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
                break
            except SeleniumEXC.NoSuchElementException:
                continue


bot = WhatsBot()
chat = bot.get_chat('ororwofnwogn')

for i in range(10):
    message = f' bot: oi to testando {i+1}'
    bot.send_message(message, chat)

print("Finished sending the messages.")
