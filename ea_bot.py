from lib2to3.pgen2 import driver
import random
import time
import selenium as a
import undetected_chromedriver as uc
from datetime import datetime

 
 
if __name__ == '__main__':

    driver = uc.Chrome()
    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
    
    while(1):
        try:
            club_name = driver.find_element("xpath","/html/body/main/section/section/div[1]")
            print(club_name.text)
            if ("Calin fc" in club_name.text):
                print(club_name.text)
                break
            time.sleep(10)
        except:
            print("wait for login")
    

    driver.find_element("xpath","/html/body/main/section/nav/button[3]").click()
    time.sleep(10)
    driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div/div[2]").click()
    time.sleep(10)
    
    while(1):
        try:
            try:
                make_bid = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[1]")
                if ( make_bid.text == "Make Bid"):
                    break
            except:
                print("bid not found")
            try:
                no_result_found = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div/section/div/div[2]/div/h2")
                if ( no_result_found.text == "No results found"):
                    break
            except:
                print(no_result_found.text)
            time.sleep(10)
        except:
            print("wait for bid page")

    while(1):
        now = datetime.now()
        start_time = now.strftime("%H:%M:%S")
        print(start_time)
        while(1):
            current = datetime.now()
            current_time = current.strftime("%H:%M:%S")
            start_tim = datetime.strptime(start_time, "%H:%M:%S")
            end_tim = datetime.strptime(current_time, "%H:%M:%S")
            delta = end_tim - start_tim
            sec = delta.total_seconds()
            min = int(sec / 60)
            if(min >= 1):
                break
            i = 0
            while(True):
                i+=1
                print(i)
                try:
                    detail = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li["+str(i)+"]/div")
                    if (("BUY NOW" in detail.text) and ("Expired" not in detail.text)):
                        driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]").click()
                        while(True):
                            try:
                                print("here stuck")
                                driver.find_element("xpath","//span[text()='Ok']").click()
                                time.sleep(1)
                                driver.find_element("xpath","html[1]/body[1]/main[1]/section[1]/section[1]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/div[3]/button[8]").click()
                                break
                            except:
                                print("not clickable")
                                break
                except:
                    break
            driver.find_element("xpath","/html/body/main/section/section/div[1]/button[1]").click()
            time.sleep(2)
            min_value = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input")
            mp = min_value.get_attribute('value')
            if(mp == ''):
                imp = 0
            else:
                imp = int("".join(mp.split(",")))
            buy_value = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")
            bp = buy_value.get_attribute('value')
            ibp = int("".join(bp.split(",")))
            if ((((imp +100) == ibp and (ibp <= 10000) )) or (((imp + 250) == ibp and (ibp <= 50000) and (ibp > 10000) )) or (((imp + 500) == ibp) and (ibp <= 100000) and (ibp > 50000)) ):
                driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/button").click()
                input_value = driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input")
                input_value.send_keys('1000')
                driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
                time.sleep(1)
            else:
                driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/button[2]").click()
                driver.find_element("xpath","/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
                time.sleep(1)
        time.sleep(600)



        