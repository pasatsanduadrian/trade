import gradio as gr
import os
from pathlib import Path

# Citește fișierul HTML
def load_html():
    html_path = Path(__file__).parent / "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# Funcție pentru a servi aplicația
def serve_trading_bot():
    html_content = load_html()
    return f"""
    <div style="width: 100%; height: 100vh; overflow: hidden;">
        <iframe 
            srcdoc='{html_content.replace("'", "&apos;")}' 
            style="width: 100%; height: 100vh; border: none;"
            sandbox="allow-scripts allow-same-origin allow-forms allow-modals allow-popups"
        ></iframe>
    </div>
    """

# Creează interfața Gradio
with gr.Blocks(title="Solana Pump.fun Trading Bot", theme=gr.themes.Base()) as app:
    gr.HTML(value=serve_trading_bot())

# Configurare pentru Colab
if __name__ == "__main__":
    # În Colab, setăm share=True pentru acces public
    import sys
    is_colab = 'google.colab' in sys.modules

    # CLI override: `python app.py --share`
    force_share = "--share" in sys.argv

    app.launch(
        share=True if is_colab or force_share else False,
        server_name="0.0.0.0",
        server_port=7860,
        height=1000,
        width="100%",
        quiet=False,
        show_api=False
    )
