# import pandas as pd 
# from langchain.agents import create_csv_agent
# from langchain.agents import create_pandas_dataframe_agent
# from FreeLLM import BardChatAPI
# from Bard import Chatbot

# cookie_path = "Wghlci3JMlUaLO4_VZgMKjCDDhUSMRvL4049frEMZZaj3PK1cJ6iMDTJbZoeClmdcGaRYg."
# llm=BardChatAPI.BardChat(cookie=cookie_path)

# df = pd.read_csv("cc_statement_short.csv")
# df = df.fillna(0)
# # agent = create_csv_agent(llm = llm, path = "train.csv", verbose=True)
# agent = create_pandas_dataframe_agent(llm=llm, df=df, verbose=False, cookie = cookie_path)
# query = """
# analyze the dataframe provided, and save the results into an Excel file named "multi_sheet.xlsx". use the "openpyxl" library when saving the Excel file. 
# Note you do not need to save the Excel file for intermediate steps.
# Inside the excel file, create a sheet "spending_by_category" that contains a summary of total spendings by each category.
# then use the summary data to create a bar chart inside Excel and put it on the same sheet "spending_by_category".
# """

# agent.run(query)
# import streamlit as st
# import pandas as pd

# # Título de la interfaz
# st.title("Generador de código")

# # Control para ingresar código Python
# codigo = st.text_area("Ingresa tu código Python aquí")

# # Botón de ejecución
# if st.button("Ejecutar"):
#     # Ejecutar el código ingresado
#     exec(codigo)
#     # Mostrar el resultado del código utilizando st.write()
#     st.write(result)
import streamlit as st
import pandas as pd

# Título de la interfaz
st.title("Generador de código")

# Control para ingresar código Python
codigo = st.text_area("Ingresa tu código Python aquí" , height = 400)

# Botón de ejecución
if st.button("Ejecutar"):
    # Crear un stream de texto para capturar la salida
    output = st.empty()
    # Redirigir la salida estándar al stream de texto
    with output:
        # Ejecutar el código ingresado
        exec(codigo)


