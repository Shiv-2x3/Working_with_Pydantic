from pydantic import BaseModel , EmailStr , computed_field , AnyUrl , field_validator
from typing import List , Dict

class paitent(BaseModel):

    name :str
    age : int
    email : EmailStr
    marrige : bool
    ig_url : AnyUrl
    height : float
    sugar : bool
    weight : float
    allergies :List[str]
    contact : Dict[str , str]

    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
        valid_domains = ['hdfc.bank' , 'icic.bank']
        domain_name = value.rsplit("@" , 1)[-1].lower()
        if domain_name not in valid_domains:
            raise ValueError("Email not in domain")
        else:
            return value

    @field_validator('name')
    @classmethod
    def upeer_name(cls , value):
        return value.upper()

    @field_validator("age")
    @classmethod
    def valid_age(cls , value):
        if 0 < value < 120:
            return value
        else:
            raise ValueError("Invlaid Integer")


paitent_info = {'name' : 'Shiv',
                'email' : 'Shiv@hdfc.bank',
                'marrige' : False,
                'ig_url' : "https://instagram?24344",
                'age' : 19,
                'weight' : 65.89,
                'height' : 23,
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