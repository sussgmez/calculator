import reflex as rx
import numpy as np
from scipy.stats import binom, poisson, hypergeom, norm


class MainState(rx.State):
    selected_distribution: int

    def change_distribution(self, i): self.selected_distribution = i


class BinomialState(rx.State):
    data: dict = {}
    chart_data: list

    n: int
    p: float
    x: int
    x1: int
    x2: int

    show_x1_x2: bool

    error_message: str

    d1: float
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d6 = ""
    d7 = ""

    def handle_submit(self, data: dict):
        self.data = data
        self.chart_data = []

        self.show_x1_x2 = False

        self.n = 0
        self.p = 0
        self.x = 0

        self.d1 = 0

        self.d2 = 0
        self.d3 = 0

        self.d4 = 0
        self.d5 = 0

        self.d6 = 0
        self.d7 = 0

        if int(self.data['x']) <= int(self.data['n']):
            self.error_message = ''

            self.n = int(self.data['n'])
            self.p = float(self.data['p'])
            self.x = int(self.data['x'])

            self.d1 = str( '%.5f' % binom.pmf(self.x, self.n, self.p))

            i = int(self.n * self.p)
            while binom.pmf(i, self.n, self.p) > 0.000001: i -= 1
            i += 1

            while binom.pmf(i, self.n, self.p) > 0.000001:
                if i >= self.x + 1: self.d2 += binom.pmf(i, self.n, self.p)
                if i <= self.x - 1: self.d3 += binom.pmf(i, self.n, self.p)
                if i >= self.x: self.d4 += binom.pmf(i, self.n, self.p)
                if i <= self.x: self.d5 += binom.pmf(i, self.n, self.p)

                d = {'x':i, 'p':binom.pmf(i, self.n, self.p)}
                self.chart_data.append(d)

                i += 1

            self.d2 = str( '%.5f' % self.d2)
            self.d3 = str( '%.5f' % self.d3)
            self.d4 = str( '%.5f' % self.d4)
            self.d5 = str( '%.5f' % self.d5)


            if self.data['x1'] != '' and self.data['x2'] != '':

                self.x1 = int(self.data['x1']) 
                self.x2 = int(self.data['x2'])

                if self.x1 <= self.x and self.x1 >= 0:
                    if self.x2 >= self.x and  self.x2 <= self.n:
                        for i in range(self.x1 + 1, self.x2): self.d6 += binom.pmf(i, self.n, self.p)
                        self.d6 = str( '%.5f' % self.d6)

                        for i in range(self.x1, self.x2 + 1): self.d7 += binom.pmf(i, self.n, self.p)
                        self.d7 = str( '%.5f' % self.d7)

                        self.show_x1_x2 = True
                    else: self.error_message = 'El valor de xⱼ debe estar entre ({}, {})'.format(self.x, self.n)
                else: self.error_message = 'El valor de xᵢ debe estar entre (0, {})'.format(self.x)

                    
        else: self.error_message = 'El valor de x debe ser menor o igual que n.'

    def set_null(self): self.reset()
    

class PoissonState(rx.State):
    data: dict = {}
    chart_data = []

    l: int
    x: int
    x1: int
    x2: int

    show_x1_x2: bool

    error_message: str

    d1: float
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d6 = ""
    d7 = ""

    def handle_submit(self, data: dict):
        self.data = data
        self.chart_data = []

        self.show_x1_x2 = False

        self.l = 0
        self.x = 0

        self.d1 = 0

        self.d2 = 0
        self.d3 = 0

        self.d4 = 0
        self.d5 = 0

        self.d6 = 0
        self.d7 = 0

        self.error_message = ''

        self.l = float(self.data['l'])
        self.x = int(self.data['x'])

        self.d1 = str( '%.5f' % poisson.pmf(self.x, self.l))
        
        i = self.l
        while poisson.pmf(i, self.l) > 0.000001: i -= 1
        i += 1

        while poisson.pmf(i, self.l) > 0.000001:
            if i >= self.x + 1: self.d2 += poisson.pmf(i, self.l)
            if i <= self.x - 1: self.d3 += poisson.pmf(i, self.l)
            if i >= self.x: self.d4 += poisson.pmf(i, self.l)
            if i <= self.x: self.d5 += poisson.pmf(i, self.l)

            d = {'x':i, 'p':poisson.pmf(i, self.l)}
            self.chart_data.append(d)

            i += 1

        self.d2 = str( '%.5f' % self.d2)
        self.d3 = str( '%.5f' % self.d3)
        self.d4 = str( '%.5f' % self.d4)
        self.d5 = str( '%.5f' % self.d5)


        if self.data['x1'] != '' and self.data['x2'] != '':
            self.x1 = int(self.data['x1']) 
            self.x2 = int(self.data['x2'])

            if self.x1 <= self.x and self.x1 >= 0:
                if self.x2 >= self.x:
                    for i in range(self.x1 + 1, self.x2): self.d6 += poisson.pmf(i, self.l)
                    self.d6 = str( '%.5f' % self.d6)
                    
                    for i in range(self.x1, self.x2 + 1): self.d7 += poisson.pmf(i, self.l)
                    self.d7 = str( '%.5f' % self.d7)

                    self.show_x1_x2 = True
                else: self.error_message = 'El valor de xⱼ debe ser mayor o igual que {}'.format(self.x)
            else: self.error_message = 'El valor de xᵢ debe estar entre (0, {})'.format(self.x)

    def set_null(self): self.reset()        


