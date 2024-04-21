from fastapi import FastAPI

app = FastAPI()

@app.get("/waist5.32e-07/contrast1.2/radius0.1")
def get_waist5_32e_07_contrast_1_2_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast1.2/radius0.2")
def get_waist5_32e_07_contrast_1_2_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast1.2/radius0.5")
def get_waist5_32e_07_contrast_1_2_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast1.2/radius0.05")
def get_waist5_32e_07_contrast_1_2_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 1.2/waist5.32e-07contrast1.2size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast2.1/radius0.1")
def get_waist5_32e_07_contrast_2_1_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast2.1/radius0.2")
def get_waist5_32e_07_contrast_2_1_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast2.1/radius0.5")
def get_waist5_32e_07_contrast_2_1_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast2.1/radius0.05")
def get_waist5_32e_07_contrast_2_1_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 2.1/waist5.32e-07contrast2.1size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3/radius0.1")
def get_waist5_32e_07_contrast_3_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3/radius0.2")
def get_waist5_32e_07_contrast_3_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3/radius0.5")
def get_waist5_32e_07_contrast_3_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3/radius0.05")
def get_waist5_32e_07_contrast_3_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3/waist5.32e-07contrast3size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3.9/radius0.1")
def get_waist5_32e_07_contrast_3_9_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3.9/radius0.2")
def get_waist5_32e_07_contrast_3_9_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3.9/radius0.5")
def get_waist5_32e_07_contrast_3_9_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist5.32e-07/contrast3.9/radius0.05")
def get_waist5_32e_07_contrast_3_9_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0/contrast 3.9/waist5.32e-07contrast3.9size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast1.2/radius0.1")
def get_waist4_0303e_07_contrast_1_2_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast1.2/radius0.2")
def get_waist4_0303e_07_contrast_1_2_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast1.2/radius0.5")
def get_waist4_0303e_07_contrast_1_2_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast1.2/radius0.05")
def get_waist4_0303e_07_contrast_1_2_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 1.2/waist4.0303e-07contrast1.2size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast2.1/radius0.1")
def get_waist4_0303e_07_contrast_2_1_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast2.1/radius0.2")
def get_waist4_0303e_07_contrast_2_1_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast2.1/radius0.5")
def get_waist4_0303e_07_contrast_2_1_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast2.1/radius0.05")
def get_waist4_0303e_07_contrast_2_1_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 2.1/waist4.0303e-07contrast2.1size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3/radius0.1")
def get_waist4_0303e_07_contrast_3_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3/radius0.2")
def get_waist4_0303e_07_contrast_3_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3/radius0.5")
def get_waist4_0303e_07_contrast_3_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3/radius0.05")
def get_waist4_0303e_07_contrast_3_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3/waist4.0303e-07contrast3size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3.9/radius0.1")
def get_waist4_0303e_07_contrast_3_9_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3.9/radius0.2")
def get_waist4_0303e_07_contrast_3_9_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3.9/radius0.5")
def get_waist4_0303e_07_contrast_3_9_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist4.0303e-07/contrast3.9/radius0.05")
def get_waist4_0303e_07_contrast_3_9_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 1.32/contrast 3.9/waist4.0303e-07contrast3.9size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast1.2/radius0.1")
def get_waist2_5961e_07_contrast_1_2_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast1.2/radius0.2")
def get_waist2_5961e_07_contrast_1_2_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast1.2/radius0.5")
def get_waist2_5961e_07_contrast_1_2_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast1.2/radius0.05")
def get_waist2_5961e_07_contrast_1_2_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 1.2/waist2.5961e-07contrast1.2size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast2.1/radius0.1")
def get_waist2_5961e_07_contrast_2_1_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast2.1/radius0.2")
def get_waist2_5961e_07_contrast_2_1_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast2.1/radius0.5")
def get_waist2_5961e_07_contrast_2_1_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast2.1/radius0.05")
def get_waist2_5961e_07_contrast_2_1_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 2.1/waist2.5961e-07contrast2.1size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3/radius0.1")
def get_waist2_5961e_07_contrast_3_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3/radius0.2")
def get_waist2_5961e_07_contrast_3_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3/radius0.5")
def get_waist2_5961e_07_contrast_3_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3/radius0.05")
def get_waist2_5961e_07_contrast_3_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3/waist2.5961e-07contrast3size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3.9/radius0.1")
def get_waist2_5961e_07_contrast_3_9_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3.9/radius0.2")
def get_waist2_5961e_07_contrast_3_9_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3.9/radius0.5")
def get_waist2_5961e_07_contrast_3_9_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.5961e-07/contrast3.9/radius0.05")
def get_waist2_5961e_07_contrast_3_9_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.0492/contrast 3.9/waist2.5961e-07contrast3.9size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast1.2/radius0.1")
def get_waist2_1635e_07_contrast_1_2_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast1.2/radius0.2")
def get_waist2_1635e_07_contrast_1_2_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast1.2/radius0.5")
def get_waist2_1635e_07_contrast_1_2_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast1.2/radius0.05")
def get_waist2_1635e_07_contrast_1_2_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 1.2/waist2.1635e-07contrast1.2size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast2.1/radius0.1")
def get_waist2_1635e_07_contrast_2_1_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast2.1/radius0.2")
def get_waist2_1635e_07_contrast_2_1_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast2.1/radius0.5")
def get_waist2_1635e_07_contrast_2_1_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast2.1/radius0.05")
def get_waist2_1635e_07_contrast_2_1_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 2.1/waist2.1635e-07contrast2.1size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3/radius0.1")
def get_waist2_1635e_07_contrast_3_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3/radius0.2")
def get_waist2_1635e_07_contrast_3_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3/radius0.5")
def get_waist2_1635e_07_contrast_3_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3/radius0.05")
def get_waist2_1635e_07_contrast_3_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3/waist2.1635e-07contrast3size0.05/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3.9/radius0.1")
def get_waist2_1635e_07_contrast_3_9_radius_0_1():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.1/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.1/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3.9/radius0.2")
def get_waist2_1635e_07_contrast_3_9_radius_0_2():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.2/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.2/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3.9/radius0.5")
def get_waist2_1635e_07_contrast_3_9_radius_0_5():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.5/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.5/Fz.txt').readlines()]
    return table_x, table_z

@app.get("/waist2.1635e-07/contrast3.9/radius0.05")
def get_waist2_1635e_07_contrast_3_9_radius_0_05():
    table_x = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.05/Fx.txt').readlines()]
    table_z = [i.split() for i in open('Forces/waist=wl0 2.459/contrast 3.9/waist2.1635e-07contrast3.9size0.05/Fz.txt').readlines()]
    return table_x, table_z