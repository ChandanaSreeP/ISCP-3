'''
Instructions: 

1) This is the final capstone project of our end to end deployment series

2) By now you would have an code which stores the conversation a person had with a chatbot in database

3) We are now going to build an end to end deployment of a website

 

Question:

We are building an Admin Portal

1) Build a frontend using gradio, in which you can filter users by their ID, and date range: https://gradio.app/quickstart/

2) Once the admin enters the user_id and also the date range, it has to return all the conversation that the user had with chatbot on the date range

https://www.javatpoint.com/mysql-json

3) If the admin only enters the user_id, then all the conversations associated with that user should be returned

mysql commands: https://github.com/dkarthicks27/sample-repo/blob/main/mysql_commands.txt

4) If the admin enters only date range then during that date range whatever conversation are there it should return

5) Atleast one filter should be there, you can add more filters like location, contact, pro_user, etc, and modify similarly in database
'''

import openai
import mysql.connector
import datetime
import gradio as gr

openai.api_key = "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"

cnx = mysql.connector.connect(
    host="localhost", user="root", password="pcs123", database="mysql"
)
My_cursor = cnx.cursor()
My_cursor.execute(
    """CREATE TABLE IF NOT EXISTS chat_history (
                    USER VARCHAR(50) NOT NULL,
                    BOT VARCHAR(2500) NOT NULL,
                    Date DATE NOT NULL);"""
)

chat_history = []
def chat_bot(feed):
    if feed == "exit":
        res = "\n".join(chat_history)
        return res
    
    if feed == "show history":
        date_input = input("Enter the date (YYYY-MM-DD): ")
        query = "SELECT * FROM chat_history WHERE Date = %s"
        My_cursor.execute(query, (date_input,))
        rows = My_cursor.fetchall()
        if len(rows) == 0:
            return "No chat history found for the given date."
        else:
            response = "Chat history for " + date_input + ":\n"
            for row in rows:
                response += "User: " + row[0] + "\n"
                response += "Bot: " + row[1] + "\n"
                response += "Date: " + row[2].strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
            return response
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": feed}]
    )
    bot_response = response["choices"][0]["message"]["content"]
    result = feed + "\n" + bot_response
    date = datetime.datetime.now()
    insert_into_sql = "INSERT INTO chat_history (USER, BOT, Date) VALUES (%s, %s, %s)"
    data_push = (feed, bot_response, date)
    My_cursor.execute(insert_into_sql, data_push)
    cnx.commit()
    chat_history.append(result)
    return bot_response

iface = gr.Interface(fn=chat_bot, inputs="text", outputs="text", title="Chatbot")
iface.launch()


My_cursor.close()
cnx.close()
