import sqlite3

connection = sqlite3.connect("Car store")
cursor_ = connection.cursor()
cursor_.execute("CREATE TABLE IF NOT EXISTS car_model("
                "id INTEGER PRIMARY KEY  AUTOINCREMENT,"
                "brand TEXT NOT NULL,"
                "model Text,"
                "price INTEGER"
                ")")
# ---------------- INSERT, SELECT, DELETE, UPDATE -------------------
# cursor_.execute("""INSERT INTO car_model(brand, model ) VALUES ("Tesla", "Y")""")
# connection.commit()

query_1 = "SELECT * FROM car_model"
query_2 = "SELECT * FROM car_model WHERE price>75000"
query_3 = "SELECT * FROM car_model WHERE brand='BMW'"
query_4 = "SELECT * FROM car_model WHERE brand='Mercedes' AND price<90000"
query_5 = "DELETE FROM car_model WHERE brand='Opel' and price<1000"
query_6 = "UPDATE car_model SET price=55000 WHERE id=24"
query_7 = "SELECT * FROM car_model ORDER BY price"
query_8 = "SELECT * FROM car_model ORDER BY price DESC"
query_9 = "SELECT * FROM car_model ORDER BY brand"
query_10 = "SELECT * FROM car_model WHERE brand=? AND price<?"

# ------------------ aggregation functions -------------------
query_agg_1 = "SELECT MAX(price) FROM car_model"
query_agg_2 = "SELECT MIN(price) FROM car_model"
query_agg_3 = "SELECT AVG(price) FROM car_model"
query_agg_4 = "SELECT COUNT(brand) FROM car_model"
query_agg_5 = "SELECT SUM(price) FROM car_model"

# result = cursor_.execute(query_10)
search_model = 'Opel'
search_price = 95000
result = cursor_.execute(query_10, (search_model, search_price))
# connection.commit()

for item in result.fetchall():
    print(item)
connection.close()
