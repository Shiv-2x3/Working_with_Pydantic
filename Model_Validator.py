from pydantic import BaseModel , EmailStr , field_validator ,model_validator
from typing import List , Dict

class paitent(BaseModel):

    name :str
    age : int
    email : EmailStr
    marrige : bool
    weight : float
    contact = Dict[str , str]

    @classmethod
    @model_validator(mode= "after")
    def validate_emergency_conatct(cls , model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("person should have emergency contact")
        else:
            return model



paitent_info = {'name' : 'Shiv',
                'email' : 'Shiv@gmail.com',
                'ig_url' : "https://instagram?24344",
                'age' : 19,
                'weight' : 65.89,
                'sugar' : False,
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
          paitent.contact , sep='\n')
    print("!!data inserted sucessfully")


insert_paitent_data(paitent1)