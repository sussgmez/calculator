import reflex as rx
from scipy.stats import binom, poisson, hypergeom, norm


class MainState(rx.State):
    # Distribución seleccionada
    selected_distribution: int
    
    def change_distribution(self, i):
        # Cambiar distribución seleccionada
        self.selected_distribution = i


class BinomialState(rx.State):
    # Valores iniciales para la distribución binomial.
    
    data: dict = {} # Entradas

    chart_data: list # Datos para la gráfica

    # Valores para calcular la distribución
    n: int
    p: float
    x: int

    x1: int # xi
    x2: int # xj

    show_x1_x2: bool

    error_message: str

    d1 = ""
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d6 = ""
    d7 = ""

    def handle_submit(self, data: dict):
        self.data = data

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

        self.show_x1_x2 = False

        self.chart_data = []

        if int(self.data['x']) <= int(self.data['n']):
            self.error_message = ''

            self.n = int(self.data['n'])
            self.p = float(self.data['p'])
            self.x = int(self.data['x'])

            # Valor puntual
            self.d1 = str( '%.5f' % binom.pmf(self.x, self.n, self.p))

            # Mayor
            self.d2 = str( '%.5f' % (1 - binom.cdf(self.x, self.n, self.p)))
            
            # Menor
            self.d3 = str( '%.5f' % (binom.cdf(self.x - 1, self.n, self.p)))
            
            # Mayor o igual
            self.d4 = str( '%.5f' % (1 - binom.cdf(self.x - 1, self.n, self.p)))
            
            # Menor o igual
            self.d5 = str( '%.5f' % (binom.cdf(self.x, self.n, self.p)))

            # Dado xi y xj
            if self.data['x1'] != '' and self.data['x2'] != '':

                self.x1 = int(self.data['x1']) 
                self.x2 = int(self.data['x2'])

                if self.x1 <= self.x and self.x1 >= 0:
                    if self.x2 >= self.x and  self.x2 <= self.n:
                        
                        # xi < x < xj
                        self.d6 = str('%.5f' % (binom.cdf(self.x2 - 1, self.n, self.p) - binom.cdf(self.x1, self.n, self.p)))

                        # xi ≤ x ≤ xj
                        self.d7 = str('%.5f' % (binom.cdf(self.x2, self.n, self.p) - binom.cdf(self.x1 - 1, self.n, self.p)))

                        self.show_x1_x2 = True

                    else: self.error_message = 'El valor de xⱼ debe estar entre ({}, {})'.format(self.x, self.n)
                else: self.error_message = 'El valor de xᵢ debe estar entre (0, {})'.format(self.x)

            # Gráfica
            i = int(self.n * self.p)
            while binom.pmf(i, self.n, self.p) > 0.000001: i -= 1
            i += 1

            while binom.pmf(i, self.n, self.p) > 0.000001:
                d = {'x':i, 'p':binom.pmf(i, self.n, self.p)}
                self.chart_data.append(d)
                i += 1


        else: self.error_message = 'El valor de x debe ser menor o igual que n.'

    def set_null(self): self.reset()


class PoissonState(rx.State):
    # Valores iniciales para la distribución de Poisson.
    
    data: dict = {} # Entradas

    chart_data: list # Datos para la gráfica

    # Valores para calcular la distribución
    l: int
    x: int
    x1: int # xi
    x2: int # xj

    show_x1_x2: bool

    error_message: str

    d1 = ""
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d6 = ""
    d7 = ""

    def handle_submit(self, data: dict):
        self.data = data

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

        # Valor puntual
        self.d1 = str( '%.5f' % poisson.pmf(self.x, self.l))

        # Mayor
        self.d2 = str( '%.5f' % (1 - poisson.cdf(self.x, self.l)))

        # Menor
        self.d3 = str( '%.5f' % (poisson.cdf(self.x - 1, self.l)))

        # Mayor o igual
        self.d4 = str( '%.5f' % (1 - poisson.cdf(self.x - 1, self.l)))

        # Menor o igual
        self.d5 = str( '%.5f' % (poisson.cdf(self.x, self.l)))

        # Dado xi y xj
        if self.data['x1'] != '' and self.data['x2'] != '':
            self.x1 = int(self.data['x1']) 
            self.x2 = int(self.data['x2'])

            if self.x1 <= self.x and self.x1 >= 0:
                if self.x2 >= self.x:
                    
                    # xi < x < xj
                    self.d6 = str('%.5f' % (poisson.cdf(self.x2 - 1, self.l) - poisson.cdf(self.x1, self.l)))

                    # xi ≤ x ≤ xj
                    self.d7 = str('%.5f' % (poisson.cdf(self.x2, self.l) - poisson.cdf(self.x1 - 1, self.l)))

                    self.show_x1_x2 = True
                else: self.error_message = 'El valor de xⱼ debe ser mayor o igual que {}'.format(self.x)
            else: self.error_message = 'El valor de xᵢ debe estar entre (0, {})'.format(self.x)

        # Gráfica
        self.chart_data = []

        i = self.l
        while poisson.pmf(i, self.l) > 0.000001: i -= 1
        i += 1

        while poisson.pmf(i, self.l) > 0.000001:
            d = {'x':i, 'p':poisson.pmf(i, self.l)}
            self.chart_data.append(d)
            i += 1

    def set_null(self): self.reset()        


