import gradio as gr
import random
import datetime

pairs = [
    ("Hello, world!", "Hello, Gradio!"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
    ("Python", "Pyton"),
]

random.shuffle(pairs)

def evaluate_similarity(*scores):
    results = [(pairs[i], score) for i, score in enumerate(scores)]
    with open(f"{datetime.datetime.now()}.csv", "w") as f:
        for (str1, str2), answer in results:
            f.write(f"{str1}\t{str2}\t{answer}\n")
    return results

with gr.Blocks() as demo:
    gr.Markdown("### 50組の文字列ペアの近さを評価してください (0-1の間)")
    
    sliders = []
    for i, (string1, string2) in enumerate(pairs):
        gr.Markdown(f"#### ペア {i+1}")
        gr.Markdown(f"**String 1:** {string1}")
        gr.Markdown(f"**String 2:** {string2}")
        slider = gr.Slider(0, 1, label=f"文字列ペア {i+1} の近さを評価", step=0.01)
        sliders.append(slider)
    
    output = gr.Dataframe(headers=["文字列ペア", "評価"])
    submit_button = gr.Button("評価を送信")
    
    submit_button.click(evaluate_similarity, inputs=sliders, outputs=output)

# Webアプリを実行
demo.launch()