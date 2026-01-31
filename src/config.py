# NOTE: I still don't have any clue what the purpose of this file is. 
# I tried to make use of it as per the instructions given to me by ChatGPT 
# but I couldn't make sense of it. It has something to do with importing data 
# (json, etc) from the 'data/' directory. Perhaps because this conce[t is too 
# new to me and I have not been able to grasp it adequately, thus i failed to 
# truly understand its functionality within the larger program.


from pathlib import Path

PRJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PRJECT_ROOT / "data" 

print(DATA_DIR)


# ____ Original notes/reccommendation from ChatGPT for this method ____:

# 🏗 7. If You Want to Go Further (Best Practice Option)

# Many production Python apps adopt a settings.py or config.py:

# src/
# └── config.py


# Content:

# from pathlib import Path

# PRJECT_ROOT = Path(__file__).resolve().parents[1]
# DATA_DIR = PRJECT_ROOT / "data"


# Then everywhere else:

# from modules.config import DATA_DIR


# This is how Django, FastAPI, Airflow, and others do it.