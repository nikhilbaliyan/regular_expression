import re
line = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better"
l=re.findall(r'\bB\w+', line, flags=re.IGNORECASE)
print(l)