class HypergeometricState(rx.State):
    # Valores iniciales para la distribución hipergeométrica.
    data: dict = {} # Entradas

    chart_data: list # Datos para la gráfica

    # Valores para calcular la distribución
    n: int
    N: int
    M: int
    x: int
    x1: int # xi
    x2: int # xj

    show_x1_x2: bool

    error_message: str
    
    d1 = ""
    d2 = ""
    d3 = ""
    d4 = ""
    d5 = ""
    d6 = ""
    d7 = ""

    def handle_submit(self, data: dict):
        self.data = data

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
        
        self.chart_data = [] 

        if self.n <= self.N and self.M <= self.N:

            # Valor puntual
            self.d1 = str( '%.5f' % hypergeom.pmf(self.x, self.N, self.M, self.n)) 
            
            # Mayor
            self.d2 = str( '%.5f' % (1 - hypergeom.cdf(self.x, self.N, self.M, self.n)))
            
            # Menor
            self.d3 = str( '%.5f' % (hypergeom.cdf(self.x - 1, self.N, self.M, self.n)))
            
            # Mayor o igual
            self.d4 = str( '%.5f' % (1 - hypergeom.cdf(self.x - 1, self.N, self.M, self.n)))
            
            # Menor o igual
            self.d5 = str( '%.5f' % (hypergeom.cdf(self.x, self.N, self.M, self.n)))
            
            # Dado xi y xj
            if self.data['x1'] != '' and self.data['x2'] != '':
                self.x1 = int(self.data['x1']) 
                self.x2 = int(self.data['x2'])

                if self.x1 <= self.x and self.x1 >= 0:
                    if self.x2 >= self.x:

                        # xi < x < xj
                        self.d6 = str('%.5f' % (hypergeom.cdf(self.x2 - 1, self.N, self.M, self.n) - hypergeom.cdf(self.x1, self.N, self.M, self.n)))
                               
                        # xi ≤ x ≤ xj
                        self.d7 = str('%.5f' % (hypergeom.cdf(self.x2, self.N, self.M, self.n) - hypergeom.cdf(self.x1 - 1, self.N, self.M, self.n)))

                        self.show_x1_x2 = True
                    else: self.error_message = 'El valor de xⱼ debe ser mayor o igual que {}'.format(self.x)
                else: self.error_message = 'El valor de xᵢ debe estar entre (0, {})'.format(self.x)

            i = int(hypergeom.mean(self.N, self.M, self.n))
            while hypergeom.pmf(i, self.N, self.M, self.n) > 0.000001: i -= 1
            i += 1

            while hypergeom.pmf(i, self.N, self.M, self.n) > 0.000001:

                d = {'x':i, 'p': hypergeom.pmf(i, self.N, self.M, self.n)}
                self.chart_data.append(d)

                i += 1

        else: self.error_message = 'El valor de n y el valor M deben estar entre (0, {})'.format(self.N)

    def set_null(self): self.reset()
 
 
class NormalState(rx.State):
    # Valores iniciales para la distribución Normal.

    data: dict = {} # Entradas

    chart_data: list # Datos para la gráfica

    # Valores para calcular la distribución
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

        # Mayor
        self.d2 = str('%.5f' % (1 - norm.cdf(self.x, self.m, self.d)))
        
        # Menor
        self.d3 = str('%.5f' % norm.cdf(self.x, self.m, self.d))

        # Dado xi y xj
        if self.data['x1'] != '' and self.data['x2'] != '':

            self.x1 = float(self.data['x1']) 
            self.x2 = float(self.data['x2'])
            
            if self.x1 <= self.x:
                if self.x2 >= self.x:

                    self.d6 = str('%.5f' % (norm.cdf(self.x2, self.m, self.d) - norm.cdf(self.x1, self.m, self.d)))

                    self.show_x1_x2 = True
                else: self.error_message = 'El valor de xⱼ debe ser mayor o igual que {}'.format(self.x)
            else: self.error_message = 'El valor de xᵢ debe ser menor o igual que {}'.format(self.x)

        self.chart_data = [] 
        for i in range(-8, 9):
            d = {'x':str('%.2f' % (self.m+self.d*i/2)), 'p': norm.pdf(self.m+self.d*i, self.m, self.d)}
            self.chart_data.append(d)

    def set_null(self): self.reset()
        