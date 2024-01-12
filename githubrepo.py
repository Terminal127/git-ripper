from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')


def search_github_repositories(username, itemprop_value, output_file='github_repositories.txt'):
    # Set up Chrome WebDriver (adjust the executable_path accordingly)
    driver = webdriver.Chrome(options = options)

    try:
        # Navigate to GitHub and perform the search
        search_query = f'site:github.com {username} itemprop:"{itemprop_value}"'
        search_url = f'https://github.com/Terminal127?tab=repositories'
        print(f"Navigating to the GitHub search results for {username}'s repositories with itemprop='{itemprop_value}'")
        driver.get(search_url)
        time.sleep(10)  # Adjust sleep duration if needed

        # Find and print the search results
        search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')

        # Open a file in write mode
        with open(output_file, 'w', encoding='utf-8') as file:
            for result in search_results:
                repo_name = result.text.replace(" Public", "")
                if repo_name != "Footer navigation":
                    file.write(f"{repo_name}\n")
            

        print(f"Search results saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser
        print("Closing the browser...")
        driver.quit()

# Example: Search for repositories with itemprop='remote codeRepository' for user 'Terminal127'
search_github_repositories('Terminal127', 'remote codeRepository')
