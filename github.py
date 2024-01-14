from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from dotenv import load_dotenv
import os
load_dotenv()
# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')


def scrape_github_readme(username,repo_name):
    # Set up Chrome WebDriver (adjust the executable_path accordingly)
    driver = webdriver.Chrome(options = options)
    try:
        repository_url = f'https://github.com/{username}/{repo_name}'
        driver.get(repository_url)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.markdown-body')))
        #time.sleep(10)  # Adjust sleep duration if needed

        # Find the README content 
        readme_content = driver.find_element(By.CSS_SELECTOR, '.repository-content .markdown-body')
        
        with open("final_github_output.txt", "a" if open("final_github_output.txt").read() else "w") as output_file:
            # Check if file exists, use "a" for append, "w" for create
            output_file.write(f"--- Repository: {repo_name.strip()} ---\n")
            output_file.write(readme_content.text + "\n\n")
            output_file.write("-" * 50 + "\n\n")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser
        driver.quit()

def scrape_readmes_from_file(file_path,username):
    print(f"Navigating to given GitHub repository(s)...")
    try:
        with open(file_path, 'r') as file:
            # Read repository names line by line
            repository_names = file.readlines()

            threads = []
            for name in repository_names:
                t = threading.Thread(target=scrape_github_readme, args=[username,name])
                t.start()
                threads.append(t)
                # Call the function to scrape README for each repository

    except Exception as e:
        print(f"Error reading file: {e}")
    for t in threads: 
        t.join()

def main():
    # Example: File containing repository names
    file_path = 'github_repositories.txt'
    username = os.environ.get("NAME")
    scrape_readmes_from_file(file_path,username)
    print("Closing the browser(s)...")

if __name__ == '__main__':
    main()