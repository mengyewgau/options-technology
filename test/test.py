from common.config import ENGINE

try:
    conn = ENGINE.connect()
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print(f"Failed to connect: {e}")
