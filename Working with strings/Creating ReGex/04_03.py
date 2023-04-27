import re

pharse = "yahia 281 years old an mohamed 25 years old and sara is 1 years old"
print(re.sub("(yahia|mohamed) \d*", "name", pharse))
print(re.sub("(yahia|mohamed) \d*", "ahmed", pharse))
print(re.sub("(yahia|mohamed) \d*", "name", pharse, 1))
