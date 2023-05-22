from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_scores_service(web_url="http://127.0.0.1:5000/"):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='113.0.5672.63').install()))
    driver.get(web_url)
    score = driver.find_element(By.ID, "score").text
    score = int(score)
    if score > 1 & score < 1000:
        return True
    else:
        return False
def main_function(test_score_service):
    try:
        test_scores_service()
    except Exception:
        pass


main_function(test_scores_service())
