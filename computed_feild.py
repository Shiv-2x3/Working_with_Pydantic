from pydantic import BaseModel , EmailStr , computed_field , AnyUrl
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

    @computed_field
    @property
    def cal_BMI(self) -> float:
        BMI = round(self.weight /(self.height**2),2)
        return BMI


paitent_info = {'name' : 'Shiv',
                'email' : 'Shiv@gmail.com',
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
          paitent.cal_BMI, 
          paitent.contact , sep='\n')
    print("!!data inserted sucessfully")


insert_paitent_data(paitent1)