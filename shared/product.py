from pydantic import BaseModel

class Product(BaseModel):
    productName: str
    productPrice: float
        
    # Getters and Setters
    @property
    def productName(self) -> str:
        return self.productName
    
    @productName.setter
    def productName(self, productName):
        self.productName = productName
        
    @property
    def productPrice(self):
        return self.productPrice
    
    @productPrice.setter
    def productPrice(self, productPrice):
        self.productPrice = productPrice
        
    def __str__(self):
        return f"Product [Name = {self.productName}, Price = {self.productPrice}]"
