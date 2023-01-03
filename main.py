import customtkinter as ctk


class BMI:
    def __init__(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.window = ctk.CTk()
        self.window.title('BMI Calculator')
        self.window.geometry('335x235')
        self.window.config(padx=20, pady=20)
        self.window.columnconfigure(0, weight = 1, minsize = 50)
        self.window.columnconfigure(1, weight = 1, minsize = 50)
        self.window.rowconfigure(1, weight = 1, minsize = 50)
        self.window.rowconfigure(2, weight = 1, minsize = 50)
        self.window.rowconfigure(3, weight = 1, minsize = 50)
        self.window.rowconfigure(5, weight = 1, minsize = 50)
        
        self.weight_label = ctk.CTkLabel(master=self.window, text='Weight(kg):')
        self.height_label = ctk.CTkLabel(master=self.window, text='Height(cm):')
        
        self.weight_label.grid(column=0, row=2)
        self.height_label.grid(column=0, row=1)
        
        self.weight_entry = ctk.CTkEntry(master = self.window, corner_radius=5)
        self.height_entry = ctk.CTkEntry(master=self.window, corner_radius=5)

        self.weight_entry.grid(column = 1, row = 2)
        self.height_entry.grid(column=1, row=1)

        self.submit_btn = ctk.CTkButton(master=self.window, text='Submit', command=self.calculate)
        self.submit_btn.grid(column=1, row=3)

        self.result_var = ctk.StringVar(value='')
        self.result_label = ctk.CTkLabel(master=self.window, textvariable=self.result_var, font=('Arial', 10),
                                         text_color ='white')
       
        self.result_label.grid(column=1, row=5)

        self.window.mainloop()

    def calculate(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
  
        bmi = weight / (height ** 2)
        bmi = round(bmi, 1)

        if 18.5 > bmi:
            self.result_var.set(f'Your BMI:{bmi}\nYour Rank: Underweight, \nYou need to gain weight')

        elif 24.9 >= bmi >= 18.5:
            self.result_var.set(f'Your BMI:{bmi}\nYour Rank: Normal, \nYou are ok!')

        elif 29.9 >= bmi >= 25:
            self.result_var.set(f'Your BMI:{bmi}\nYour Rank: Overweight, \nYou need to lose weight slightly')

        elif 34.9 >= bmi >= 30:
            self.result_var.set(f'Your BMI:{bmi}\nYour Rank: Obese, \nYou should lose weight')

        elif bmi > 35:
            self.result_var.set(f'Your BMI:{bmi}\nYour Rank: Extreme Obese, \nYou should lose weight heavy')


if __name__ == '__main__':
    BMI()