class HypergeometricState(rx.State):
    data: dict = {}
    chart_data = []

    n: int
    N: int
    M: int
    x: int
    x1: int
    x2: int

    show_x1_x2: bool

    error_message: str

    d1: float
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d6 = ""
    d7 = ""

    def handle_submit(self, data: dict):
        self.data = data
        self.chart_data = [] 

        self.show_x1_x2 = False

        self.d1 = 0

        self.d2 = 0
        self.d3 = 0

        self.d4 = 0
        self.d5 = 0

        self.d6 = 0
        self.d7 = 0

        self.error_message = ''

        self.n = int(self.data['n'])
        self.N = int(self.data['N'])
        self.M = int(self.data['M'])
        self.x = int(self.data['x'])
        
        if self.n <= self.N and self.M <= self.N:

            self.d1 = str( '%.5f' % hypergeom.pmf(self.x, self.N, self.M, self.n)) 

            i = int(hypergeom.mean(self.N, self.M, self.n))
            while hypergeom.pmf(i, self.N, self.M, self.n) > 0.000001: i -= 1
            i += 1

            while hypergeom.pmf(i, self.N, self.M, self.n) > 0.000001:
                if i >= self.x + 1: self.d2 += hypergeom.pmf(i, self.N, self.M, self.n)
                if i <= self.x - 1: self.d3 += hypergeom.pmf(i, self.N, self.M, self.n)
                if i >= self.x: self.d4 += hypergeom.pmf(i, self.N, self.M, self.n)
                if i <= self.x: self.d5 += hypergeom.pmf(i, self.N, self.M, self.n)

                d = {'x':i, 'p': hypergeom.pmf(i, self.N, self.M, self.n)}
                self.chart_data.append(d)

                i += 1

            self.d2 = str( '%.5f' % self.d2)
            self.d3 = str( '%.5f' % self.d3)
            self.d4 = str( '%.5f' % self.d4)
            self.d5 = str( '%.5f' % self.d5)


            if self.data['x1'] != '' and self.data['x2'] != '':
                self.x1 = int(self.data['x1']) 
                self.x2 = int(self.data['x2'])

                if self.x1 <= self.x and self.x1 >= 0:
                    if self.x2 >= self.x:
                        for i in range(self.x1 + 1, self.x2): self.d6 += hypergeom.pmf(i, self.N, self.M, self.n)
                        self.d6 = str( '%.5f' % self.d6)
                        
                        for i in range(self.x1, self.x2 + 1): self.d7 += hypergeom.pmf(i, self.N, self.M, self.n)
                        self.d7 = str( '%.5f' % self.d7)

                        self.show_x1_x2 = True
                    else: self.error_message = 'El valor de xⱼ debe ser mayor o igual que {}'.format(self.x)
                else: self.error_message = 'El valor de xᵢ debe estar entre (0, {})'.format(self.x)

        else: self.error_message = 'El valor de n y el valor M deben estar entre (0, {})'.format(self.N)

    def set_null(self): self.reset()
 
 
class NormalState(rx.State):
    """
    P(X>xi)
    P(X<xi)
    P(xi<x<xj)
    """

    data: dict = {}

    m: float
    d: float
    x: float
    x1: float
    x2: float

    show_x1_x2: bool

    error_message: str

    d2 = ""
    d3 = ""
    d6 = ""

    def handle_submit(self, data: dict):
        self.data = data

        self.show_x1_x2 = False

        self.m = 0
        self.d = 0
        self.x = 0
        self.x1 = 0
        self.x2 = 0

        self.d2 = 0
        self.d3 = 0

        self.d6 = 0

        self.error_message = ''

        self.m = float(self.data['m'])
        self.d = float(self.data['d'])
        self.x = float(self.data['x'])

        self.d2 = str('%.5f' % (1 - norm.cdf(self.x, self.m, self.d)))
        self.d3 = str('%.5f' % norm.cdf(self.x, self.m, self.d))

        self.d6 = str('%.5f' % (norm.cdf(self.x, self.m, self.d)))
        
        if self.data['x1'] != '' and self.data['x2'] != '':

            self.x1 = float(self.data['x1']) 
            self.x2 = float(self.data['x2'])
            
            if self.x1 <= self.x:
                if self.x2 >= self.x:

                    self.d6 = str('%.5f' % (norm.cdf(self.x2, self.m, self.d) - norm.cdf(self.x1, self.m, self.d)))

                    self.show_x1_x2 = True
                else: self.error_message = 'El valor de xⱼ debe ser mayor o igual que {}'.format(self.x)
            else: self.error_message = 'El valor de xᵢ debe ser menor o igual que {}'.format(self.x)



    def set_null(self): self.reset()
        