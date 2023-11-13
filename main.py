from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

# Массивы сил для R = 100 nm

#some_file_path = "C:/Users/yana5/PycharmProjects/pythonProject/trying/arr_Fx.json"
@app.get("/R100nmFX")
async def R100nmFX():
    return FileResponse("C:/Users/yana5/PycharmProjects/pythonProject/trying/arr_Fx.json")

@app.get("/R100nmFY")
async def R100nmFY():
    return FileResponse("C:/Users/yana5/PycharmProjects/pythonProject/trying/arr_Fy.json")

@app.get("/R100nmFZ")
async def R100nmFZ():
    return FileResponse("C:/Users/yana5/PycharmProjects/pythonProject/trying/arr_Fz.json")
###############################################3
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/1")
def read_one():
    return ['система 1 тут будут два массива для Fx Fz']
@app.get("/2")
def read_two():
    return [2,2,2,4,5,6,7,8]
@app.get("/3")
def read_three():
    return [3,3,1,4,5,6,7,8]
@app.get("/4")
def read_four():
    return [4,4,1,4,5,6,7,8]

@app.get("/waist1/radius0.05/contrast1.2")
def get_waist_1_radius_0_05_contrast_1_2():
    return [1, 0.05, 1.2]

@app.get("/waist1/radius0.05/contrast2.1")
def get_waist_1_radius_0_05_contrast_2_1():
    return [1, 0.05, 2.1]

@app.get("/waist1/radius0.05/contrast3")
def get_waist_1_radius_0_05_contrast_3():
    return [1, 0.05, 3]

@app.get("/waist1/radius0.05/contrast3.9")
def get_waist_1_radius_0_05_contrast_3_9():
    return [1, 0.05, 3.9]

@app.get("/waist1/radius0.1/contrast1.2")
def get_waist_1_radius_0_1_contrast_1_2():
    return [1, 0.1, 1.2]

@app.get("/waist1/radius0.1/contrast2.1")
def get_waist_1_radius_0_1_contrast_2_1():
    return [1, 0.1, 2.1]

@app.get("/waist1/radius0.1/contrast3")
def get_waist_1_radius_0_1_contrast_3():
    return [1, 0.1, 3]

@app.get("/waist1/radius0.1/contrast3.9")
def get_waist_1_radius_0_1_contrast_3_9():
    return [1, 0.1, 3.9]

@app.get("/waist1/radius0.2/contrast1.2")
def get_waist_1_radius_0_2_contrast_1_2():
    return [1, 0.2, 1.2]

@app.get("/waist1/radius0.2/contrast2.1")
def get_waist_1_radius_0_2_contrast_2_1():
    return [1, 0.2, 2.1]

@app.get("/waist1/radius0.2/contrast3")
def get_waist_1_radius_0_2_contrast_3():
    return [1, 0.2, 3]

@app.get("/waist1/radius0.2/contrast3.9")
def get_waist_1_radius_0_2_contrast_3_9():
    return [1, 0.2, 3.9]

@app.get("/waist1/radius0.5/contrast1.2")
def get_waist_1_radius_0_5_contrast_1_2():
    return [1, 0.5, 1.2]

@app.get("/waist1/radius0.5/contrast2.1")
def get_waist_1_radius_0_5_contrast_2_1():
    return [1, 0.5, 2.1]

@app.get("/waist1/radius0.5/contrast3")
def get_waist_1_radius_0_5_contrast_3():
    return [1, 0.5, 3]

@app.get("/waist1/radius0.5/contrast3.9")
def get_waist_1_radius_0_5_contrast_3_9():
    return [1, 0.5, 3.9]

@app.get("/waist0.5/radius0.05/contrast1.2")
def get_waist_0_5_radius_0_05_contrast_1_2():
    return [0.5, 0.05, 1.2]

@app.get("/waist0.5/radius0.05/contrast2.1")
def get_waist_0_5_radius_0_05_contrast_2_1():
    return [0.5, 0.05, 2.1]

@app.get("/waist0.5/radius0.05/contrast3")
def get_waist_0_5_radius_0_05_contrast_3():
    return [0.5, 0.05, 3]

@app.get("/waist0.5/radius0.05/contrast3.9")
def get_waist_0_5_radius_0_05_contrast_3_9():
    return [0.5, 0.05, 3.9]

@app.get("/waist0.5/radius0.1/contrast1.2")
def get_waist_0_5_radius_0_1_contrast_1_2():
    return [0.5, 0.1, 1.2]

