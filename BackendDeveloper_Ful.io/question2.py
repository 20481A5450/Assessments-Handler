import re
import requests

def get_website_details(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            social_links = re.findall(r'href="(https?://www\.facebook\.com[^"]*|https?://www\.linkedin\.com[^"]*)"', content)
            email = re.findall(r'[\w\.-]+@[\w\.-]+', content)
            contact_numbers = re.findall(r'\+\d{1,3} \d{3} \d{3} \d{4}', content)
            
            return social_links, email, contact_numbers
        else:
            print("Error: Unable to fetch website content.")
            return None, None, None
    except Exception as e:
        print("An error occurred:", str(e))
        return None, None, None

# Get user input for the website URL
website_url = input("Enter the website URL: ")

# Get website details
social_links, email, contact_numbers = get_website_details(website_url)

if social_links:
    print("Social links:")
    for link in social_links:
        print(link)
else:
    print("No social links found.")

if email:
    print("Email:")
    for e in email:
        print(e)
else:
    print("No email found.")

if contact_numbers:
    print("Contact:")
    for number in contact_numbers:
        print(number)
else:
    print("No contact numbers found.")
