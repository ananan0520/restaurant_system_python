# this python file is only used to generate testing data for financial graph with admin privilege

import sqlite3
from datetime import datetime, timedelta
import os
import random

relative_path = "db"
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, relative_path, "restaurantSystem.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

start_date = datetime.now()
end_date = start_date - timedelta(days=365 * 3)

reserve_id_counter = 1

while start_date > end_date:
    for _ in range(10):
        dish_id = random.randint(1, 100)  
        dish_amount = random.randint(1, 3)

        order_time = start_date.replace(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))

        cur.execute(
            """
            INSERT INTO reserve_kitchen (reserve_id, time, dish_id, dish_amount, serving_stat)
            VALUES (?, ?, ?, ?, ?)
            """, (str(reserve_id_counter), str(order_time), str(dish_id), str(dish_amount), "PAID")
        )

        reserve_id_counter += 1

    start_date -= timedelta(days=1)

conn.commit()
conn.close()