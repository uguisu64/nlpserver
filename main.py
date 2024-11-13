import gradio as gr
import random
import datetime
import json

# データを読み込み
with open('result.json', "r") as fp:
    data = json.load(fp)

low_sim = data["low_sim"]
middle_sim = data["middle_sim"]
high_sim = data["high_sim"]

pairs = []

# インデックスとラベルを付けてペアを作成
for i, item in enumerate(low_sim):
    pairs.append((i, "low", item["sentence1"], item["sentence2"]))
for i, item in enumerate(middle_sim, start=len(low_sim)):
    pairs.append((i, "middle", item["sentence1"], item["sentence2"]))
for i, item in enumerate(high_sim, start=len(low_sim) + len(middle_sim)):
    pairs.append((i, "high", item["sentence1"], item["sentence2"]))

# ペアをシャッフル
random.shuffle(pairs)

# 評価関数
def evaluate_similarity(*scores):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    results = [(index, label, str1, str2, score) for (index, label, str1, str2), score in zip(pairs, scores)]
    
    # CSVファイルに保存
    filename = f"similarity_evaluation_{timestamp}.csv"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Index\tLabel\tString1\tString2\tScore\n")
        for index, label, str1, str2, score in results:
            f.write(f"{index}\t{label}\t{str1}\t{str2}\t{score}\n")
    
    return results

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("### 50組の文字列ペアの近さを評価してください (0-1の間)")
    
    sliders = []
    for i, (index, label, string1, string2) in enumerate(pairs):
        gr.Markdown(f"#### ペア {i+1}")
        gr.Markdown(f"**String 1:** {string1}")
        gr.Markdown(f"**String 2:** {string2}")
        slider = gr.Slider(0, 1, label=f"文字列ペア {i+1} の近さを評価", step=0.01)
        sliders.append(slider)
    
    output = gr.Dataframe(headers=["Index", "Label", "String1", "String2", "Score"])
    submit_button = gr.Button("評価を送信")
    
    # 評価関数の呼び出し
    submit_button.click(evaluate_similarity, inputs=sliders, outputs=output)

# Webアプリを実行
demo.launch(server_name="0.0.0.0")
