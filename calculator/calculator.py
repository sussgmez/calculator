import reflex as rx
import scipy

from calculator import style
from calculator.state import State, BinomialFormState



def select_calculator() -> rx.Component:
    return rx.box(
        rx.button('Distribucion Binomial', style=style.button_style, on_click=State.show_binomial),
        rx.button('Distribucion De Poisson', style=style.button_style),
        rx.button('Distribucion Hipergeometrica', style=style.button_style),
        rx.button('Distribucion Normal', style=style.button_style),
        style=dict(
            display='flex', 
            gap='4px', 
            width='fit-content', 
            flex_wrap='wrap',
            margin='auto',
            margin_bottom='8px'
        )
    )


def binomial() -> rx.Component:
    return rx.box(
        rx.form(
            rx.box(
                rx.text('n', text_align='center'),
                rx.input(placeholder='n', type='number', name='n', required=True),
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
                rx.input(placeholder='x1', type='number', name='min'),
                style=style.input_style | {'grid_column':'span 3'}
            ),
            rx.box(
                rx.text('max', text_align='center'),
                rx.input(placeholder='x2', type='number', name='max'),
                style=style.input_style| {'grid_column':'span 3'}
            ),
            style=dict(
                display='grid',
                grid_template_columns='1fr 1fr 1fr 1fr 1fr 1fr',
                gap='4px'
            ),
            on_submit=BinomialFormState.handle_submit,
        ),
        rx.container(
            rx.box(
                rx.text('Resultados: ', font_weight=800),
                rx.text('P(x): ', font_weight=800),
                rx.text(BinomialFormState.result1, display='block', margin='auto'),
                rx.text('P(x>xi): ', font_weight=800),
                rx.text(BinomialFormState.result2, display='block', margin='auto'),
                rx.text('P(x<xi): ', font_weight=800),
                rx.text(BinomialFormState.result3, display='block', margin='auto'),
                rx.text('P(x>=xi): ', font_weight=800),
                rx.text(BinomialFormState.result4, display='block', margin='auto'),
                rx.text('P(x<=xi): ', font_weight=800),
                rx.text(BinomialFormState.result5, display='block', margin='auto'),
                rx.text('P(x1<x<x2): ', font_weight=800),
                rx.text(BinomialFormState.result6, display='block', margin='auto'),
                rx.text('P(x1<=x<=x2): ', font_weight=800),
                rx.text(BinomialFormState.result7, display='block', margin='auto'),
                
                style = dict(
                    display='flex',
                    flex_direction='column',
                    gap='8px',
                    justify_content='center'
                ),
            ),
        ),
        rx.container(
            rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key='vl', fill='#82ca9d'
                ),
                rx.recharts.x_axis(data_key='name'),
                rx.recharts.y_axis(),
                data=BinomialFormState.data,
                height=400
            ),
        ),
        display=State.binomial_display,
        style=dict(

        )
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
        binomial()  
    )

app = rx.App()
app.add_page(index)