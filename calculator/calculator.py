import reflex as rx

from calculator.style import style
from calculator.state import MainState, BinomialState, PoissonState, HypergeometricState, NormalState

def selector() -> rx.Component:
    return rx.box(
        rx.text('Seleccione una distribución', class_name='p-btns'),
        rx.box(
            rx.button('Binomial', class_name='btn-selector', on_click=lambda: [MainState.change_distribution(1), BinomialState.set_null()]),
            rx.button('De Poisson', class_name='btn-selector', on_click=lambda: [MainState.change_distribution(2), PoissonState.set_null()]),
            rx.button('Hipergeométrica', class_name='btn-selector', on_click=lambda: [MainState.change_distribution(3), HypergeometricState.set_null()]),
            rx.button('Normal', class_name='btn-selector', on_click=lambda: [MainState.change_distribution(4), NormalState.set_null()]),
            class_name='btns-selector'
        ),
        class_name='selector'
    )

def binomial() -> rx.Component:
    return rx.box(
        rx.heading('Distribucion Binomial', class_name='h-distribution'),
        rx.text('Ingrese los datos', class_name='p-distribution'),
        rx.form(
            rx.box(
                rx.box(
                    rx.text('n', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='n', required=True, custom_attrs={'min':1}),
                    class_name='box-input',
                ),
                rx.box(
                    rx.text('p', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='p', required=True, custom_attrs={'step':'0.001', 'max':1, 'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('x', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x', required=True, custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xᵢ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x1', custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xⱼ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x2', custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.button('Calcular'),
                class_name='inputs-distribution'
            ),
            on_submit=BinomialState.handle_submit,
        ),
        rx.cond(BinomialState.error_message != "", rx.text(BinomialState.error_message, class_name='p-error')),
        rx.text('Resultados', class_name='p-distribution'),
        rx.box(
            rx.box(
                rx.text(rx.cond(BinomialState.x > 0, 'P({})'.format(BinomialState.x), 'P(x)'), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=BinomialState.d1),
                class_name='box-result',
            ),
            rx.separator(style={'width':'100%'}),
            rx.box(
                rx.text('P(x > {})'.format(BinomialState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=BinomialState.d2),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x < {})'.format(BinomialState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=BinomialState.d3),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x ≥ {})'.format(BinomialState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=BinomialState.d4),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x ≤ {})'.format(BinomialState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=BinomialState.d5),
                class_name='box-result'
            ),
            rx.cond(
                BinomialState.show_x1_x2,
                rx.box(
                    rx.text('P({} < x < {})'.format(BinomialState.x1, BinomialState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=BinomialState.d6),
                    class_name='box-result'
                ),
            ),
            rx.cond(
                BinomialState.show_x1_x2,
                rx.box(
                    rx.text('P({} ≤ x ≤ {})'.format(BinomialState.x1, BinomialState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=BinomialState.d7),
                    class_name='box-result'
                ),
            ),
            class_name='results-distribution'
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key='p', fill='#82ca9d'
            ),
            rx.recharts.x_axis(data_key='x'),
            rx.recharts.y_axis(),
            data=BinomialState.chart_data,
            height=400,
            class_name='chart'
        ),
    )

def poisson() -> rx.Component:
    return rx.box(
        rx.heading('Distribucion De Poisson', class_name='h-distribution'),
        rx.text('Ingrese los datos', class_name='p-distribution'),
        rx.form(
            rx.box(
                rx.box(
                    rx.text('λ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='l', required=True, custom_attrs={'min':1, 'step':'0.001'}),
                    class_name='box-input',
                ),
                rx.box(
                    rx.text('x', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x', required=True, custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xᵢ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x1', custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xⱼ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x2', custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.button('Calcular'),
                class_name='inputs-distribution'
            ),
            on_submit=PoissonState.handle_submit,
        ),
        rx.cond(PoissonState.error_message != "", rx.text(PoissonState.error_message, class_name='p-error')),
        rx.text('Resultados', class_name='p-distribution'),
        rx.box(
            rx.box(
                rx.text(rx.cond(PoissonState.x > 0, 'P({})'.format(PoissonState.x), 'P(x)'), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=PoissonState.d1),
                class_name='box-result',
            ),
            rx.separator(style={'width':'100%'}),
            rx.box(
                rx.text('P(x > {})'.format(PoissonState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=PoissonState.d2),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x < {})'.format(PoissonState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=PoissonState.d3),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x ≥ {})'.format(PoissonState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=PoissonState.d4),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x ≤ {})'.format(PoissonState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=PoissonState.d5),
                class_name='box-result'
            ),
            rx.cond(
                PoissonState.show_x1_x2,
                rx.box(
                    rx.text('P({} < x < {})'.format(PoissonState.x1, PoissonState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=PoissonState.d6),
                    class_name='box-result'
                ),
            ),
            rx.cond(
                PoissonState.show_x1_x2,
                rx.box(
                    rx.text('P({} ≤ x ≤ {})'.format(PoissonState.x1, PoissonState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=PoissonState.d7),
                    class_name='box-result'
                ),
            ),
            class_name='results-distribution'
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key='p', fill='#82ca9d'
            ),
            rx.recharts.x_axis(data_key='x'),
            rx.recharts.y_axis(),
            data=PoissonState.chart_data,
            height=400,
            class_name='chart'
        ),
    )

def hypergeometric() -> rx.Component:
    return rx.box(
        rx.heading('Distribucion Hipergeométrica', class_name='h-distribution'),
        rx.text('Ingrese los datos', class_name='p-distribution'),
        rx.form(
            rx.box(
                rx.box(
                    rx.text('n', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='n', required=True, custom_attrs={'min':1}),
                    class_name='box-input',
                ),
                rx.box(
                    rx.text('N', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='N', required=True, custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('M', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='M', required=True, custom_attrs={'min':1}),
                    class_name='box-input',
                ),
                rx.box(
                    rx.text('x', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x', required=True, custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xᵢ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x1', custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xⱼ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x2', custom_attrs={'min':0}),
                    class_name='box-input'
                ),
                rx.button('Calcular'),
                class_name='inputs-distribution'
            ),
            on_submit=HypergeometricState.handle_submit,
        ),
        rx.cond(HypergeometricState.error_message != "", rx.text(HypergeometricState.error_message, class_name='p-error')),
        rx.text('Resultados', class_name='p-distribution'),
        rx.box(
            rx.box(
                rx.text(rx.cond(HypergeometricState.x > 0, 'P({})'.format(HypergeometricState.x), 'P(x)'), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=HypergeometricState.d1),
                class_name='box-result',
            ),
            rx.separator(style={'width':'100%'}),
            rx.box(
                rx.text('P(x > {})'.format(HypergeometricState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=HypergeometricState.d2),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x < {})'.format(HypergeometricState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=HypergeometricState.d3),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x ≥ {})'.format(HypergeometricState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=HypergeometricState.d4),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x ≤ {})'.format(HypergeometricState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=HypergeometricState.d5),
                class_name='box-result'
            ),
            rx.cond(
                HypergeometricState.show_x1_x2,
                rx.box(
                    rx.text('P({} < x < {})'.format(HypergeometricState.x1, HypergeometricState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=HypergeometricState.d6),
                    class_name='box-result'
                ),
            ),
            rx.cond(
                HypergeometricState.show_x1_x2,
                rx.box(
                    rx.text('P({} ≤ x ≤ {})'.format(HypergeometricState.x1, HypergeometricState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=HypergeometricState.d7),
                    class_name='box-result'
                ),
            ),
            class_name='results-distribution'
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key='p', fill='#82ca9d'
            ),
            rx.recharts.x_axis(data_key='x'),
            rx.recharts.y_axis(),
            data=HypergeometricState.chart_data,
            height=400,
            class_name='chart'
        ),
    )

def normal() -> rx.Component:
    return rx.box(
        rx.heading('Distribucion Normal', class_name='h-distribution'),
        rx.text('Ingrese los datos', class_name='p-distribution'),
        rx.form(
            rx.box(
                rx.box(
                    rx.text('µ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='m', required=True, custom_attrs={'step':'0.001'}),
                    class_name='box-input',
                ),
                rx.box(
                    rx.text('σ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='d', required=True, custom_attrs={'step':'0.001'}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('x', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x', required=True, custom_attrs={'step':'0.001'}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xᵢ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x1', custom_attrs={'step':'0.001'}),
                    class_name='box-input'
                ),
                rx.box(
                    rx.text('xⱼ', class_name='l-input'),
                    rx.input(class_name='input', type='number', name='x2', custom_attrs={'step':'0.001'}),
                    class_name='box-input'
                ),
                rx.button('Calcular'),
                class_name='inputs-distribution'
            ),
            on_submit=NormalState.handle_submit,
        ),
        rx.cond(NormalState.error_message != "", rx.text(NormalState.error_message, class_name='p-error')),
        rx.text('Resultados', class_name='p-distribution'),
        rx.box(
            rx.box(
                rx.text('P(x > {})'.format(NormalState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=NormalState.d2),
                class_name='box-result'
            ),
            rx.box(
                rx.text('P(x < {})'.format(NormalState.x), class_name='l-result'),
                rx.input(class_name='result', read_only=True, value=NormalState.d3),
                class_name='box-result'
            ),
            rx.cond(
                NormalState.show_x1_x2,
                rx.box(
                    rx.text('P({} < x < {})'.format(NormalState.x1, NormalState.x2), class_name='l-result'),
                    rx.input(class_name='result', read_only=True, value=NormalState.d6),
                    class_name='box-result'
                ),
            ),
            class_name='results-distribution'
        ),
    )

def calculator() -> rx.Component:
    return rx.container(
        rx.heading('Calculadora de probabilidades', class_name='h-calculator'),
        selector(),
        rx.cond(MainState.selected_distribution == 1, binomial()),
        rx.cond(MainState.selected_distribution == 2, poisson()),
        rx.cond(MainState.selected_distribution == 3, hypergeometric()),
        rx.cond(MainState.selected_distribution == 4, normal()),
    )

app = rx.App(
    style=style
)
app.add_page(calculator)

