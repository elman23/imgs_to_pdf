import tkinter
import tkinter.messagebox
import customtkinter

from Converter import Converter
from Image import Image
from typing import List

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class ConverterGUIApp(customtkinter.CTk):

    converter: Converter

    def __init__(self):
        super().__init__()

        self.converter = Converter()

        self.title("CustomTkinter complex_example.py")
        # self.geometry(f"{1100}x{580}")
        self.geometry(f"{850}x{600}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Convert Images To PDF", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.files_frame = customtkinter.CTkFrame(self)
        self.files_frame.grid(row=0, column=1, padx=(
            20, 20), pady=(20, 0), sticky="ew")
        self.chosen_files_title = customtkinter.CTkLabel(
            self.files_frame, text="Chosen files", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.chosen_files_title.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.chosen_files_entry = customtkinter.CTkLabel(
            self.files_frame, text="")
        self.chosen_files_entry.grid(row=1, column=0, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="new")

        self.output_file_recap_frame = customtkinter.CTkFrame(self)
        self.output_file_recap_frame.grid(row=1, column=1, padx=(
            20, 20), pady=(20, 0), sticky="ew")
        self.out_file_title = customtkinter.CTkLabel(
            self.output_file_recap_frame, text="Output file", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.out_file_title.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.output_file_label = customtkinter.CTkLabel(
            self.output_file_recap_frame, text="")
        self.output_file_label.grid(row=1, column=0, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="new")

        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=2, column=1, padx=(
            20, 20), pady=(20, 0), sticky="ew")
        self.image_file_entry = customtkinter.CTkEntry(
            self.entry_frame, placeholder_text="Image file name")
        self.image_file_entry.grid(row=1, column=0, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="ew")
        self.main_button_1 = customtkinter.CTkButton(
            text="Add file",
            master=self.entry_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
            command=self.add_image)
        self.main_button_1.grid(row=1, column=3, padx=(
            20, 20), pady=(20, 20), sticky="new")

        self.output_file_frame = customtkinter.CTkFrame(self)
        self.output_file_frame.grid(row=3, column=1, padx=(
            20, 20), pady=(20, 0), sticky="ew")
        self.output_file_entry = customtkinter.CTkEntry(
            self.output_file_frame, placeholder_text="Output file name")
        self.output_file_entry.grid(row=1, column=0, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="ew")
        self.main_button_3 = customtkinter.CTkButton(
            text="Add output file",
            master=self.output_file_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
            command=self.add_output_file)
        self.main_button_3.grid(row=1, column=3, padx=(
            20, 20), pady=(20, 20), sticky="new")

        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=1, column=2, padx=(
            20, 20), pady=(20, 0), sticky="ew")
        self.orientation = tkinter.StringVar(value="portrait")
        self.label_radio_group = customtkinter.CTkLabel(
            master=self.radiobutton_frame, text="Image orientation:")
        self.label_radio_group.grid(
            row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(
            text="Portrait",
            master=self.radiobutton_frame, variable=self.orientation, value="portrait")
        self.radio_button_1.grid(
            row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(
            text="Landscape",
            master=self.radiobutton_frame, variable=self.orientation, value="landscape")
        self.radio_button_2.grid(
            row=2, column=2, pady=10, padx=20, sticky="n")

        self.convert_frame = customtkinter.CTkFrame(self)
        self.convert_frame.grid(row=2, column=2, padx=(
            20, 20), pady=(20, 0), sticky="ew")
        self.sidebar_button_1 = customtkinter.CTkButton(
            self.convert_frame, command=self.convert, text="Convert")
        self.sidebar_button_1.grid(
            row=0, column=1, padx=20, pady=10, sticky="sew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def add_image(self) -> None:
        file_name = self.image_file_entry.get()
        self.image_file_entry.delete(0, len(file_name))
        self.converter.add_img(file_name, orientation=self.orientation.get())
        image_names = [img.file_name for img in self.converter.imgs]
        self.chosen_files_entry.configure(text=self.format_text(image_names))
        print(image_names)

    def format_text(self, image_names):
        text = ""
        for image_name in image_names:
            if text == "":
                text += image_name
            else:
                text += "\n" + image_name
        return text

    def add_output_file(self) -> None:
        output_file = self.output_file_entry.get()
        self.converter.add_out_file(output_file)
        self.output_file_label.configure(text=output_file)
        self.output_file_entry.delete(0, len(output_file))
        print(self.converter.out_file)

    def convert(self) -> None:
        if self.converter.out_file is None:
            return
        if len(self.converter.imgs) == 0:
            return
        print("Converting...")
        self.converter.convert_images()


if __name__ == "__main__":
    app = ConverterGUIApp()
    app.mainloop()
