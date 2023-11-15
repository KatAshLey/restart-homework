#creating APIs for items

from dto import ItemOrigin, InventoryItem
from fastapi import FastAPI, HTTPException

app = FastAPI()

#create dictionary
item01 = InventoryItem(name= "Chocolate",
                       quantity= 551,
                       serial_num= "5155465",
                       origin= ItemOrigin(country= "Ethiopia",
                                           production_date= "21/05/2038"))
item02 = InventoryItem(name= "Gummies",
                       quantity= 6513,
                       serial_num= "hb568454",
                       origin= ItemOrigin(country= "Ethiopia",
                                          production_date= "24/03/3152"))
item03 = InventoryItem(name= "Chewies",
                       quantity= 54351,
                       serial_num= "jjn536156154",
                       origin= ItemOrigin(country= "Ethiopia",
                                          production_date= "16/09/1343"))
my_inventory_items_dict = {
    item01.serial_num: item01,
    item02.serial_num: item02,
    item03.serial_num: item03
}
print(my_inventory_items_dict)


#create PUT APIs
@app.put("/items/{serial_num}")
def update_item(name: str, quantity: int, serial_num: str, origin: ItemOrigin):
    return {"name": name, "quantity": quantity, "serial_num": serial_num, "origin": origin}

#create GET APIs
@app.get("items/{serial_num}")
def read_item(name: str, quantity: int, serial_num: str, origin: ItemOrigin):
    if serial_num not in my_inventory_items_dict:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": name, "quantity": quantity, "serial_num": serial_num, "origin": origin}



