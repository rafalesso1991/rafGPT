from fastapi import FastAPI, status
import json
import uvicorn
from typing import Union

app = FastAPI(
        title="rafGPT",
        description="Portfolio: Rafael Alesso",
        version="1.0.0",
        debug=True
        )

items_table = [{ "id":1, "name":"item" }]

@app.get("/", status_code = status.HTTP_200_OK)
def read_all():
    return json.loads(json.dumps(items_table))

@app.get("/{id}", status_code = status.HTTP_200_OK)
def read_root(id: int):
    for item in items_table:
        if item["id"] == id:
            return item
    
    return {}

@app.post("/create_item", status_code = status.HTTP_201_CREATED)
def read_root(name: str):
    new_id = items_table[-1]["id"]
    items_table.append({ "id": new_id + 1, "name": name })
    return {"id": new_id + 1, "name": name}

@app.delete("/delete_{id}", status_code = status.HTTP_200_OK)
def delete_item(id: int):
    for item in items_table:
        if item["id"] == id:
            deleted_item = item
            items_table.remove(item)
            return deleted_item
    
    return {}

@app.patch("/patch_{id}", status_code = status.HTTP_200_OK)
def patch_item(id: int, name: str):
    for item in items_table:
        if item["id"] == id:
            item["name"] = name
            return item
    
    return {}

@app.get("/items/{item_id}", status_code = status.HTTP_200_OK)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__=="__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)