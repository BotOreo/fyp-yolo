import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constants
image_folder = 'cube_train' #folder directory
savedir = 'annotations'
obj1 = 'obstacle'
#obj2 = 'car'


def line_select_callback(clk, rls):

    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata))) #clk refer to take coordinate when click
    br_list.append((int(rls.xdata), int(rls.ydata)))#rls refer to take coordinate when release
    #object_list.append(obj)
    '''
    classify=input("Press 'f' for fake, 'r' for real : ")
    if classify=='f':
        object_list.append(obj)
        #plt.connect('key_press_event', onkeypress)
    elif classify=='r':
        object_list.append(obj2)
        #plt.connect('key_press_event', onkeypress)
    elif classify=='q' or'Q':
       key = plt.connect('key_press_event', onkeypress)


    try:
        if keyboard.is_pressed('f' or 'F'):
            object_list.append(obj)
        elif keyboard.is_pressed('r' or 'R'):
            object_list.append(obj2)
    except:
        print("Invalid!")
    '''
def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'a': #press p if it's a person
        object_list.append(obj1)
        write_xml(image_folder, img, object_list,tl_list,br_list,savedir)
        print(tl_list,br_list,object_list)
        #write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()
    '''   
    #this part of the code is not needed unless I have multiple class
     
    elif event.key == 'c': #press P if it's a car
        object_list.append(obj2)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        print(tl_list,br_list,object_list)
        #write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()
    '''

def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        mngr = plt.get_current_fig_manager()
        #mngr.window.setGeometry(250, 120, 1280, 1024) #this line no need, it's just to show where to pop up
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #conver BGR format to RGB
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
        bbox = plt.connect('key_press_event', toggle_selector)

        key = plt.connect('key_press_event', onkeypress) #to connect with def onkeypress event so that if we hit p or c, it will move on
        plt.show()