@app.get("/waist0.5/radius0.1/contrast2.1")
def get_waist_0_5_radius_0_1_contrast_2_1():
    return [0.5, 0.1, 2.1]

@app.get("/waist0.5/radius0.1/contrast3")
def get_waist_0_5_radius_0_1_contrast_3():
    return [0.5, 0.1, 3]

@app.get("/waist0.5/radius0.1/contrast3.9")
def get_waist_0_5_radius_0_1_contrast_3_9():
    return [0.5, 0.1, 3.9]

@app.get("/waist0.5/radius0.2/contrast1.2")
def get_waist_0_5_radius_0_2_contrast_1_2():
    return [0.5, 0.2, 1.2]

@app.get("/waist0.5/radius0.2/contrast2.1")
def get_waist_0_5_radius_0_2_contrast_2_1():
    return [0.5, 0.2, 2.1]

@app.get("/waist0.5/radius0.2/contrast3")
def get_waist_0_5_radius_0_2_contrast_3():
    return [0.5, 0.2, 3]

@app.get("/waist0.5/radius0.2/contrast3.9")
def get_waist_0_5_radius_0_2_contrast_3_9():
    return [0.5, 0.2, 3.9]

@app.get("/waist0.5/radius0.5/contrast1.2")
def get_waist_0_5_radius_0_5_contrast_1_2():
    return [0.5, 0.5, 1.2]

@app.get("/waist0.5/radius0.5/contrast2.1")
def get_waist_0_5_radius_0_5_contrast_2_1():
    return [0.5, 0.5, 2.1]

@app.get("/waist0.5/radius0.5/contrast3")
def get_waist_0_5_radius_0_5_contrast_3():
    return [0.5, 0.5, 3]

@app.get("/waist0.5/radius0.5/contrast3.9")
def get_waist_0_5_radius_0_5_contrast_3_9():
    return [0.5, 0.5, 3.9]

@app.get("/waist0.25/radius0.05/contrast1.2")
def get_waist_0_25_radius_0_05_contrast_1_2():
    return [0.25, 0.05, 1.2]

@app.get("/waist0.25/radius0.05/contrast2.1")
def get_waist_0_25_radius_0_05_contrast_2_1():
    return [0.25, 0.05, 2.1]

@app.get("/waist0.25/radius0.05/contrast3")
def get_waist_0_25_radius_0_05_contrast_3():
    return [0.25, 0.05, 3]

@app.get("/waist0.25/radius0.05/contrast3.9")
def get_waist_0_25_radius_0_05_contrast_3_9():
    return [0.25, 0.05, 3.9]

@app.get("/waist0.25/radius0.1/contrast1.2")
def get_waist_0_25_radius_0_1_contrast_1_2():
    return [0.25, 0.1, 1.2]

@app.get("/waist0.25/radius0.1/contrast2.1")
def get_waist_0_25_radius_0_1_contrast_2_1():
    return [0.25, 0.1, 2.1]

@app.get("/waist0.25/radius0.1/contrast3")
def get_waist_0_25_radius_0_1_contrast_3():
    return [0.25, 0.1, 3]

@app.get("/waist0.25/radius0.1/contrast3.9")
def get_waist_0_25_radius_0_1_contrast_3_9():
    return [0.25, 0.1, 3.9]

@app.get("/waist0.25/radius0.2/contrast1.2")
def get_waist_0_25_radius_0_2_contrast_1_2():
    return [0.25, 0.2, 1.2]

@app.get("/waist0.25/radius0.2/contrast2.1")
def get_waist_0_25_radius_0_2_contrast_2_1():
    return [0.25, 0.2, 2.1]

@app.get("/waist0.25/radius0.2/contrast3")
def get_waist_0_25_radius_0_2_contrast_3():
    return [0.25, 0.2, 3]

@app.get("/waist0.25/radius0.2/contrast3.9")
def get_waist_0_25_radius_0_2_contrast_3_9():
    return [0.25, 0.2, 3.9]

@app.get("/waist0.25/radius0.5/contrast1.2")
def get_waist_0_25_radius_0_5_contrast_1_2():
    return [0.25, 0.5, 1.2]

@app.get("/waist0.25/radius0.5/contrast2.1")
def get_waist_0_25_radius_0_5_contrast_2_1():
    return [0.25, 0.5, 2.1]

@app.get("/waist0.25/radius0.5/contrast3")
def get_waist_0_25_radius_0_5_contrast_3():
    return [0.25, 0.5, 3]

@app.get("/waist0.25/radius0.5/contrast3.9")
def get_waist_0_25_radius_0_5_contrast_3_9():
    return [0.25, 0.5, 3.9]


