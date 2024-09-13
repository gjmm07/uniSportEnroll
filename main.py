from selenium import webdriver
import time
import datetime
import argparse


def is_page_ready() -> bool:
    DRIVER.refresh()
    return DRIVER.title != "HSP: Anmeldung geschlossen"


def enroll(firstname: str,
           lastname: str,
           mat: str,
           email: str,
           phone: str,
           uni: str, ):
    DRIVER.find_element("id", "vorname").send_keys(firstname)
    DRIVER.find_element("id", "nachname").send_keys(lastname)
    DRIVER.find_element("id", "matrikel").send_keys(mat)
    DRIVER.find_element("id", "email").send_keys(email)
    DRIVER.find_element("id", "telefon").send_keys(phone)  # sometimes telefonnummer
    DRIVER.find_element("id", "hochschulen").send_keys(uni)
    DRIVER.find_element("id", "anmelden").click()


def wait_for_time(date: datetime.date):
    while True:
        now = datetime.datetime.now()
        yield (date - now) > datetime.timedelta(0)


def wait_for_page(site: str, date: datetime.date):
    # "https://anmeldung.hochschulsport-koeln.de/anmeldung.php?course=64&offer=44"
    DRIVER.get(site)
    gen = wait_for_time(date)
    while next(gen):
        time.sleep(0.1)
    while True:
        if is_page_ready():
            break
        time.sleep(1)


if __name__ == "__main__":
    uni_lookup: dict[int, str] = {1: "01 Universität Köln",
                                  2: "02 Technische Hochschule Köln"}
    parser = argparse.ArgumentParser()
    parser.add_argument("--firstname", "-f", type=str, required=True)
    parser.add_argument("--lastname", "-l", type=str, required=True)
    parser.add_argument("--matrikel", "-m", type=int, required=True)
    parser.add_argument("-email", "-e", type=str, required=True)
    parser.add_argument("--phone", "-p", type=str, required=True)
    parser.add_argument("--uni", "-u", type=lambda idx: uni_lookup.get(int(idx)), required=True)
    parser.add_argument("--site", "-s", type=str, required=True)
    parser.add_argument(
        "--date", "-d", type=lambda s: datetime.datetime.strptime(s, "%d.%m.%Y_%H:%M:%S"),
        required=True)
    args = parser.parse_args()
    DRIVER = webdriver.Chrome()
    wait_for_page(args.site, args.date)
    enroll(args.firstname, args.lastname, args.matrikel, args.email, args.phone, args.uni)
    time.sleep(5000)

