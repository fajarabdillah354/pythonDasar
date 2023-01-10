from ast import Try
from xml.dom import ValidationErr


try:
    x = open('tryExxcep.txt')
    s = x.readlines()
    b = int(s.strip())
except OSError as error:
    print("OS is error : ",error)
except ValueError :
    print("could not convert data to integer")
except Exception as error:
    print(f"Unexpected {error = }, {type(error)=}")
finally:
    print("FINALLY is always running")



