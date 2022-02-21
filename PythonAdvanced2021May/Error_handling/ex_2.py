import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()
    if email == 'End':
        break

    result = re.search(r'(^|(?<=\s))[A-Za-z0-9]{5,}@[A-Za-z1-9]+(.com|.bg|.net|.org)(\.w+)?', email)
    first_part = re.search(r'(^|(?<=\s))[A-Za-z0-9]{5,}', email)
    valid_domains = {'com', 'bg', 'org', 'net'} & set(email.split('.'))

    if not first_part:
        raise NameTooShortError('Name must be more than 4 characters')

    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    elif not valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    else:
        print('Email is valid')
