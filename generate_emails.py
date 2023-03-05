# this will generate emails from a list of names.
# not yet capable of dealing with duplicates
# needs to be provided with full name (preferable generated via generate_names) and domain (don't include '@' - eg. 'gmail.com')
# this is best used in a for or while loop iterating over a list

def generate_emails(fullname,  domain):
    email = str(str.replace(fullname, ' ', '.').title() + '@' + domain)
    return email
