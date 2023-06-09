from pyfire import Credentials
from pyfire import Database
from pyfire import Session


def run():
    fire = Session(Credentials.user, Credentials.password)
    firebase = Database(fire)
    print(firebase.equal("alegra/products", "reference", "TP-19100"))
    # print(firebase.get("woocommerce/products"))
    invoices = firebase.between("alegra/invoices", "date",
                                "2023-05-01", "2023-05-1")
    print(invoices[1])


if __name__ == "__main__":

    run()
