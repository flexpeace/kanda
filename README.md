# This is a quick excercise for Kanda. 

# SETUP
1. install virtualenv by running `pip install virtualenv`
2. create new environment virtualenv kandaEnv 
3. cd into kandaEnv and `source bin/activate`
4. cd into root folder `kanda`
5. run `pip install -r requirements.txt` and `pip install -r tests-requirements.txt`
6. Run tests or server using commands below

# RUNNING TESTS
`pytest tests`

# RUNNING SERVER
`gunicorn --reload main:app`
