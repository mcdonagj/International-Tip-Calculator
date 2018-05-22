from InternationalTipCalculator import *
from DictionaryBuilder import *
from UserInterface import *
from flask import Flask


def main():

    # Create a DictionaryBuilder object, which:
    #   Creates a dictionary and stores key-value pairs of all available currencies and rates for a designated base.

    dictionary_builder: DictionaryBuilder = DictionaryBuilder()

    # Retrieve the rates for a given base currency.
    exec_rates = dictionary_builder.request_rates()

    # If the retrieval of rates does not succeed, send an email with details of the event.
    if not exec_rates:
        dictionary_builder.send_error_message()
        sys.exit()

    # Populate the dictionary with available currencies.
    rates = dictionary_builder.get_rates(exec_rates)

    # TODO: Integrate user input from GUI to allow for entry of a given rate.
    itc: InternationalTipCalculator = InternationalTipCalculator("EUR", dictionary_builder)

    # TODO: Implement a graphical user interface for the International Tip Calculator.
    #ui: UserInterface = UserInterface("International Tip Calculator", itc)

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Welcome to the International Tip Calculator."

    @app.route('/fixer_status')
    def fixer_status():
        result = "Fixer.io is not available."
        if exec_rates:
            result = "Fixer.io is available for use."

        return result

    app.run(debug=True)

    #print(len(dictionary_builder.currencies))

    #print(dictionary_builder.check_available_bases('ZWL'))

    #print(rates)


if __name__ == '__main__':
    main()


