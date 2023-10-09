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
    regex_rule = r'^[a-zA-Z0-9]+\.?[a-zA-Z0-9]*\@[a-zA-Z]+\.(com|cz){1}$'
    if re.match(regex_rule, email_t):
        return True
    else:
        return False


def build_sql_update_user_jmeno_by_id(name, id_t):
    if check_id(id_t) and check_name(name):
        return "UPDATE uzivatel SET jmeno = '" + name + "' WHERE id = " + str(id_t)
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_delete_by_table_and_id(table_name, id_t):
    if check_id(id_t) and check_name(table_name):
        return "DELETE FROM '" + table_name + "' WHERE id = " + str(id_t)
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_insert_users(users):
    sql = ""
    for user in users:
        if not check_name(user["jmeno"]) or not check_email(user["email"]):
            raise Exception("Hodnoty jsou zadany spatne!")
        else:
            sql += "INSERT INTO uzivatel (email, jmeno) VALUES ('" + user["email"] + "','" + user["jmeno"] + "')\n"
    return sql


# Pro otestování základní funkcionality můžete použít níže uvedené printy

try:
    print(SQL_command)
    print(build_sql_update_user_jmeno_by_id("jiri", 28))
    print(build_sql_delete_by_table_and_id("uzivatel", 39))
    print(build_sql_insert_users([{"jmeno": "Jiri", "email": "jiri.syrovatko3@seznam.cz"}, {"jmeno": "Jaromir", "email": "jaromirdub@gmail.com"}]))
except Exception as e:
    print(e)
