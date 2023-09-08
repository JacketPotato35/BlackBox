import random
import sqlite3

connection_obj=sqlite3.connect("QUESTION.db")
cursor_obj=connection_obj.cursor()


function_name="modulus"
for i in range(1,25):
    a=random.randint(1,20)
    b=random.randint(1,5)
    pre_written_code=[f"A={a}"]
    end_written_code=[f"return A"]
    comment=f"use the modulus operator to find A modulus by {b} when A={a}"
    answer=a%b
    conditions=[b,"%"]
    print(comment,answer)
    sql_code=f"""
    INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer)
    VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}");
    """
    cursor_obj.execute(sql_code)
    connection_obj.commit()
function_name="exponential"
for i in range(1,25):
    a=random.randint(1,10)
    b=random.randint(1,3)
    pre_written_code=[f"A={a}"]
    end_written_code=[f"return A"]
    comment=f"use the exponential operator to find A to the power of {b} when A={a}"
    answer=a**b
    conditions=[b,"**"]
    print(comment,answer)
    sql_code=f"""
    INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer)
    VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}");
    """
    cursor_obj.execute(sql_code)
    connection_obj.commit()
function_name="floor division"
for i in range(1,25):
    a=random.randint(1,50)
    b=random.randint(1,10)
    pre_written_code=[f"A={a}"]
    end_written_code=[f"return A"]
    comment=f"use the floor division operator to find A floor divided by {b} when A={a}"
    answer=a//b
    conditions=[b,"//"]
    print(comment,answer)
    sql_code=f"""
    INSERT INTO question ( function_name, comments, pre_written_code, end_written_code, conditions, answer)
    VALUES ("{function_name}", "{comment}", "{pre_written_code}", "{end_written_code}", "{conditions}", "{answer}");
    """
    cursor_obj.execute(sql_code)
    connection_obj.commit()