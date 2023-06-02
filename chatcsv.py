import pandas as pd 
from langchain.agents import create_csv_agent
from langchain.agents import create_pandas_dataframe_agent
from FreeLLM import BardChatAPI
from Bard import Chatbot

cookie_path = "Wghlci3JMlUaLO4_VZgMKjCDDhUSMRvL4049frEMZZaj3PK1cJ6iMDTJbZoeClmdcGaRYg."
llm=BardChatAPI.BardChat(cookie=cookie_path)

df = pd.read_csv("900.csv")
df = df.fillna(0)
# agent = create_csv_agent(llm = llm, path = "train.csv", verbose=True)
agent = create_pandas_dataframe_agent(llm=llm, df=df, verbose=True, cookie = cookie_path)
consulta = "contar cuantos registros tienen nombre de mujer"
agent.run(consulta)