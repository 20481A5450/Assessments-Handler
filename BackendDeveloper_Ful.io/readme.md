# Full.io-Backend-Developer-Internship
# Full.io-Backend-Developer-Internship
# README: Technical Questions and Solutions

This README provides explanations and solutions for the technical questions given as part of an assessment. The solutions are written in Python and aim to fulfill the specified requirements for each question.

## Task 1: Valid Contact Number Checker
### Problem Statement:
Check if a given contact number is valid using regular expressions. Different countries have varying formats for contact numbers. Examples include formats like "2124567890," "(212)456-7890," and "+12124567890." The goal is to determine the validity of these numbers by analyzing their representations.

### Approach:
To solve this task, regular expressions are used to match valid contact number patterns. The regular expression pattern is designed to capture common variations in contact number formats, including hyphens, parentheses, and country codes.

### Solution Explanation:
The `is_valid_contact_number` function uses regular expressions to match the given patterns. The function takes a contact number as input and returns `True` if the number matches a valid pattern; otherwise, it returns `False`.

## Task 2: Website Information Extractor
### Problem Statement:
Extract social links, email addresses, and contact details from a given website's HTML content. The input is a website URL, and the output should include social links, email addresses, and contact details.

### Approach:
The solution uses the `requests` library to fetch the website's HTML content and the `BeautifulSoup` library for HTML parsing. Regular expressions and HTML element searches are used to extract social links, email addresses, and contact details.

### Solution Explanation:
The `get_social_links`, `get_email`, and `get_contact` functions are responsible for extracting social links, email addresses, and contact details, respectively. The main function prompts the user for a website URL, fetches the HTML content, and then utilizes the extraction functions to obtain the desired information.

## Task 3: One-Line Answers
### Problem Statement:
Answer questions related to Linux terminal usage and server administration concisely in one-line responses.

### Approach:
The provided questions are answered directly, concisely, and accurately in a single line each.

### Solution Explanation:
Each question is answered with a short sentence that addresses the query or topic.
---
These solutions demonstrate a clear understanding of the problem statements and the ability to apply programming skills to address the given tasks. Regular expressions, HTML parsing, and Linux command line knowledge are utilized effectively to provide accurate and efficient solutions.

Please feel free to reach out if you have any further questions or need additional information.

---

This README file explains the approach and solutions for each of the given tasks, highlighting your ability to solve technical problems and showcase your skills. Make sure to adjust the explanations according to your actual implementations if there are any variations.
