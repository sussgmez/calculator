import reflex as rx
from scipy.stats import binom, poisson 
from math import sqrt

class State(rx.State):
    binomial_display = 'none'
    poisson_display = 'none'
    hypergeometric_display = 'none'

    def show_binomial(self):
        self.binomial_display = 'block'
        self.poisson_display = 'none'
        self.hypergeometric_display = 'none'
        
        
    def show_poisson(self):
        self.binomial_display = 'none'
        self.poisson_display = 'block'
        self.hypergeometric_display = 'none'
    
    def show_hypergeometric(self):
        self.binomial_display = 'none'
        self.poisson_display = 'none'
        self.hypergeometric_display = 'block'
    
    

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

    result1: float
    result2: float
    result3: float
    result4: float
    result5: float
    result6: float
    result7: float

    m: int
    x2: int
    
    data = []
    bar_color:str

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        x = int(self.form_data['x'])
        n = int(self.form_data['n'])
        p = float(self.form_data['p'])

        self.result1 = 0
        self.result2 = 0
        self.result3 = 0
        self.result4 = 0
        self.result5 = 0
        self.result6 = 0
        self.result7 = 0

        if x <= n:
            self.result1 = str( '%.5f' % binom.pmf(x, n, p))

            self.x1 = int(n/(1/p)-sqrt(n/(1/p))*2)
            #self.x1 = 0
            if self.form_data['x1'] != '': self.x1 = int(self.form_data['x1'])
            if self.x1<0: self.x1 = 0

            self.x2 = int(n/(1/p)+sqrt(n/(1/p))*2)
            #self.x2 = n + 1 
            if self.form_data['x2'] != '': self.x2 = int(self.form_data['x2'])
            if self.x2>n: self.x2 = n + 1

            for i in range(x + 1, n + 1): self.result2 += binom.pmf(i, n, p)
            self.result2 = str( '%.5f' % self.result2)

            for i in range(0, x): self.result3 += binom.pmf(i, n, p)
            self.result3 = str( '%.5f' % self.result3)

            for i in range(x, n + 1): self.result4 += binom.pmf(i, n, p)
            self.result4 = str( '%.5f' % self.result4)

            for i in range(0, x + 1): self.result5 += binom.pmf(i, n, p)
            self.result5 = str( '%.5f' % self.result5)

            for i in range(self.m, self.x2): self.result6 += binom.pmf(i, n, p)
            self.result6 = str( '%.5f' % self.result6)
            
            for i in range(self.m, self.x2 + 1): self.result7 += binom.pmf(i, n, p)
            self.result7 = str( '%.5f' % self.result7)

            r_values = range(self.x1, self.x2)
            
            self.data = []

            for r in r_values:
                d = {'name':r, 'vl':binom.pmf(r, n, p)}
                self.data.append(d)


class PoissonFormState(rx.State):
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

    result1: float
    result2: float
    result3: float
    result4: float
    result5: float
    result6: float
    result7: float

    m: int
    x2: int
    
    data = []
    bar_color:str

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        x = int(self.form_data['x'])
        p = float(self.form_data['p'])

        self.result1 = 0
        self.result2 = 0
        self.result3 = 0
        self.result4 = 0
        self.result5 = 0
        self.result6 = 0
        self.result7 = 0

        self.result1 = str( '%.5f' % poisson.pmf(x, p))

        self.x1 = int(p-sqrt(p)*6)
        if self.form_data['x1'] != '': self.x1 = int(self.form_data['x1'])
        if self.x1<0: self.x1 = 0

        self.x2 = int(p+sqrt(p)*6)
        if self.form_data['x2'] != '': self.x2 = int(self.form_data['x2'])

        for i in range(x + 1, x*2): self.result2 += poisson.pmf(i, p)
        self.result2 = str( '%.5f' % self.result2)

        for i in range(0, x): self.result3 += poisson.pmf(i, p)
        self.result3 = str( '%.5f' % self.result3)

        for i in range(x, x*2): self.result4 += poisson.pmf(i, p)
        self.result4 = str( '%.5f' % self.result4)

        for i in range(0, x + 1): self.result5 += poisson.pmf(i, p)
        self.result5 = str( '%.5f' % self.result5)

        for i in range(self.x1, self.x2 + 1): self.result6 += poisson.pmf(i, p)
        self.result6 = str( '%.5f' % self.result6)
        
        for i in range(self.x1, self.x2): self.result7 += poisson.pmf(i, p)
        self.result7 = str( '%.5f' % self.result7)

        r_values = range(self.x1, self.x2)

        self.data = []

        for r in r_values:
            d = {'name':r, 'vl':poisson.pmf(r, p)}
            self.data.append(d)

