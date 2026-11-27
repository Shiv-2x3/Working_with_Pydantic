from pydantic import BaseModel

class Address(BaseModel):
    city :str
    state : str
    pincode :int

class paitent(BaseModel):
    name : str
    age : int 
    gender :str
    address : Address


adress_dict ={'city' : "malegoan" , "state" : "Malegoan" , "pincode" :223455}
address1 = Address(**adress_dict)
paitent_dict = {"name" : "shiv" , "age" : 45 , "gender"  : "male" , "address" : address1}
paitent1 = paitent(**paitent_dict)

temp = paitent1.model_dump()
print(temp)