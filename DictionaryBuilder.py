import smtplib
import sys
from time import strftime, gmtime

import requests


class DictionaryBuilder:
    currencies = dict()

    def get_dictionary(self) -> object:
        """
        get_dictionary - Returns the currencies instance variable.
        :return: Dictionary object containing all retrieved currencies.
        """

        return self.currencies

    def request_rates(self) -> bool:
        """
        request_rates - Builds the current rates variable with current rate values.
                        Prints an error message to the terminal if the status code is not HTTP[200] (OK).
        :return: Boolean value if the rates can be retrieved from the given service.
        """

        current_rates = requests.get(
            'http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1')
        ok_response = current_rates.status_code == 200

        if not ok_response:
            print("ERROR code" + str(current_rates.status_code) + ": invalid response from fixer.io:")

        return ok_response

    def get_rates(self, service_up: bool) -> str:
        """
        get_rates(bool) - Retrieves and calls JSON organization subroutine for available rates.
        :param service_up: Boolean variable dictating availability of rates service, Fixer.io.
        :return: JSON text of a given rates query.
        """

        # Check to see if the service is available.
        if not service_up:
            print("ERROR: rate service 'fixer.io' is not available. Try again later.")
            sys.exit()

        requests_text = requests.get(
            "http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1").text

        self.split_json(requests_text)

        return requests.get('http://data.fixer.io/api/latest?access_key=a6cf5db13abce0db6576c936b74eeef3&format=1').text

    def send_error_message(self):
        """
        send_error_message - Helper function that assists with handling error messages within the ITC.
        Creates an MIME message and sends it to a given email address. Execution of the ITC halts if
        this state is encountered.
        """
        # TODO: Implement functionality that sends an email notification to mcdonagj@dukes.jmu.edu
        # when the request for rate information fails.
        # Used for testing email messaging.

        from email.mime.multipart import MIMEMultipart
        message = MIMEMultipart()

        message['From'] = 'sendpyerr@gmail.com'
        message['To'] = 'mcdonagj@dukes.jmu.edu'
        message['Subject'] = '[ERROR] International Tip Calculator - ' + strftime("%Y-%m-%d %H:%M:%S", gmtime())

        message_text = "There was a problem with retrieving rates in the International Tip Calculator:\n\tDate: {0}\n".format(
            strftime(
                "%Y-%m-%d %H:%M:%S", gmtime()))

        message_body = 'Subject: {}\n\n{}'.format(message['Subject'], message_text)

        gmail_user = 'sendpyerr@gmail.com'
        gmail_pwd = 'pythonerr'

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(gmail_user, gmail_pwd)

        smtpserver.sendmail(message['From'], message['To'], message_body)

    # TODO: create a function that retrieves each currency and assigns them to a dictionary position.
    def split_json(self, requests_text: str) -> bool:
        """
        split_json(str) - Helper method that divides JSON text into usable text for the Dictionary of currencies.
        :param requests_text: JSON text retrieved from Fixer.io.
        :return: Boolean condition indicating the success of dividing this text.
        """
        start_currencies = False

        for word in requests_text.split():
            if start_currencies:
                self.add_currency(word)
            else:
                if word.__contains__("rates"):
                    start_currencies = True
        return start_currencies

    def check_available_bases(self, given_base: str):
        """
        check_available_bases(str) - Helper method that checks to see if a given base (key) is within the dictionary.
        :param given_base:
        :return: the given key if it is within the currencies dictionary.
        """
        return given_base in self.currencies

    def check_available_currencies(self, given_currencies):
        """
        check_available_currencies(dict) - Helper method that compares the contents of two dictionaries.
        :param given_currencies:
        :return: False if the parameter is larger or smaller; True otherwise.
        """
        valid_currency_set = False
        return valid_currency_set

    def add_currency(self, currency_to_add: str):
        revised_addition = currency_to_add.replace(",", "").replace("}", "")

        if len(revised_addition) > 0:
            key_pairs = revised_addition.split(":")
            # print("-- Currency Addition:\n")

            # NOTE: Quotations removed from key values.
            key = key_pairs[0].replace('"', "")
            # print("  Key: " + key + "\n")

            value = key_pairs[1]
            # print("  Value: " + value + "\n")

            self.currencies[key] = value

        else:
            revised_addition = "ERROR"

        return revised_addition
