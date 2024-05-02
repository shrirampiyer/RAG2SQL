from vanna.vannadb import VannaDB_VectorStore
from vanna.google import GoogleGeminiChat
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

"""class MyVanna(VannaDB_VectorStore, GoogleGeminiChat):
    def __init__(self, config=None):
        MY_VANNA_MODEL = # Your model name from https://vanna.ai/account/profile
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key=MY_VANNA_API_KEY, config=config)
        GoogleGeminiChat.__init__(self, config={'api_key': AIzaSyDGXS9dQQ9CW0S7SKus5aWzRKCfHCDxdJg, 'model': GEMINI_MODEL})"""

vn = VannaDefault(model='chinook', api_key='ffa7619819984d25acdfa499a427de23')
vn.connect_to_postgres(host='localhost', dbname='postgres', user='postgres', password='password', port='5432')

#df_information_schema = vn.run_sql("select * from healthcare_claims")

#plan = vn.get_training_plan_generic(df_information_schema)
#plan

vn.train(ddl="""CREATE TABLE healthcare_claims (
    id SERIAL PRIMARY KEY,
    patient VARCHAR(100),
    diagnosis_description VARCHAR(255),
    procedure_code VARCHAR(10),
    provider VARCHAR(100),
    service_date DATE,
    claim_submission_date DATE,
    bill_amount DECIMAL(10, 2),
    claim_status VARCHAR(50)
)""")

vn.train(documentation="No indexes are currently defined on the database. Consider creating indexes on columns frequently used in queries for improved query performance.")

vn.train(sql="SELECT * FROM healthcare_claims WHERE bill_amount > 500.00")
training_data = vn.get_training_data()
training_data

VannaFlaskApp(vn).run()