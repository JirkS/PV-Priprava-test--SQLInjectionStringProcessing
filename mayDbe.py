import re

SQL_command = "CREATE TABLE uzivatel (id int unsigned NOT NULL AUTO_INCREMENT, email varchar(255) NOT NULL, jmeno varchar(55) NOT NULL, PRIMARY KEY (id), UNIQUE KEY email_UNIQUE (email));"

# Opravte níže uvedenou knihovnu funkcí tak, aby ji nebylo možné naopadnout SQL Injection


def check_id(id_t):
    if str(id_t).isdigit() and id_t > 0:
        return True
    else:
        return False


def check_name(name_t):
    regex_rule = r'^[a-zA-Z0-9]+$'
    if re.match(regex_rule, name_t):
        return True
    else:
        return False


def check_email(email_t):
    regex_rule = r'^[a-zA-Z0-9]+.?[a-zA-Z0-9]+\@[a-zA-Z]+\.(com|cz){1}$'
    if re.match(regex_rule, email_t):
        return True
    else:
        return False


def build_sql_update_email_by_id(email, id_t):
    if check_email(email) and check_id(id_t):
        return "UPDATE uzivatel SET email = '"+email+"' WHERE id = "+str(id_t)
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_delete_all_by_table(table_name):
    if check_name(table_name):
        return "DELETE FROM '"+table_name+"' WHERE 1=1"
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_update_users(users):
    sql = ""
    for user in users:
        if not check_email(user["email"]) or not check_name(user["jmeno"]) or not check_id(user["id"]):
            raise Exception("Hodnoty jsou zadany spatne!")
        else:
            sql += "UPDATE uzivatel SET email = '"+user["email"]+"', jmeno = '"+user["jmeno"]+"' WHERE id = "+str(user["id"]) + " "
    return sql


# Pro otestování základní funkcionality můžete použít níže uvedené printy

try:
    print(SQL_command)
    print(build_sql_update_email_by_id("ondraKulhav@seznam.cz", 17))
    print(build_sql_delete_all_by_table("uzivatel"))
    print(build_sql_update_users([{"id": 9, "jmeno": "Jiri", "email": "jiri.syrovatko3@seznam.cz"}, {"id": 28, "jmeno": "Andrej", "email": "andrejB@mail.com"}]))
except Exception as e:
    print(e)
