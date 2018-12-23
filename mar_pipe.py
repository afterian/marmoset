#########mar_pipe v.01
##pipeline tools for Marmoset
#


import mset
import os
import json

project_dir = "E:/projects/ssd/asset/charactor/aurora/"
source_dir = "assets/"
model_dir = "E:/projects/marmoset/models/"
model_low_dir =""
model_high_dir=""
material_dir ="E:/source/materials/sample/"
export_dir=""
frames_dir=""
textureU = "1"
textureV = "1"

# File formats
formats = [
    "psd",
    "png"
    "jpg",
    "jpeg",
    "tga",
    "bmp"
]

sufx = {
    "albedo":"_color.png",
    "surface":"_bumpMap.png",
    "microsurface":"_reflectionGlossiness.png",
    "reflectivy":"_reflectionColor.png",
    }

###### get_project_folder v.01
## gets the directory for the root of the scenes
def get_project_folder() :
    path = mset.showOpenFolderDialog()
    if path != '':
        project_folder_field.value = path
        project_dir = path
    print (path)

###### get_material_folder v.01
## gets the directory for the root of the scenes
def get_material_folder() :
    path = mset.showOpenFolderDialog()
    if path != '':
        material_folder_field.value = path
        material_dir = path
    print (path)

###### get_model_folder v.01
## gets the directory for the root of the scenes
def get_model_folder() :
    path = mset.showOpenFolderDialog()
    if path != '':
        model_folder_field.value = path
        model_dir=path
    print (path)

#### create material from Images v.01
### creates a material from src Images
def create_mat_images ():
    print ("building simple Sp gloss shader")
    # Determine search area
    search_dir = material_dir
    files = os.listdir(search_dir)
    first_file = files[0]
    #gets the material name prefix
    prefix = first_file.split("_")
    matName = prefix[0]
    #matNameb = (prefix[0]+prefix[1])


    #finds images according to naming convensions
    img_albedo = (material_dir + matName + sufx["albedo"])
    img_normal = (material_dir + matName + sufx["surface"])
    img_gloss = (material_dir + matName + sufx["microsurface"])
    img_specular = (material_dir + matName + sufx["reflectivy"])

    #create and build material
    mat = mset.Material(name=matName)
    mat.getSubroutine("surface").setField( "Normal Map", mset.Texture(img_normal))
    mat.setSubroutine("microsurface","Gloss")
    mat.getSubroutine("microsurface").setField( "Gloss Map", mset.Texture(img_gloss))
    mat.getSubroutine("albedo").setField( "Albedo Map", mset.Texture(img_albedo))
    mat.setSubroutine("reflectivity","Specular")
    mat.getSubroutine("reflectivity").setField( "Specular Map", mset.Texture(img_specular))




    ## import pipeline pbrs.
    #impMat=mset.importMaterial("E:/source/materials/sample/sample.sbsar", "sample")
    #impMat=mset.importMaterial(first_file, "sample")
    #impMat=mset.importMaterial(first_file, matName)
    #impMatb=mset.importMaterial(secondfile, matName)

def show_json_data ():
    data_loc = open((material_dir + "zdata.json")).read()
    mat_data = json.loads(data_loc)
    print (mat_data["textureScale"])


## ui
window = mset.UIWindow("mar.pipe v.01")

#project_settings

settings_drawer_ui = mset.UIDrawer(name="Settings")
settings_drawer = mset.UIWindow(name="", register=False)
settings_drawer_ui.containedControl = settings_drawer
window.addElement(settings_drawer_ui)

#project dir
settings_drawer.addElement(mset.UILabel("project"))
file_button = mset.UIButton("...")
file_button.onClick = get_project_folder
settings_drawer.addElement(file_button)
project_folder_field = mset.UITextField()
project_folder_field.value = project_dir
settings_drawer.addElement(project_folder_field)



#material_dir
settings_drawer.addReturn()
settings_drawer.addElement(mset.UILabel("materials"))
file_button = mset.UIButton("...")
file_button.onClick = get_material_folder
settings_drawer.addElement(file_button)
material_folder_field = mset.UITextField()
material_folder_field.value = material_dir
settings_drawer.addElement(material_folder_field)

#model_dir
settings_drawer.addReturn()
settings_drawer.addElement(mset.UILabel("models"))
file_button = mset.UIButton("...")
file_button.onClick = get_model_folder
settings_drawer.addElement(file_button)
model_folder_field = mset.UITextField()
model_folder_field.value = model_dir
settings_drawer.addElement(model_folder_field)

#### import drawer

window.addReturn()
import_drawer_ui = mset.UIDrawer(name="import")
import_drawer = mset.UIWindow(name="", register=False)
import_drawer_ui.containedControl = import_drawer
window.addElement(import_drawer_ui)

#### create drawer

window.addReturn()
create_drawer_ui = mset.UIDrawer(name="Create")
create_drawer = mset.UIWindow(name="", register=False)
create_drawer_ui.containedControl = create_drawer
window.addElement(create_drawer_ui)

create_mat_images_button = mset.UIButton("Material from images")
create_mat_images_button.onClick = create_mat_images
create_drawer.addElement(create_mat_images_button)

json_data = mset.UIButton("data")
json_data.onClick = show_json_data
create_drawer.addElement(json_data)

#
window.addReturn()

close_button = mset.UIButton("Close")
close_button.onClick = lambda: mset.shutdownPlugin()
window.addElement(close_button)











"""
window.addReturn()



drawer = mset.UIDrawer(name="Settings")
drawer_window = mset.UIWindow(name="", register=False)
drawer.containedControl = drawer_window

scrollbox = mset.UIScrollBox()
scrollbox_window = mset.UIWindow(name="", register=False)
scrollbox.containedControl = scrollbox_window

ls1 = mset.UIListBox("List 1")
ls1.addItem("1")
ls1.addItem("2")
ls1.addItem("3")

ls2 = mset.UIListBox("List 2")
ls2.addItem("4")
ls2.addItem("5")
ls2.addItem("6")


slider = mset.UISliderInt(min=5, max=128, name="Slider")

button = mset.UIButton("Button")

icon_button = mset.UIButton()
icon_button.setIcon(os.path.abspath(os.path.join(os.curdir, "data/gui/control/animationplay.tga")))

picker = mset.UIColorPicker("Color")

text = mset.UITextField()

checkbox = mset.UICheckBox()

# Render
window.addElement(slider)
window.addReturn()
window.addElement(scrollbox)
scrollbox_window.addElement(drawer)
drawer_window.addElement(button)
drawer_window.addSpace(16)
drawer_window.addElement(checkbox)
drawer_window.addReturn()
drawer_window.addElement(ls1)
drawer_window.addElement(ls2)
drawer_window.addReturn()
drawer_window.addElement(icon_button)
window.addReturn()
window.addElement(picker)
window.addReturn()
window.addElement(text)
"""
