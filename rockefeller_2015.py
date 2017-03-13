from bs4 import BeautifulSoup as bs
import requests
import csv
import re

grantee = []
location = []
amount = []
purpose = []

url = "https://www.rockefellerfoundation.org/2015-grantees/"

def get_grantees(url_in):
    r = requests.get(url_in)
    soup = bs(r.text, "html.parser")

    for hr in soup.find_all("hr"):
        grantee_p = hr.next_sibling.next_sibling
        if grantee_p.get_text() == '\xa0':
            grantee_p = grantee_p.next_sibling.next_sibling
        location_p = grantee_p.next_sibling.next_sibling
        amount_p = location_p.next_sibling.next_sibling
        purpose_p = amount_p.next_sibling.next_sibling

        grantee.append(grantee_p.get_text().replace("Grantee:","").replace("Organization:","").strip().replace("\u2013","-").replace("\u2019","\'"))
        location.append(location_p.get_text().replace("Location:","").replace("<br/>","").strip().replace("\u2013","-").replace("\u2019","\'"))
        amount.append(int(amount_p.get_text().replace("Amount:","").replace("$","").replace(",","").replace("<br/>","").strip().replace("\u2013","-").replace("\u2019","\'")))
        purpose.append(purpose_p.get_text().replace("Purpose:","").replace("<br/>","").strip().replace("\u2013","-").replace("\u2019","\'").replace("\u201d","\"").replace("\u201c","\""))

    return {"grantee": grantee,
    "location": location,
    "amount": amount,
    "purpose": purpose
    }

grantees = get_grantees(url)

data = []
data.append(grantee,location,amount,purpose)
print(data)
