from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chromedriver ="/Users/Lenovo/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.twitter.com')

a = browser.find_element_by_xpath('//input[@autocomplete="username"]')
a.click()
a.send_keys('Type Your Twitter Email here')
sleep(2)
b = browser.find_element_by_xpath('//input[@type="password"]')
b.click()
b.send_keys('Pasword')
sleep(2)
c = browser.find_element_by_xpath('//input[@value="Log in"]')
c.click()
sleep(2)
d = browser.find_element_by_xpath('//div[text()="What’s happening?"]')
d.click()
sleep(1)
e = browser.find_element_by_xpath('//div[@aria-labelledby="tweet-box-home-timeline-label"]')
f= browser.find_element_by_xpath('//span[@class="button-text tweeting-text"]')
ayush = ["Your Tweets are here","Your Tweets are here","Your Tweets are here","Your Tweets are here","Your Tweets are here"]
for p  in range(len(ayush)):
	e.send_keys(ayush[p])
	f.click()
	sleep(2)
	d = browser.find_element_by_xpath('//div[text()="What’s happening?"]')
	d.click()
	e = browser.find_element_by_xpath('//div[@aria-labelledby="tweet-box-home-timeline-label"]')
	f= browser.find_element_by_xpath('//span[@class="button-text tweeting-text"]')
	





