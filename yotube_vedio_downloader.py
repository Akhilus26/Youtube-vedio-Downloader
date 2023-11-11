from pytube import YouTube
from tkinter import *

high_resolution_vedio_path="./high_resolution_vedio"
audiopath="./audio_downloaded"
low_resolution_vedio_path="./low_resolution_vedio"

window=Tk()
# window.geometry("400x700")
window.title("YouTube Vedio/Audio Downloader")
download_frame=Frame(window)
failed_frame=Frame(window)
download_detail_frame=Frame(window)


#-----------------------function part--------------------------# 

def frame_creator():
    global download_frame
    if download_frame:
        download_frame.destroy()
    download_frame=Frame(window)
    download_frame.grid(row=6,column=0,columnspan=2)
    
#---------------------vedio downloading part--------------------#

def high_res_donload_click():

    yd=yt.streams.get_highest_resolution()
    yd.download(f"{high_resolution_vedio_path}")
    downloaded_label=Label(download_frame, text="Downloaded", fg="green", font=('Times New Roman', 12))
    downloaded_label.grid(row=8, column=0, columnspan=2)

def low_res_download_click():

    yd=yt.streams.get_lowest_resolution()
    yd.download(f"{low_resolution_vedio_path}")   
    downloaded_label=Label(download_frame, text="Downloaded", fg="green", font=('Times New Roman', 12))
    downloaded_label.grid(row=11, column=0, columnspan=2) 

def vedio_click():
    frame_creator()
    vedio_title_highframe_label=Label(download_frame,text="High Quality file", width=15, height=5, font=('Times New Roman', 13))
    vedio_title_highframe_label.grid(row=7, column=0)
    vedio_download_high_button=Button(download_frame,text="Download", fg="white", bg = "green",width=20, command=high_res_donload_click, pady=7)
    vedio_download_high_button.grid(row=7, column=1)

    vedio_title_lowframe_label=Label(download_frame,text="Low Quality file",width=15,height=5, font=('Times New Roman', 13))
    vedio_title_lowframe_label.grid(row=9,column=0)
    vedio_download_low_button=Button(download_frame,text="Download",fg="white", bg = "green",width=20, command=low_res_download_click, pady=7)
    vedio_download_low_button.grid(row=9,column=1)

#------------------ audio downloading part ---------------------#

def audio_download_click():

    yd=yt.streams.get_audio_only()
    yd.download(f"{audiopath}")
    downloaded_label=Label(download_frame, text="Downloaded", fg="green", font=('Times New Roman', 12))
    downloaded_label.grid(row=9, column=0, columnspan=2)

def audio_click():
    frame_creator()
    auido_title_label=Label(download_frame,text="audio file",width=15,height=5, font=('Times New Roman', 13))
    auido_title_label.grid(row=7,column=0)
    audio_download_button=Button(download_frame,text="Download",fg="white", bg = "green",width=20,command=audio_download_click ,pady=7 )
    audio_download_button.grid(row=7,column=1)




def download():
    

    try:
        global yt
        global failed_frame
        global download_detail_frame
            
        link = link_entry.get('1.0',END)

        yt=YouTube(link)
        title=yt.title

        download_detail_frame=Frame(window)
        download_detail_frame.grid(row=3,column=0,columnspan=2)

        yt_details=Label(download_detail_frame,text="YouTube Vedio Details - ",font=('Times New Roman', 15, UNDERLINE))
        yt_details.grid(row=3,column=0,columnspan=2,pady=5)

        yt_title_label=Label(download_detail_frame,text=f"{ title}",fg="#e11d48",font=('Times New Roman', 13))
        yt_title_label.grid(row=4,column=0,columnspan=2,pady=20)
        

        audio_button=Button(download_detail_frame,text="Audio",width=20 ,bg="#f53939",fg="white", command=audio_click, pady=10)
        audio_button.grid(row=5,column=1,pady=30)

        vedio_button=Button(download_detail_frame,text="Vedio",width=20,bg="grey",fg="white", command=vedio_click,pady=10)
        vedio_button.grid(row=5,column=0,pady=30)
        
    except:
        failed_frame=Frame(window)
        failed_frame.grid(row=11,column=0,columnspan=2)

        failed=Label(failed_frame,text="Enter a Valid URL ",fg="red")
        failed.grid(row=11,column=0,columnspan=2)
        if download_detail_frame:
            download_detail_frame.destroy()
        if download_frame:
            download_frame.destroy()
        
    else:
        if failed_frame:
            failed_frame.destroy()

def delete_link_click():
    link_entry.delete('1.0',END)
    if download_detail_frame:
        download_detail_frame.destroy()
    if download_frame:
        download_frame.destroy()

title_label=Label(window,text="YouTube Vedio/Audio Downloader",fg="#7928ca",width=29,height=4, font=('Times New Roman', 20, 'bold',UNDERLINE))
link_entry=Text(window, state=NORMAL,height=1,width=45,font=('Times New Roman', 14))
link_delete_button=Button(window,text="X",bg="red",fg="white",width=2, command=delete_link_click)
download_button=Button(window,text="Download",command=download, width=40, height=2, bg="#ff0080",fg="white")
exit_button=Button(window,text="Exit Button",command=window.quit,bg="red",fg="white",padx=205,pady=10)

title_label.grid(row=0,column=0,columnspan=2)
link_entry.grid(row=1,column=0,pady=20,columnspan=2)
link_entry.insert(END,"Enter/Past the URL ")
link_delete_button.grid(row=1,column=1,sticky=E,padx=5)
download_button.grid(row=2,column=0,columnspan=2,pady=20)
exit_button.grid(row=12,column=0,columnspan=2)


window.mainloop()
