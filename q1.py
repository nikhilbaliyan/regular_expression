import re
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
l=re.findall(pattern, emails, flags=re.IGNORECASE)
print(l)