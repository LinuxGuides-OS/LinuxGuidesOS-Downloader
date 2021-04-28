from tkinter import W, messagebox
import wget
import tkinter

root = tkinter.Tk()
root.title("LinuxGuidesOS DL")
tkinter.Label(root, text="LinuxGuidesOS DL\n 21.04.2 Alpha").pack()


def dl():
    if int(var.get()) == 1:
        messagebox.showinfo("Downloading...", "To start press Ok this will take some time!")
        wget.download("https://cd.linuxguides-os.de/alpha/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso")
        messagebox.showinfo("File saved", "File saved in current dir.")
        exit()
    if int(var.get()) == 2:
        messagebox.showinfo("Downloading...", "To start press Ok this will take some time!")
        wget.download("https://ftp.halifax.rwth-aachen.de/osdn/linuxguides-os/75010/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso")
        messagebox.showinfo("File saved", "File saved in current dir.")
        exit()
    if int(var.get()) == 3:
        messagebox.showinfo("Downloading...", "To start press Ok this will take some time!")
        wget.download("https://lgos.rexum.gratis-host.de/alpha/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso")
        messagebox.showinfo("File saved", "File saved in current dir.")
        exit()
    if int(var.get()) == 4:
        messagebox.showinfo("Downloading...", "To start press Ok this will take some time!")
        wget.download("https://archive.org/download/linux-guides-os-21.04.2-alpha-aphrodite/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso")
        messagebox.showinfo("File saved", "File saved in current dir.")
        exit()
    if int(var.get()) == 5:
        messagebox.showinfo("Downloading...", "To start press Ok this will take some time!")
        wget.download("https://cdn-33.anonfiles.com/16c9Aasaue/b4896af6-1619622608/LinuxGuides-OS-21.04.2_Alpha_Aphrodite.iso")
        messagebox.showinfo("File saved", "File saved in current dir.")
        exit()


var = tkinter.IntVar()
tkinter.Radiobutton(root, text="Official Server", variable=var, value=1, command=dl).pack(anchor=W)
tkinter.Radiobutton(root, text="RWTH Aachen", variable=var, value=2, command=dl).pack(anchor=W)
tkinter.Radiobutton(root, text="Gratis-Host", variable=var, value=3, command=dl).pack(anchor=W)
tkinter.Radiobutton(root, text="ArchiveORG", variable=var, value=4, command=dl).pack(anchor=W)
tkinter.Radiobutton(root, text="AnonFiles", variable=var, value=5, command=dl).pack(anchor=W)

root.mainloop()
