import tkinter as tk


class Header(tk.Frame):
    """ Default header with breadcrumb bar, title, and instruction text """
    def __init__(self, parent, title, instruction):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # breadcrumb
        tk.Frame(self, bg="orange", height=30).pack(fill="x")

        # title and text
        tk.Label(self, text=title).pack(expand=1)
        tk.Label(self, wraplength=700, text=instruction).pack(expand=1)


class NavButton(tk.Button):
    """ Standard layout for 'previous'- & 'next'-button """
    def __init__(self, parent, color, line):
        tk.Button.__init__(self, parent, bg=color, text=line)
        self.parent = parent


class Footer(tk.Frame):
    """ Default footer containing a 'previous'- and a 'next'-button """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="gray", height=200)
        NavButton(self, color="white", line="PREVIOUS").pack(side="left")
        NavButton(self, color="pink", line="NEXT").pack(side="right")


class Headline(tk.Label):
    """ Default headline style (NOT title style!) """
    def __init__(self, parent, line):
        tk.Label.__init__(self, parent, text=line, bg="aqua")
        self.parent = parent


class ToggleButton(tk.Button):
    """ Default style for buttons without borders / selectable text """
    def __init__(self, parent, line):
        tk.Button.__init__(self, parent, text=line)
        self.parent = parent


class Races(tk.Frame):
    """ Main races frame (IIa) """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent

        # initialize content
        Headline(self, line="Human").grid(row=0, column=0)
        ToggleButton(self, line="Breton").grid(row=1, column=0)
        ToggleButton(self, line="Nord").grid(row=2, column=0)
        ToggleButton(self, line="Imperial").grid(row=3, column=0)
        ToggleButton(self, line="Redguard").grid(row=4, column=0)

        Headline(self, line="Mer").grid(row=0, column=1)
        ToggleButton(self, line="Altmer").grid(row=1, column=1)
        ToggleButton(self, line="Bosmer").grid(row=2, column=1)
        ToggleButton(self, line="Dunmer").grid(row=3, column=1)
        ToggleButton(self, line="Orc").grid(row=4, column=1)

        Headline(self, line="Beast").grid(row=0, column=2)
        ToggleButton(self, line="Argonian").grid(row=1, column=2)
        ToggleButton(self, line="Khajiit").grid(row=2, column=2)


class ContentWrapper(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="blue")
        self.parent = parent

        Header(self, "Title", "At vero eos et accusam et justo duo dolores et ea rebum.").pack(fill="x")
        Races(self).pack(fill="x")
        Footer(self).pack(fill="x", side="bottom")


class Start(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="white")
        self.parent = parent

        # initialize content
        __image = tk.Frame(self, bg="gray", width=150, height=150)
        __title = tk.Label(self, bg="white", text="Welcome!")
        __introduction = tk.Label(self, bg="white", wraplength=700,
            text="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                 "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                 "magna aliquyam erat, sed diam voluptua.")
        __wrapper = tk.Frame(self, bg="red", width=300, height=100)
        __new = tk.Button(__wrapper, text="NEW")
        __existing = tk.Button(__wrapper, text="EXISTING")

        __image.pack(expand=1)
        __title.pack(expand=1)
        __introduction.pack(expand=1)
        __wrapper.pack(expand=1)
        __new.pack(side="left")
        __existing.pack(side="right")


def configure_window(self):
    # title
    self.title("Skyrim Calculator")

    # size
    width = 800
    height = 600
    self.minsize(width, height)

    # position
    x_pos = (self.winfo_screenwidth() - width) / 2
    y_pos = (self.winfo_screenheight() - height) / 2
    self.geometry("%dx%d+%d+%d" % (width, height, x_pos, y_pos))


if __name__ == "__main__":
    root = tk.Tk()
    configure_window(root)
    start = ContentWrapper(root).pack(fill="both", expand=1)
    root.mainloop()
