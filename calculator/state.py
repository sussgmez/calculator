import reflex as rx
from scipy.stats import binom 

class State(rx.State):
    binomial_display: str

    def show_binomial(self):
        if self.binomial_display == 'none': self.binomial_display = 'block'
        else: self.binomial_display = 'none'


class BinomialFormState(rx.State):
    """
        result1: x=x
        result2: x>x
        result3: x<x
        result4: x>=x
        result5: x<=x
        result6: x<x<x
        result7: x<=x<=x
    """
    form_data: dict = {}
    result: float

    result1: float
    result2: float
    result3: float
    result4: float
    result5: float
    result6: float
    result7: float

    min: int
    max: int
    
    data = []
    bar_color:str

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        x = int(self.form_data['x'])
        n = int(self.form_data['n'])
        p = float(self.form_data['p'])

        self.min = 0
        if self.form_data['min'] != '': self.min = int(self.form_data['min'])
        self.max = n + 1 
        if self.form_data['max'] != '': self.max = int(self.form_data['max'])
        
        print(self.max)
        
        self.result1 = str( '%.5f' % binom.pmf(x, n, p))

        self.result2 = 0
        for i in range(x + 1, n + 1): self.result2 += binom.pmf(i, n, p)
        self.result2 = str( '%.5f' % self.result2)

        self.result3 = 0
        for i in range(0, x): self.result3 += binom.pmf(i, n, p)
        self.result3 = str( '%.5f' % self.result3)

        self.result4 = 0
        for i in range(x, n + 1): self.result4 += binom.pmf(i, n, p)
        self.result4 = str( '%.5f' % self.result4)

        self.result5 = 0
        for i in range(0, x + 1): self.result5 += binom.pmf(i, n, p)
        self.result5 = str( '%.5f' % self.result5)

        self.result6 = 0
        self.result7 = 0

        for i in range(self.min, self.max): self.result6 += binom.pmf(i, n, p)
        self.result6 = str( '%.5f' % self.result6)
        
        for i in range(self.min, self.max + 1): self.result7 += binom.pmf(i, n, p)
        self.result7 = str( '%.5f' % self.result7)

        r_values = range(0, n + 1)

        self.data = []

        for r in r_values:
            d = {'name':r, 'vl':binom.pmf(r, n, p)}
            self.data.append(d)



