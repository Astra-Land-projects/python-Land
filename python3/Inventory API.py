from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Inventory API"
)


class Product(BaseModel):
    name: str
    quantity: int
    price: float


products = []


@app.post("/products")
def add_product(product: Product):

    item = {
        "id": len(products) + 1,
        "name": product.name,
        "quantity": product.quantity,
        "price": product.price
    }

    products.append(item)

    return item


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {
        "error": "Product not found"
    }


@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            return {
                "message": "Product deleted"
            }

    return {
        "error": "Product not found"
    }