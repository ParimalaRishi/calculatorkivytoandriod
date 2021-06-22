from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Size of app
Window.size = (500,700)

# .kv design file
Builder.load_file('calc.kv')

class MyLayout(Widget):   
    def clear(self):
        self.ids.calc_input.text='0'

    # create a button pressing function

    def button_press(self, button):
        # create a variable that contains whatever was in the text box already 
        prior = self.ids.calc_input.text

        # test case
        if "Error" in prior:
            prior =''

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text= ''
            self.ids.calc_input.text= f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'

    # Remove functions
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior [:-1]
        self.ids.calc_input.text = prior
    
    # pos function
    def pos_negative(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'


    # decimal functions
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior


        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # add decimal to function
        prior = f'{prior}.'
    # math function
    def math_sign(self, sign):
        # create a variable that contains whatever was in the text box already 
        prior = self.ids.calc_input.text
        self.ids.calc_input.text=f'{prior}{sign}'

    # equals to function
    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
            
        '''
        # Add
        if "+" in prior:
            num_list = prior.split("+")
            print(num_list)
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)
            self.ids.calc_input.text = str(answer)
        '''
            





class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()