from selenium import webdriver
import csv

PATH = r"C:\Users\Marwan\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.amazon.in/gp/bestsellers/books/')

titles = driver.find_elements_by_xpath("//div[@class='p13n-sc-truncated']")
prices = driver.find_elements_by_xpath("//span[@class='p13n-sc-price']")
ratings = driver.find_elements_by_xpath("//a[@class='a-link-normal']")

with open(r"D:/ITI/DataExploration/DataAssignment1/amazzzon.csv", 'w', newline='', encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Booktitle','Price','Ratings'])
    for i in range(1,len(ratings)):
        csvwriter.writerow([titles[i].text, prices[i].text, ratings[i].get_attribute(name='title')])




