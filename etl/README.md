# ETL

This is the data ETL code that pulls the data from Robinhood into Redis for consumption
in the API. The reason for this is that it abstracts security, as well as offers a buffer
zone for the data so that the Streamlit UI can more quickly access the information.

This application is a script that runs on a cadence to populate the in memory database.
