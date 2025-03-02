import re
#print(dir(re))
#['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'NOFLAG',
# 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X',
# 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall',
# 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sub', 'subn', 'template'

pattern = "cookie"
sequence = " Cake and cookie"
data = re.search(pattern, sequence)  # <_sre.SRE_Match object; span=(9, 15), match='cookie'>
print(data.group())  #   'cookie'

pattern = "C"
sequence = "CookieCakeandcookie"
data = re.match(pattern, sequence)  # <_sre.SRE_Match object; span=(9, 15), match='cookie'>
print(data.group())  #   'cookie'


str = 'purple alice-b@google.com monkey dishwasher kvr@gmail.com dinesh@gmail.com'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())   #  'alice-b@google.com' (the whole match)
    print(match.groups())  #  ('alice-b', 'google.com')
    print(match.group(1)) #   'alice-b' (the username, group 1)
    print(match.group(2))


str = 'purple alice-b@google.com monkey dishwasher kvr@gmail.com dinesh@gmail.com'
match = re.findall('([\w.-]+)@([\w.-]+)', str)
print(match)
import re
email_address = "Please contact us at: support@google.com, xyz@google.com hello@yahoo.co.in"
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
print(addresses)


a="dinesh"
print(dir(a))