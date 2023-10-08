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


def build_sql_select_all_from_table(table_name):
    if check_name(table_name):
        return "SELECT * FROM " + table_name
    else:
        raise Exception("Hodnoty jsou zadany spatne!")


def build_sql_select_custom_from_users(columns):
    sql = "SELECT "
    isFirst = True
    for column in columns:
        if isFirst:
            isFirst = False
            if not check_name(column):
                raise Exception("Hodnoty jsou zadany spatne!")
            else:
                sql += column
        else:
            if not check_name(column):
                raise Exception("Hodnoty jsou zadany spatne!")
            else:
                sql += ", "+column
    sql += " FROM USER"
    return sql


def build_sql_select_users_order_by_custom(order_by_section):
    return "SELECT * FROM USER ORDER BY "+order_by_section


# Pro otestování základní funkcionality můžete použít níže uvedené printy

try:
    print(SQL_command)
    print(build_sql_select_all_from_table("USER"))
    print(build_sql_select_custom_from_users(["NAME", "USERNAME"]))
    print(build_sql_select_users_order_by_custom("USERNAME DESC, ID"))
except Exception as e:
    print(e)
