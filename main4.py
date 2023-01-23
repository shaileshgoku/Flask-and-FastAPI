# from fastapi import FastAPI

# from pydantic import BaseModel

# class Star(BaseModel):
#     name : str
#     price: int
# app = FastAPI()

# @app.get("/")
# def root_default():
#     return {"hello":"galaxy"}

# @app.get("/star_count/{count}")
# def root_get_count(count: str):
#     return{"total star count": count}

# @app.put("/star_count/{count}")
# def root_get_count(count: int, star_name: Star):
#     return{"total star count": count, "name of star": star_name.name, "price of star": star_name.price}

import textwrap

def wrap(string, max_width):
    s = textwrap.wrap(string, max_width)
    for i in s:
        if i == None:
            pass
        else:
            print(i)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


