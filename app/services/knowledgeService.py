import pyodbc
import os
from typing import List, Dict
from dotenv import load_dotenv

from app.db.connection import get_connection

load_dotenv()

# def get_chat_knowledge() -> List[Dict]:
#     conn_str = (
#         f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
#         f"SERVER={os.getenv('DB_SERVER')};"
#         f"DATABASE={os.getenv('DB_NAME')};"
#         f"UID={os.getenv('DB_USER')};"
#         f"PWD={os.getenv('DB_PASSWORD')}"
#     )
#
#     conn = pyodbc.connect(conn_str)
#     cursor = conn.cursor()
#
#     cursor.execute("""
#                    SELECT entity_type, entity_code, text
#                    FROM CHAT_KNOWLEDGE
#                    """)
#
#     columns = [column[0] for column in cursor.description]
#     rows = []
#
#     for row in cursor.fetchall():
#         rows.append(dict(zip(columns, row)))
#
#     cursor.close()
#     conn.close()
#
#     return rows

def fetch_knowledge():
    """
    Returns unified knowledge rows for chatbot
    """

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT entity_type, entity_code, text
                   FROM VW_CHAT_KNOWLEDGE
                   """)

    knowledge = [
        {
            "entity_type": r.entity_type,
            "entity_code": r.entity_code,
            "text": r.text
        }
        for r in cursor.fetchall()
    ]


    cursor.close()
    conn.close()

    return knowledge
