import reflex as rx
import scipy

from calculator import style
from calculator.state import State, BinomialFormState, PoissonFormState


def select_calculator() -> rx.Component:
    return rx.box(
        rx.button('Distribucion Binomial', style=style.button_style, on_click=State.show_binomial),
        rx.button('Distribucion De Poisson', style=style.button_style, on_click=State.show_poisson),
        rx.button('Distribucion Hipergeometrica', style=style.button_style, on_click=State.show_hypergeometric),
        rx.button('Distribucion Normal', style=style.button_style),
        style=dict(
            display='flex', 
            gap='4px', 
            width='fit-content', 
            max_width='540px',
            flex_wrap='wrap',
            margin='auto',
            margin_bottom='24px'
        )
    )

def binomial() -> rx.Component:
    return rx.box(
        rx.form(
            rx.box(
                rx.text('n', text_align='center'),
                rx.input(placeholder='n', type='number', name='n', required=True, custom_attrs={'min':1}),
                style=style.input_style | {'grid_column':'span 2'}
            ),
            rx.box(
                rx.text('p', text_align='center'),
                rx.input(placeholder='p', type='number', name='p', required=True, custom_attrs={'step':'0.001', 'max':1}), 
                style=style.input_style | {'grid_column':'span 2'}
            ),
            rx.box(
                rx.text('x', text_align='center'),
                rx.input(placeholder='x', type='number', name='x', required=True),
                style=style.input_style | {'grid_column':'span 2'}
            ),
            rx.button('Calcular',type='Submit', style=dict(grid_column='span 6')), 
            rx.box(
                rx.text('min', text_align='center'),
                rx.input(placeholder='x1', type='number', name='x1'),
                style=style.input_style | {'grid_column':'span 3'}
            ),
            rx.box(
                rx.text('max', text_align='center'),
                rx.input(placeholder='x2', type='number', name='x2'),
                style=style.input_style| {'grid_column':'span 3'}
            ),
            style=dict(
                display='grid',
                grid_template_columns='1fr 1fr 1fr 1fr 1fr 1fr',
                gap='4px',
                max_width='600px',
                margin='auto',
                margin_bottom='24px',
            ),
            on_submit=BinomialFormState.handle_submit,
        ),
        rx.box(
            rx.text('Resultados: ', font_weight=800, style=dict(grid_column='span 2')),
            rx.box(
                rx.text('P(x): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result1, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x>xi): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result2, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x<xi): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result3, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x>=xi): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result4, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x<=xi): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result5, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(style=dict(grid_column='span 2')),
            rx.box(
                rx.text('P(x1<x<x2): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result6, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x1<=x<=x2): ', font_weight=800, style=style.label_result_style),
                rx.text(BinomialFormState.result7, style=style.input_result_style),
                style=style.result_style
            ),
            style = dict(
                display='grid',
                grid_template_columns='1fr 1fr',
                gap='8px',
                justify_content='center',
                max_width='600px',
                margin='auto'
            ),
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key='vl', fill='#82ca9d'
            ),
            rx.recharts.x_axis(data_key='name'),
            rx.recharts.y_axis(),
            data=BinomialFormState.data,
            height=400,
            style=dict(
                max_width='600px',
                margin='auto'
            )
        ),
        display=State.binomial_display,
    )

def poisson() -> rx.Component:
    return rx.box(
        rx.form(
            rx.box(
                rx.text('ɣ', text_align='center'),
                rx.input(placeholder='p', type='number', name='p', required=True, custom_attrs={'min':1}), 
                style=style.input_style | {'grid_column':'span 3'}
            ),
            rx.box(
                rx.text('x', text_align='center'),
                rx.input(placeholder='x', type='number', name='x', required=True),
                style=style.input_style | {'grid_column':'span 3'}
            ),
            rx.button('Calcular',type='Submit', style=dict(grid_column='span 6')), 
            rx.box(
                rx.text('min', text_align='center'),
                rx.input(placeholder='x1', type='number', name='x1'),
                style=style.input_style | {'grid_column':'span 3'}
            ),
            rx.box(
                rx.text('max', text_align='center'),
                rx.input(placeholder='x2', type='number', name='x2'),
                style=style.input_style| {'grid_column':'span 3'}
            ),
            style=dict(
                display='grid',
                grid_template_columns='1fr 1fr 1fr 1fr 1fr 1fr',
                gap='4px',
                max_width='600px',
                margin='auto',
                margin_bottom='24px',
            ),
            on_submit=PoissonFormState.handle_submit,
        ),
        rx.box(
            rx.text('Resultados: ', font_weight=800, style=dict(grid_column='span 2')),
            rx.box(
                rx.text('P(x): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result1, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x>xi): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result2, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x<xi): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result3, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x>=xi): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result4, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x<=xi): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result5, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(style=dict(grid_column='span 2')),
            rx.box(
                rx.text('P(x1<x<x2): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result6, style=style.input_result_style),
                style=style.result_style
            ),
            rx.box(
                rx.text('P(x1<=x<=x2): ', font_weight=800, style=style.label_result_style),
                rx.text(PoissonFormState.result7, style=style.input_result_style),
                style=style.result_style
            ),
            style = dict(
                display='grid',
                grid_template_columns='1fr 1fr',
                gap='8px',
                justify_content='center',
                max_width='600px',
                margin='auto'
            ),
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key='vl', fill='#82ca9d'
            ),
            rx.recharts.x_axis(data_key='name'),
            rx.recharts.y_axis(),
            data=PoissonFormState.data,
            height=400,
            style=dict(
                max_width='600px',
                margin='auto'
            )
        ),
        display=State.poisson_display,
    )

def hypergeometric() -> rx.Component:
    return rx.box(
        rx.form(
            rx.box(
                rx.text('N', text_align='center'),
                rx.input(placeholder='N', type='number', name='N', required=True, custom_attrs={'min':0}), 
                style=style.input_style | {'grid_column':'span 1'}
            ),
            rx.box(
                rx.text('M', text_align='center'),
                rx.input(placeholder='M', type='number', name='M', required=True),
                style=style.input_style | {'grid_column':'span 1'}
            ),  
            rx.box(
                rx.text('n', text_align='center'),
                rx.input(placeholder='n', type='number', name='n', required=True, custom_attrs={'min':0}), 
                style=style.input_style | {'grid_column':'span 1'}
            ),
            rx.box(
                rx.text('x', text_align='center'),
                rx.input(placeholder='x', type='number', name='x', required=True),
                style=style.input_style | {'grid_column':'span 1'}
            ),
            rx.button('Calcular',type='Submit', style=dict(grid_column='span 6')), 
            rx.box(
                rx.text('min', text_align='center'),
                rx.input(placeholder='x1', type='number', name='x1'),
                style=style.input_style | {'grid_column':'span 2'}
            ),
            rx.box(
                rx.text('max', text_align='center'),
                rx.input(placeholder='x2', type='number', name='x2'),
                style=style.input_style | {'grid_column':'span 2'}
            ),
            style=dict(
                display='grid',
                grid_template_columns='1fr 1fr 1fr 1fr',
                gap='4px',
                max_width='600px',
                margin='auto',
                margin_bottom='24px',
            ),
        ),
        display=State.hypergeometric_display,
    )


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "Calculadora de propabilidades",
            style=dict(
                text_align='center',
                margin_bottom='8px'
            )
        ),
        select_calculator(),
        binomial(),
        poisson(),
        hypergeometric()
    )

app = rx.App()
app.add_page(index)