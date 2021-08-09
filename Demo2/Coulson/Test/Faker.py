from faker import Faker
from icecream import ic

fake = Faker(locale='zh_CN')    #zh_CN/en_US
ic(fake.name())
ic(fake.address())

ic(fake.ssn())
ic(fake.company())
ic(fake.name())
ic(fake.phone_number())
ic(fake.password())
ic(fake.pystr())