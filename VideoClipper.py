from tkinter import filedialog
from tkinter import *
import random
import os
import moviepy.editor as mp
from moviepy import *

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    Path_Box.delete("1.0", "end")
    Path_Box.insert(END,folder_path.get())

def browse_button_1():
    global file_path
    filename = filedialog.askdirectory()
    file_path.set(filename)
    OPath_Box.delete("1.0", "end")
    OPath_Box.insert(END,file_path.get())


def start():
    num_of_episodes= int(VidNum_Input.get())
    episode_name= Name_Input.get()
    input_loc= folder_path.get()
    output_loc=file_path.get()
    num_of_clips=int(ClipNum_Input.get())
    len_of_clip=int(ClipLen_Input.get())
    for a in range(1, num_of_episodes+1):
        if choice.get()== "new_folder": 
            output_loc=file_path.get()
            Directory= "/Episode " + str(a)
            path= output_loc+Directory
            if os.path.isdir(path)== False:
                os.mkdir(path)
            output_loc= path
            loc= input_loc + "/" + episode_name + str(a) + str(click.get())
            video = mp.VideoFileClip(loc)
            dur= int(video.duration)
            for i in range(1,num_of_clips+1):
                ran= random.randint(0, dur-len_of_clip)
                Clip = video.subclip(ran, ran+len_of_clip)
                dest= output_loc + "/Clip" + str(a) + str(i)+ ".mp4"
                Clip.write_videofile(dest)
        else:
            loc= input_loc + "/" + episode_name + str(a) + str(click.get())
            video = mp.VideoFileClip(loc)
            dur= int(video.duration)
            for i in range(1,num_of_clips+1):
                ran= random.randint(0, dur-len_of_clip)
                Clip = video.subclip(ran, ran+len_of_clip)
                dest= output_loc + "/Clip" + str(a) + str(i)+ ".mp4"
                Clip.write_videofile(dest)
            
root= Tk()
folder_path = StringVar()
file_path= StringVar()
root.title("The Ultimate Video Clip Maker")
root.iconbitmap(r".\img\icon.ico")
root.geometry("850x400")

click= StringVar(root, "3")
choice=StringVar(root, "old_folder")

Label(root, text= "THE ULTIMATE VIDEO CLIP MAKER", font= "Roboto 30").place(x= 100, y= 25)
Label(root, text= "-------------------------------------------------------------").place(x= 270, y= 80)

# Path Of Folder 
Path_text= Label(root, text= "Enter Path Of Folders:", font= "Aerial 12")
Path_text.place(x=150, y=120)
Path_Box= Text(root, width=39, height=1)
Path_Box.place(x=315, y=122)
Button1 = Button(text="...", command=browse_button).place(x=647, y=120)

# Name of Each File
Name_text= Label(root, text= "Name Of Each File:", font= "Aerial 12")
Name_text.place(x=150, y=150)
Name_Input= Entry(root, width= 58)
Name_Input.place(x=315, y= 153)

#Video File Type
VidType_text= Label(root, text= "Video File Extension:", font= "Aerial 12")
VidType_text.place(x=150, y=180)
Radiobutton1= Radiobutton(root, text = "MPEG-4 (.mp4)", variable = click, value = ".mp4", font= "Aerial 10")
Radiobutton1.place(x = 360, y= 180)
Radiobutton2= Radiobutton(root, text = "MATROSKA (mkv)", variable = click, value = ".mkv", font= "Aerial 10")
Radiobutton2.place(x = 535, y= 180)

# Number Of Videos
VidNum_text= Label(root, text= "Number Of Videos:", font= "Aerial 12")
VidNum_text.place(x=150, y=210)
VidNum_Input= Entry(root, width= 4)
VidNum_Input.place(x=288, y= 213)

# Number Of Clips
ClipNum_text= Label(root, text= "Number Of Clips Per Ep:", font= "Aerial 12")
ClipNum_text.place(x= 322, y=210)
ClipNum_Input= Entry(root, width= 4)
ClipNum_Input.place(x=500, y= 213)

# Length Of Clips
ClipLen_text= Label(root, text= "Length Of Clip:", font= "Aerial 12")
ClipLen_text.place(x=530, y=210)
ClipLen_Input= Entry(root, width= 4)
ClipLen_Input.place(x=638, y= 213)

# Path Of Output File Folder 
OPath_text= Label(root, text= "Enter Path Of Output:", font= "Aerial 12")
OPath_text.place(x=150, y=240)
OPath_Box= Text(root, width=40, height=1)
OPath_Box.place(x=315, y=242)
Button7 = Button(text="...", command=browse_button_1)
Button7.place(x=647, y=240)

#Video File Type
OutputFolder_text= Label(root, text= "Output Destination Settings:", font= "Aerial 12")
OutputFolder_text.place(x=150, y=270)
RadioButton3= Radiobutton(root, text = "Make New Folder", variable=choice, value = "new_folder", font= "Aerial 10")
RadioButton3.place(x = 360, y= 270)
Radiobutton4= Radiobutton(root, text = "Keep in Current Folder", variable=choice, value=".old_folder", font= "Aerial 10")
Radiobutton4.place(x = 535, y= 270)


Label(root, text= "-------------------------------------------------------------").place(x= 270, y= 300)

Button9= Button(root, height= 3, width= 20, text= "START", command=start, borderwidth= 1, relief= "solid").place(x=350, y=320)

mainloop()