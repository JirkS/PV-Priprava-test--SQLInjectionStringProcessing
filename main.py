import re


def check_name(name_t):
    regex_rule = r'^[a-zA-Z0-9\.\s]+$'
    if re.match(regex_rule, name_t):
        return True
    else:
        return False


def check_phone(phone_t):
    regex_rule = r'^\+[0-9]{3}\s[0-9]{9}$'
    if re.match(regex_rule, phone_t):
        return True
    else:
        return False


def check_path(path_t):
    regex_rule = r'^(\/[a-zA-Z]+)*\.[a-zA-Z]{1,5}$'
    if re.match(regex_rule, path_t):
        return True
    else:
        return False


def check_size_number(num_t):
    regex_rule = r'^(0|[1-9]{1}[0-9]+)$'
    if re.match(regex_rule, str(num_t)):
        return True
    else:
        return False


def check_text(description_t):
    regex_rule = r'^([a-zA-Z0-9]+\s*)+\.?$'
    if re.match(regex_rule, description_t):
        return True
    else:
        return False


def check_account_number(a_c_t):
    regex_rule = r'^[0-9]{10}\/[0-9]{4}$'
    if re.match(regex_rule, a_c_t):
        return True
    else:
        return False


def build_html_contact_item(name, phone):
    if not check_name(name) or not check_phone(phone):
        raise Exception("Hodnoty jsou zadany spatne!")
    else:
        return "<div class=\"contact_item\"><h2>"+name+"</h2><p>Phone: "+phone+"</p></div>"


def build_html_img(path, width, height, description=""):
    if not check_path(path) or not check_size_number(width) or not check_size_number(height) or not check_text(description):
        raise Exception("Hodnoty jsou zadany spatne!")
    else:
        return "<img src=\""+path+"\" alt=\""+description+"\" width=\""+str(width)+"\" height=\""+str(height)+"\">"


def build_xml_from_money_transactions(money_transactions):
    xml = "<money_transactions>\n"
    for transaction in money_transactions:
        if not check_account_number(transaction["account_number"]) or not check_size_number(transaction["amount"]) or not check_text(transaction["message"]):
            raise Exception("Hodnoty jsou zadany spatne!")
        else:
            xml += " <transaction>\n"
            xml += "  <account_number>" + transaction["account_number"] + "</account_number>\n"
            xml += "  <amount>" + str(transaction["amount"]) + "</amount>\n"
            xml += "  <message>" + transaction["message"] + "</message>\n"
            xml += " </transaction>\n"
    xml += "</money_transactions>\n"
    return xml[0:len(xml)-2]


try:
    # priklad spravne zadanych hodnot
    print(build_html_contact_item("Ing. Jan Novak", "+420 606321423"))
    print(build_html_img("/img/obrazek.jpg", 80, 40, "Logo firmy"))
    print(build_xml_from_money_transactions([
        {"account_number": "0500021502/0800", "amount": 1300, "message": "Platba za obedy Jan Novak"},
        {"account_number": "1500023322/0600", "amount": 1450, "message": "Obedy Petr Novak"}
    ]))

    # priklad nespravne zadanych hodnot (vyhodi se exception a program nepokracuje dal)
    '''
    print(build_html_contact_item("Ing. Jan Novák","+420 606321423</p></div><script>alert('Hacked!');</script><p><div>"))
    print(build_html_img("/img/obrazek.jpg",80,-40,"\"/><img src=\"\" width=\"100\" height=\"200\" alt=\"Hacked logo"))
    print(build_xml_from_money_transactions([
        {"account_number": "0500021502/0800",  "amount": 1300, "message": "Platba za obědy Jan Novák"},
        {"account_number": "1500023322/0600",  "amount": 1450, "message": "Obědy Petr Novák</message>\n </transaction>\n <transaction>\n  <account_number>0700098720/0100</account_number>\n  <amount>1000000</amount>\n  <message>Hack"}
    ]))
    '''
except Exception as e:
    print(e)
