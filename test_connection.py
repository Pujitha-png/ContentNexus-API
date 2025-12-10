from database import engine

try:
    connection = engine.connect()
    print("Connected to MySQL successfully!")
except Exception as e:
    print("Error:", e)
