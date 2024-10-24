# helper script to rewrite sql queries with placeholders defined with f-strings to those using % formatting and tuples
# to avoid sql injection vulnerability

import re

while True:

    # input non parametrized sql query:
    sql_query = input("paste non-parametrized sql query that uses f-strings: ")

    # dropping out f-string heading
    sql_query = sql_query.replace("(f\"" , "(\"")

    # droping tail of snippet:
    sql_query = sql_query.replace("\")" , "\"")

    # replace single quotes + curvy brackets into just curvy crackets
    sql_query = sql_query.replace("'{" , "{")
    sql_query = sql_query.replace("}'" , "}")


    # regular expression pattern to find {} placeholders
    pattern = r"\{([^}]+)\}"
    params = re.findall(pattern, sql_query)

    # looping trough list and replace params for '%s'
    for param in params:
        param_quoted = str("{"+param+"}")
        sql_query = sql_query.replace(param_quoted, "%s")

    # prepare tuple (as a string) to pase join with sql query
    if len(params) == 1:
        params_tuple_str = "(" + ", ".join(params) + ",)"
    else:
        params_tuple_str = "(" + ", ".join(params) + ")"

    # full query resistant for sql injection
    parametrized_query = str(sql_query + ", " + params_tuple_str + ")")
    print("\n", parametrized_query)

    decision = input("Do you want to continue? (y/n): ")
    if decision.strip().lower() == 'y':
        continue
    else:
        break








