# Activate virtual env
virtualenv -p C:/Users/ivan_/AppData/Local/Programs/Python/Python36/python.exe streamlit-env
streamlit-env/Scripts/activate

# Run hello_world.py
streamlit run hello_world.py --server.enableCORS false --server.enableXsrfProtection false