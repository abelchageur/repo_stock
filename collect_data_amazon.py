from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  
import numpy as np
import pandas as pd
import time

browser = webdriver.Chrome()
browser.get("https://avito.ma")

recherche = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[5]/div[1]/div/div/form/div/input')
recherche.send_keys("appartement")
time.sleep(0.2)

confirmer = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[5]/div[1]/div/button[3]')
confirmer.click()
time.sleep(0.2)

def get_element_text(xpath):
    try:
        element = browser.find_element(By.XPATH, xpath)
        return element.text
    except NoSuchElementException:
        return "NaN"
    
    
    
appart_list = [] 
for n in range(2,5):

    apartment_links = []
    link_elements = browser.find_elements(By.CSS_SELECTOR, '.sc-1nre5ec-1.crKvIr.listing a')  
    for link_element in link_elements:
        href = link_element.get_attribute('href')
        if href:
            apartment_links.append(href)
    
    for link in apartment_links:
        browser.get(link)  
        time.sleep(0.5)
        
        try:
            path_chambre = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div/span").text
        except NoSuchElementException:
            try:
                path_chambre = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div/span").text
            except NoSuchElementException:
                path_chambre = "NaN"    

        try:
            path_douches = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div/span").text
        except NoSuchElementException:
            try:
                path_douches = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span").text
            except NoSuchElementException:
                path_douches = "NaN"  



        appart_dict = {
            "titre_appart": get_element_text('//*[@id="__next"]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h1'),
            "localisation": get_element_text('//*[@id="__next"]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]'),
            "prix": get_element_text('//*[@id="__next"]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p'),
            "nombre_chambre": path_chambre,
            "nombre_douches": path_douches,
            "Surface_habitable": get_element_text("//span[text()='Surface habitable']/following-sibling::span"),
            "Type": get_element_text("//span[text()='Type']/following-sibling::span"),
            "Secteur": get_element_text("//span[text()='Secteur']/following-sibling::span"),
            "Salons": get_element_text("//span[text()='Salons']/following-sibling::span"),
            "Étage": get_element_text("//span[text()='Étage']/following-sibling::span"),
            "Âge_du_bien": get_element_text("//span[text()='Âge du bien']/following-sibling::span"),
            "link": link
        }
        appart_list.append(appart_dict)
        time.sleep(0.8)
    browser.get(f"https://www.avito.ma/fr/maroc/appartements/appartement--%C3%A0_vendre?o={n}") 
    time.sleep(0.7)
    
    
df = pd.DataFrame(appart_list)
df.head()

df.to_csv('appartements.csv', index=False)
print("Data saved to appartements.csv")
browser.quit()