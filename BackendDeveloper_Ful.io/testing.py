import requests
import re

# Define regex patterns for each technology
patterns = {
    "jQuery": r'<script[^>]*src=["\'][^>]*jquery[^>]*["\'][^>]*></script>',
    "React.js": r'<script[^>]*src=["\'][^>]*react[^>]*["\'][^>]*></script>',
    "WooCommerce": r'woocommerce',
    "Bootstrap": r'<link[^>]*href=["\'][^>]*bootstrap[^>]*["\'][^>]*>',
    "Shopify": r'shopify',
    "Next.js": r'<script[^>]*src=["\'][^>]*next[^>]*["\'][^>]*></script>',
    "Materialize CSS": r'<link[^>]*href=["\'][^>]*materialize[^>]*["\'][^>]*>',
    "PHP": r'php<\?php\s.*?\?\>',
    "Python": r'\<\%python\%.*?\%\>',
    "Google Maps": r'Google Maps | \<script\ src="https:\/\/maps\-api\.google\.com\/maps\/api\/js\?key=AIzaSy.*?"></script>'
}

# Sample website URLs
sample_websites = {
    "jQuery": "https://jquery.com/",
    "React.js": "https://react.dev/",
    "WooCommerce": "https://woocommerce.com/",
    "Bootstrap": "https://getbootstrap.com/",
    "Shopify": "https://www.shopify.com/",
    "Next.js": "https://nextjs.org/",
    "Materialize CSS": "https://materializecss.com/",
    "PHP": "https://www.php.net/",
    "Python": "https://www.python.org/",
    "Google Maps": "https://www.google.com/maps/"
}

# Test the patterns on each sample website
for tech, pattern in patterns.items():
    url = sample_websites[tech]
    response = requests.get(url)
    if re.search(pattern, response.text):
        print(f"{tech} detected on {url}.")
    else:
        print(f"{tech} not detected on {url}.")
