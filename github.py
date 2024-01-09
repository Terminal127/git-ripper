from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_github_readme(repository_name):
    # Set up Chrome WebDriver (adjust the executable_path accordingly)
    driver = webdriver.Chrome()

    try:
        repository_url = f'https://github.com/Shinyzenith/{repository_name}'
        print(f"Navigating to the GitHub repository: {repository_url}")
        driver.get(repository_url)
        time.sleep(10)  # Adjust sleep duration if needed

        # Find the README content
        readme_content = driver.find_element(By.CSS_SELECTOR, '.repository-content .markdown-body')

        # Save the README content to the output file
        with open("final_github_output.txt", "a" if open("final_github_output.txt").read() else "w") as output_file:
            # Check if file exists, use "a" for append, "w" for create
            output_file.write(f"--- Repository: {repository_name} ---\n")
            output_file.write(readme_content.text + "\n")
            output_file.write("-" * 50 + "\n")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the browser
        print("Closing the browser...")
        driver.quit()

def scrape_readmes_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read repository names line by line
            repository_names = file.readlines()

            for name in repository_names:
                # Call the function to scrape README for each repository
                scrape_github_readme(name.strip())

    except Exception as e:
        print(f"Error reading file: {e}")

# Example: File containing repository names
file_path = 'repository_names.txt'
scrape_readmes_from_file(file_path)

