from fastapi import FastAPI

app = FastAPI()

@app.get("/waist1/radius0.05/contrast1.2")
def get_waist_1_radius_0_05_contrast_1_2():
    table_x = [i.split() for i in open(f'C:/Users/yana5/OneDrive/Документы/ИТМО/оптический пинцет/Force site/waist5.32e-07contrast1.2size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open(f'C:/Users/yana5/OneDrive/Документы/ИТМО/оптический пинцет/Force site/waist5.32e-07contrast1.2size0.05/Fz.txt').readlines()]
    return table_x, table_z

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
    table_x = [i.split() for i in open(f'C:/Users/yana5/OneDrive/Документы/ИТМО/оптический пинцет/Force site/waist5.32e-07contrast1.2size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open(f'C:/Users/yana5/OneDrive/Документы/ИТМО/оптический пинцет/Force site/waist5.32e-07contrast1.2size0.1/Fz.txt').readlines()]
    return table_x, table_z

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


