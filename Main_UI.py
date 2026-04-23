import customtkinter as ctk 
import math
import re
from sympy import symbols, Eq, solve, sympify

window = ctk.CTk()
window.title('Showcase Algebra Calculator')
window.geometry("800x460")

def main_menu():
    for widget in window.winfo_children():
        widget.destroy()
    ctk.CTkButton(window, text='Calculate the area of a shape', command=calculate_area).pack(pady=10)

def calculate_area():
    for widget in window.winfo_children():
        widget.destroy()
    ctk.CTkButton(window, text='Circle', command=go_to_circle_area).pack(pady=10)
    ctk.CTkButton(window, text='Rectangle', command=go_to_rectangle_area).pack(pady=10)
    ctk.CTkButton(window, text='Right Triangle', command=go_to_right_triangle_area).pack(pady=10)
    ctk.CTkButton(window, text='Regular Triangle', command=go_to_regular_triangle_area).pack(pady=10)
# the classes in order of logic code
class regular_triangle_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.area = 0
        self.side_1_label = ctk.CTkLabel(self, text='Enter the first side length of the triangle')
        self.side_1_label.pack(pady=10)
        self.side_1_entry = ctk.CTkEntry(self, placeholder_text='Side 1')
        self.side_1_entry.pack(pady=10)
        self.side_2_label = ctk.CTkLabel(self, text='Enter the second side length of the triangle')
        self.side_2_label.pack(pady=10)
        self.side_2_entry = ctk.CTkEntry(self, placeholder_text='Side 2')
        self.side_2_entry.pack(pady=10)
        self.angle_label = ctk.CTkLabel(self, text='Enter the angle between the sides in degrees')
        self.angle_label.pack(pady=10)
        self.angle_entry = ctk.CTkEntry(self, placeholder_text='Angle')
        self.angle_entry.pack(pady=10)
        ctk.CTkLabel(self, text='Would you like to round to the nearest tenth (1), hundredth (2), or thousandth (3)?').pack(pady=10)
        self.round_entry = ctk.CTkEntry(self, placeholder_text='Round to')
        self.round_entry.pack(pady=10)
        self.result_label = ctk.CTkLabel(self, text='')
        self.result_label.pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)
        ctk.CTkButton(self, text='Round Area', command=self.round_area).pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)

    def calculate_area(self):
        try:
            side_1 = float(self.side_1_entry.get())
            side_2 = float(self.side_2_entry.get())
            angle = float(self.angle_entry.get())
            if side_1 <= 0 or side_2 <= 0 or angle < 0 or angle > 180:
                self.result_label.configure(text='Invalid input.')
                return
            self.area = 0.5 * side_1 * side_2 * math.sin(math.radians(angle))
            self.result_label.configure(text=f'The area of the triangle is: {round(self.area, 4)}')
        except ValueError:
            self.result_label.configure(text='Invalid input.')

    def round_area(self):
        if self.area == 0:
            self.result_label.configure(text='Calculate area first.')
            return
        if self.round_entry.get() == 'tenth' or self.round_entry.get() == '1':
            self.result_label.configure(text=f'Area rounded to the nearest tenth: {round(self.area, 1)}')
        elif self.round_entry.get() == 'hundredth' or self.round_entry.get() == '2':
            self.result_label.configure(text=f'Area rounded to the nearest hundredth: {round(self.area, 2)}')
        elif self.round_entry.get() == 'thousandth' or self.round_entry.get() == '3':
            self.result_label.configure(text=f'Area rounded to the nearest thousandth: {round(self.area, 3)}')
        else:
            self.result_label.configure(text='Invalid input. Please enter tenth, hundredth, or thousandth.')

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

class right_triangle_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.base_label = ctk.CTkLabel(self, text='Enter the base of the triangle')
        self.base_label.pack(pady=10)
        self.base_entry = ctk.CTkEntry(self, placeholder_text='Base')
        self.base_entry.pack(pady=10)
        self.height_entry = ctk.CTkEntry(self, placeholder_text='Height')
        self.height_label = ctk.CTkLabel(self, text='Enter the height of the triangle')
        self.height_label.pack(pady=10)
        self.height_entry.pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)

    def calculate_area(self):
        try:
            base = float(self.base_entry.get())
            height = float(self.height_entry.get())
            if base <= 0 or height <= 0:
                ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)
                return
            area = 0.5 * base * height
            ctk.CTkLabel(self, text=f'The area of the triangle is: {round(area, 4)}').pack(pady=10)
        except ValueError:
            ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

class rectangle_area(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.length_entry = ctk.CTkEntry(self, placeholder_text='Length')
        self.length_label = ctk.CTkLabel(self, text='Enter the length of the rectangle')
        self.length_label.pack(pady=10)
        self.length_entry.pack(pady=10)
        self.width_entry = ctk.CTkEntry(self, placeholder_text='Width')
        self.width_label = ctk.CTkLabel(self, text='Enter the width of the rectangle')
        self.width_label.pack(pady=10)
        self.width_entry.pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)

    def calculate_area(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            if length <= 0 or width <= 0:
                ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)
                return
            area = length * width
            ctk.CTkLabel(self, text=f'The area of the rectangle is: {round(area, 4)}').pack(pady=10)
        except ValueError:
            ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

class CircleArea(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.radius_entry = ctk.CTkEntry(self, placeholder_text='Enter radius')
        self.radius_label = ctk.CTkLabel(self, text='Enter the radius of the circle')
        self.radius_label.pack(pady=10)
        self.radius_entry.pack(pady=10)
        ctk.CTkButton(self, text='Return to Main Menu', command=self.go_back).pack(pady=10)
        ctk.CTkButton(self, text='Calculate Area', command=self.calculate_area).pack(pady=10)

    def calculate_area(self):
        try:
            radius = float(self.radius_entry.get())
            if radius <= 0:
                ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)
                return
            area = math.pi * radius ** 2
            ctk.CTkLabel(self, text=f'The area of the circle is: {round(area, 4)}').pack(pady=10)
        except ValueError:
            ctk.CTkLabel(self, text='Invalid input.').pack(pady=10)

    def go_back(self):
        for widget in window.winfo_children():
            widget.destroy()
        main_menu()

def go_to_circle_area():
    for widget in window.winfo_children():
        widget.destroy()
    CircleArea(window).pack(fill="both", expand=True)

def go_to_rectangle_area():
    for widget in window.winfo_children():
        widget.destroy()
    rectangle_area(window).pack(fill="both", expand=True)

def go_to_right_triangle_area():
    for widget in window.winfo_children():
        widget.destroy()
    right_triangle_area(window).pack(fill="both", expand=True)

def go_to_regular_triangle_area():
    for widget in window.winfo_children():
        widget.destroy()
    regular_triangle_area(window).pack(fill="both", expand=True)

main_menu()
window.mainloop()