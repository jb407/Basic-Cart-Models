from pydantic import BaseModel

class Customer(BaseModel):
    nextID: int = 1000
    __customerID: int = 1 # TODO this never updates
    customerName: str
    __customerBalance: float = 0.0
        
    # Getters and Setters
    @property
    def customerID(self) -> int:
        return self.__customerID
    
    @property
    def customerName(self) -> str:
        return self.customerName
    
    @customerName.setter
    def customerName(self, customerName):
        self.customerName = customerName
        
    @property
    def customerBalance(self) -> float:
        return self.__customerBalance
    
    def update_balance(self, amount):
        self.__customerBalance = round(self.__customerBalance + amount, 2) # handle precision errors for floating-point numbers
        
    def __str__(self):
        return f"Customer ID = {self.__customerID}, Name = {self.customerName}, Balance = ${self.__customerBalance}"
