from pydantic import BaseModel , EmailStr , field_validator
from typing import List , Dict

class paitent(BaseModel):

    name :str
    age : int
    email : EmailStr
    marrige : bool
    weight : float
    allergies = List[str]
    constct = Dict[str , str]

    @field_validator('email') # This is a feild vaildator decorator for email
    @classmethod
    def email_validator(cls , value):
        valid_domains = ['hdfc.bank' , 'icic.bank']
        domain_name = value.split("@")
        if domain_name not in valid_domains:
            raise ValueError("Invlaid Domain")
        else:
            return value

    @field_validator('name')
    @classmethod
    def transform_uppercase(cls, value):
        return value.upper()

    @field_validator("age" , mode = "before")
    @classmethod
    def validating_age(cls , value):
        if 0 <value < 120:
            return value
        else:
            raise ValueError("Invalid age : Enter between 0 - 120")


paitent_info = {'name' : 'Shiv',
                'email' : 'Shiv@gmail.com',
                'ig_url' : "https://instagram?24344",
                'age' : 19,
                'weight' : 65.89,
                'sugar' : False,
                'allergies' : ['dust' , 'light'],
                'contact' : {'email' : 'xyz@gmail.com' , 'number' : '1234567899'}}



paitent1 = paitent(**paitent_info) # **-> unpack our dictnory


# Defining paitent function
def insert_paitent_data(paitent:paitent):
    print(paitent.name ,
          paitent.email ,
          paitent.ig_url,  
          paitent.age , 
          paitent.sugar , 
          paitent.weight , 
          paitent.allergies , 
          paitent.contact , sep='\n')
    print("!!data inserted sucessfully")


insert_paitent_data(paitent1)