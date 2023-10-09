import re

SQL_command = "CREATE TABLE USER (ID INT NOT NULL AUTO_INCREMENT, USERNAME VARCHAR(80) NOT NULL, PIN VARCHAR(4) NOT NULL, NAME VARCHAR(90) NOT NULL, VARIABLE_SYMBOL INT NOT NULL, PRIMARY KEY (ID), UNIQUE INDEX USERNAME_UNIQUE (USERNAME ASC) VISIBLE, UNIQUE INDEX VARIABLE_SYMBOL_UNIQUE (VARIABLE_SYMBOL ASC) VISIBLE);"

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


def check_order(order):
    regex_rule = r'^(([a-zA-Z]+\ ?)*\,?\ ?)+$'
    if re.match(regex_rule, order):
        return True
    else:
        return False


def build_sql_select_user_by_username_and_variable_symbol(username, vs):
    if check_id(vs) and check_name(username):
        return "SELECT * FROM USERS WHERE USERNAME = '" + username + "' AND VARIABLE_SYMBOL = " + str(vs)
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_select_user_by_id(id_t):
    if check_id(id_t):
        return "SELECT * FROM USERS WHERE id = " + str(id_t)
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_select_users_order_by_custom(order_by_section):
    if check_order(order_by_section):
        return "SELECT * FROM USER ORDER BY " + order_by_section
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


# Pro otestování základní funkcionality můžete použít níže uvedené printy

try:
    print(SQL_command)
    print(build_sql_select_user_by_username_and_variable_symbol("novak", 1234))
    print(build_sql_select_user_by_id(12))
    print(build_sql_select_users_order_by_custom("USERNAME DESC, ID"))
except Exception as e:
    print(e)
