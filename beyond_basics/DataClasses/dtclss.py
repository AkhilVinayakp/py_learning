# Data Classes in python
# Data class for 

from dataclasses import dataclass







# With namedTuple 
#%%
from collections import namedtuple
Student:namedtuple = namedtuple("Student",['class_', 'age'])
st1 = Student(class_ = "XI", age=17)
# %%
# with dataclass
from dataclasses import dataclass
@dataclass
class CollegeStd:
    class_: str
    age:int
std2: CollegeStd = CollegeStd(class_="CS", age=21)
# %%
from dataclasses import dataclass, make_dataclass
Proff:dataclass = make_dataclass("Proffesor", ['name', 'age', 'subject'])
p1:Proff = Proff(name="RajKuma", age=34, subject="eng")
print(p1)

# %%
# providing default values to a dataclass
from typing import Any
from dataclasses import dataclass

@dataclass
class TestData:
    delta: Any = 12

t: TestData = TestData()
print(t)

# %%
