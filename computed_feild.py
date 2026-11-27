from pydantic import BaseModel , EmailStr , computed_feild
from typing import List , Dict

class paitent(BaseModel):

    name :str
    age : int
    email : EmailStr
    marrige : bool
    height : bool
    weight : float
    allergies = List[str]
    constct = Dict[str , str]

    @computed_feild
    @property
    def cal_BMI(self) -> float:
        BMI = round(self.weight /(self.height**2),2)
        return BMI


paitent_info = {'name' : 'Shiv',
                'email' : 'Shiv@gmail.com',
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