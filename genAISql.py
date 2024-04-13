from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain

api_key  = os.getenv('GOOGLE_API_KEY')
db_user="root"
db_password="12345"
db_host="localhost"
db_name="world"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info = 3)
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)
sql_chain = create_sql_query_chain(llm, db)


def getQueryResult(query):
    resp=sql_chain.invoke({"question":query})
    new_ans=db.run(resp)
    return new_ans


if __name__ == "__main__":
    print(getQueryResult("how many cities does India have?"))

