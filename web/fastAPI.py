from fastapi import FastAPI

import db


cursor = db.conn.cursor()

app = FastAPI()


@app.get("/")
async def all_products():
    query = "SELECT * FROM produtos c order by c.name ASC"
    cursor.execute(query)
    try:
        obj_products = []
        for row in cursor.fetchall():
            obj_products.append({
                "id": row[0],     
                "nome": row[1],  
                "preco": row[2]  
            })
        return {"products": obj_products}
    except Exception:
        return {"error": "Error processing"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    query = f"SELECT * FROM produtos WHERE id={item_id}"
    cursor.execute(query)
    try:
        obj_products = []
        for row in cursor.fetchall():
            obj_products.append({
                "id": row[0],     
                "nome": row[1],  
                "preco": row[2]  
            })
        return {"products": obj_products}
    except Exception:
        return {"error": "Internal server error"}


