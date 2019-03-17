import requests

class PhoneVerifier:

    def __init__(self):
        """Constructor for PhoneVerifier objects.

        Usage::
        >>> import PhoneVerifier
        >>> pv = PhoneVerifier()
        """
        self.format = "1"
        self.country_code = ""
        self.url = "http://apilayer.net/api/validate"
        self.access_key = "3951622ea8890f098b9cb245ced7e742"

    def verifyPhone(self, number):
        """Validates phone numbers from a given integer value.

        :param number: number to validate.
        
        :return: :dict: `Dict` object containing validation information.
        :rtype: object

        Usage::

        >>> import PhoneVerifier
        >>> myPhoneVerifier = PhoneVerifier()
        >>> valid_number = myPhoneVerifier.verifyPhone(number)
        `Dict` object.
        """

        request = "{}?access_key={}&number={}&country_code={}&format={}".format(self.url, self.access_key, number, self.country_code, self.format)
        r = requests.get(request)
        if (r.ok):
            print(r.json())