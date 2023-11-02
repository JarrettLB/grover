from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests

# Function to scrape the article content from a URL
def scrape_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article = soup.find('article')  # Adjust this selector to match the structure of the webpage
        if article:
            return article.get_text()
        else:
            return None
    except Exception as e:
        print(f"Error while scraping: {str(e)}")
        return None

# Main function
def main():
    url = input("Enter the URL of the article: ")
    content = scrape_article(url)

    if content:
        # Configure Selenium to run Firefox in headless mode
        firefox_options = Options()
        firefox_options.headless = False

        # Start a web browser (Firefox) in headless mode
        driver = webdriver.Firefox(options=firefox_options)

        # Open the Grover website
        driver.get("https://grover.allenai.org/detect")
        driver.implicitly_wait(10)

        # Locate the text box element and input the article content
        text_box = driver.find_elements(By.XPATH, "/html/body/div/section/main/div/form/textarea")  # Replace with the actual HTML element ID
        text_box.send_keys(content)

        # Submit the form (you may need to locate the submit button and click it)
        submit_button = driver.find_elements(By.XPATH, "/html/body/div/section/main/div/form/div/button")  # Replace with the actual HTML element ID
        submit_button.click()

        # Wait for the analysis to complete (you may need to adjust the wait time)
        driver.implicitly_wait(10)

        # Get the result from the website (you may need to locate the result element)
        result_element = driver.find_element_by_id(".article-body__content__17Yit")  # Replace with the actual HTML element ID
        result = result_element.text
        print(result)

        # Close the web browser
        driver.quit()

if __name__ == "__main__":
    main()

#https://www.reuters.com/world/middle-east/gaza-says-israels-strikes-refugee-camp-kill-more-than-195-people-2023-11-02/
