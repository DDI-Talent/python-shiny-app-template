from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("slider_example", "N", 0, 100, 20),
    ui.output_text_verbatim("results"),
)


def server(input, output, session):
    @render.text
    def results():
        return f"n*2 is {input.slider_example() * 2}"


app = App(app_ui, server)
