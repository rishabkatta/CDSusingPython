_author = 'sps'

"""
CSCI-603: String/File/List/Dictionary Lecture (week 5)
Author: Sean Strout @ RIT CS

This is a demonstration program for strings, files, lists and dictionaries.
It takes a comma separated file (CSV) that contains basic information about
individuals (one per line):

id,first_name,last_name,email,country,ip_address

For each individual, it displays formatted information about them:

ID: #
    Name: {FirstInitial} . {LastName}
    Username: {Username}
    Domain: {Domain}
    Country Code: {CountryCode}
    IP (hex): {IP}

This data was generated randomly by the site: https://www.mockaroo.com/
"""

import sys      # stderr

# CONSTANTS

# positions of fields in CSV data file
ID = 0
FIRST_NAME = 1
LAST_NAME = 2
EMAIL = 3
COUNTRY = 4
IP = 5

# country code mappings where key(str)={Full Country Name} and associated
# value(str)= {3 digit ISO}
COUNTRY_CODES = {
    'Bangladesh' : 'BGD',
    'China' : 'CHN',
    'Dominican Republic' : 'DOM',
    'Greece' : 'GRC',
    'Kazakhstan' : 'KAZ',
    'Nigeria' : 'NGA',
    'Philippines' : 'PHL',
    'Portugal' : 'PRT',
    'Ukraine' : 'UKR'
}

def printName(firstName, lastName):
    """
    Print the name of the person in the format
    <TAB>Name: <first initial>. <last name>
    :param firstName (str): The first name
    :param lastName (str): The last name
    :return: None
    """

    # strip off the first initial
    firstInitial = firstName[:1]

    # concatenate together and print
    name = firstInitial + '. ' + lastName
    print('\tName:', name)

def printEmail(email):
    """
    Print the email information for the person in the format
    <TAB>Username: <user name>
    <TAB>Domain: <domain name>
    :param email (str): The full email address
    :return: None
    """

    # find the location of the @ symbol
    atPos = email.index('@')

    # the username is up to but not including the @ symbol
    username = email[:atPos]
    print('\tUsername:', username)

    # the domain is everything after the @ symbol
    domain = email[atPos+1:]
    print('\tDomain:', domain)

def printCountryCode(country):
    """
    Print the country code (if found). Format:
    <TAB>Country Code: <country code>
    or
    <TAB>Country Code: **** NOT FOUND ****
    :param country (str): The full name of the country
    :return: None
    """

    # if the country is in the dictionary, display the code, otherwise
    # indicate that it could not be found
    if country in COUNTRY_CODES:
        print('\tCountry Code:', COUNTRY_CODES[country])
    else:
        print('\tCountry Code:', '*** NOT FOUND ***')

def printIP(ip):
    """
    Print the IP address in hex.
    :param ip (str): The ip address as '#.#.#.#' where
    '#' is a decimal number string. Print it in the same
    form except that the four numbers will be in base 16.
    :return: None
    """

    # split the 4 bytes (as strings) into a list, e.g.:
    #   ip -> '95.126.14.81'
    #   bytes -> ['95', '126', '14', '81']
    bytes = ip.split('.')

    # build the hex address, starting with the '0x'
    address = '0x'

    # loop over the list of byte strings
    for byte in bytes:
        # convert the byte string to hex (by first converting
        # the string byte to an integer), e.g.:
        #   byte -> '95'
        #   int(byte) -> 95
        #   hex(95) -> '0x5f'
        hexStr = hex(int(byte))

        # strip off the leading '0x' because we are building this into
        # the address string
        hexStr = hexStr[2:]

        # pad string w/ a leading 0 if only 1 digit (a value less than 16),
        # e.g.:
        #     hexStr -> 'd' -> '0d'
        if (len(hexStr) != 2):
            hexStr = '0' + hexStr

        # concatenate to full address:
        # address -> '0x'
        # hexStr -> '0d'
        # address -> '0x0d'
        address += hexStr

    print('\tIP (hex):', address)


def processFile(fileName):
    """
    Process the entire CSV file and display each individuals information.
    :param fileName (str): The file name
    :exception: FileNotFoundError if fileName does not exist:
    <TAB>IP (hex): <hex ip addr>
    :return: None
    """

    # using 'with' means the file handle, f, will be automatically closed
    # when the region finishes
    with open(fileName) as f:
        # discard first line (column labels)
        f.readline()

        # process the remainder of the lines
        for line in f:
            # strip the newline at the end of the line
            line = line.strip()

            # split the line into a list of strings, using the comma delimiter
            data = line.split(',')

            # print the ID
            print('ID:', data[ID])

            # print first initial and last name
            printName(data[FIRST_NAME], data[LAST_NAME])

            # print the username and domain for the email address
            printEmail(data[EMAIL])

            # print the country code
            printCountryCode(data[COUNTRY])

            # print IP
            printIP(data[IP])


def main():
    """
    The main function.
    :return: None
    """

    try:
        fileName = input("Enter filename: ")
        processFile(fileName)
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

if __name__ == '__main__':
    main()