import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)

async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    with gr.Row():
        cancel_button = gr.Button("Cancel")
        clear_button = gr.Button("Clear")
    report = gr.Markdown(label="Report")

    run_event = run_button.click(fn=run, inputs=query_textbox, outputs=report)
    submit_event = query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

    # Cancel any in-flight events from both Run and Enter-submit
    cancel_button.click(fn=None, inputs=None, outputs=None, cancels=[run_event, submit_event])

    # Clear both the query and the report
    clear_button.click(fn=lambda: ("", ""), inputs=None, outputs=[query_textbox, report])

ui.queue()
ui.launch(inbrowser=True)
