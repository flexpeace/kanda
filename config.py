SPECIAL_CHARACTERS = set('[~!@#$%^&*()_+{}":;\']+$')

PASSWORD_ERRORS = {
    'length': 'Length must be 8 characters',
    'uppercase': 'Password must contain a uppercase character',
    'numbers': 'Password must contain a number',
    'special': 'Password must contain a special character [~!@#$%^&*()_+{}":;\']+$',
    'nonletters': 'Password must contain a lowercase character',
}
