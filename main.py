from os import getenv
from dotenv import load_dotenv
load_dotenv()

MONGO_SOURCE = str(getenv("MONGO_SOURCE")) # cast it to tell pylance 
MONGO_TARGET = str(getenv("MONGO_TARGET"))
TEST_NUMBER = int(str(getenv("LIMIT")))

print("value imported from dotenv file " + "\"" + MONGO_SOURCE + "\"")
print("Another value imported from dotenv file " + "\"" + MONGO_TARGET + "\"")
print(TEST_NUMBER, "is int value import from dotenv")
