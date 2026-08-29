# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests

url = "https://api.frankfurter.dev/v2/rates"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

    response = requests.get(url)

    print(response.status_code)

    if response.status_code == 200:

        # data = response.headers

        # print(data)

        data = response.json()

        # print(data)

        result = next((item for item in data if item.get("quote") == "USD"), None)

        print(result)

        # usd_kurs = data["USD"]

        # print(f"Aktueller EUR/USD Kurs vom {data['date']}: {usd_kurs}")

    else:

        print("Fehler beim Abrufen der Daten.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
