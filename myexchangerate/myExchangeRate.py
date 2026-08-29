"""myExchangeRate.py."""

__title__: str = "myExchangeRate"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"


import dataclasses
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import myExchangeRateDefinitions

@dataclasses.dataclass(init=False)
class MyExchangeRate:
    """

    """

    _str_url_two_exchange_data: str = dataclasses.field(init=False, default_factory=str)

    _dict_exchange_data: dict = dataclasses.field(init=False, default_factory=dict)

    _int_response_time_out: int = dataclasses.field(init=False, default_factory=int)

    def __init__(self) -> None:
        super().__init__()

        self._str_url_two_exchange_data = myExchangeRateDefinitions.STR_URL_2_EXCHANGE_DATA

        self._int_response_time_out = myExchangeRateDefinitions.INT_RESPONSE_TIME_OUT

        self._dict_exchange_data = {}

        try:

            # 1. Timeout definieren (Verhindert unendliches Hängen der Anwendung)
            response = requests.get(self._str_url_two_exchange_data, timeout=self._int_response_time_out)

            # 2. HTTP-Fehlerstatuscodes (4xx, 5xx) in eine Exception umwandeln
            response.raise_for_status()

        # Spezifische Fehler zuerst abfangen
        except HTTPError as http_err:

            print(f"HTTP-Fehler aufgetreten: {http_err}")
            # Hier spezifisches Verhalten für z.B. 404 (Not Found) oder 500 (Server Error) einbauen

        except ConnectionError as conn_err:

            print(f"Netzwerk-/Verbindungsfehler: {conn_err}")
            # DNS-Fehler, verweigerte Verbindung oder Server offline

        except Timeout as time_err:

            print(f"Die Anfrage lief in ein Zeitlimit (Timeout): {time_err}")
            # Server hat nicht schnell genug geantwortet

        # Allgemeine Requests-Exception als Fangnetz für alle anderen Bibliotheks-Fehler
        except RequestException as req_err:

            print(f"Ein allgemeiner Requests-Fehler ist aufgetreten: {req_err}")

        # Absicherung gegen logische Programmierfehler (z.B. JSON-Parsing scheitert)
        except Exception as general_err:

            print(f"Ein unerwarteter Fehler ist aufgetreten: {general_err}")

        else:

            try:

                self._dict_exchange_data = response.json()

            except ValueError:

                print("Antwort enthielt kein gültiges JSON-Format.")

    def get_exchange_rate(self, str_quote_currency_identifier: str) -> float| None:

        if str_quote_currency_identifier:

            if str_quote_currency_identifier.islower():

                str_quote_currency_identifier = str_quote_currency_identifier.upper()

            result = next((item for item in self._dict_exchange_data if item.get("quote") == str_quote_currency_identifier), None)

            if result is not None:

                return result['rate']

            else:

                return None

        else:

            return None

if __name__ == "__main__":

    my_exchange_rate = MyExchangeRate()
    # print(my_exchange_rate.get_exchange_rate("USD"))
    print(my_exchange_rate.get_exchange_rate("usd"))










