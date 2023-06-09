# AUTOGENERATED! DO NOT EDIT! File to edit: ../app.ipynb.

# %% auto 0
__all__ = ['learner', 'categories', 'image', 'label', 'examples', 'intf', 'classify_image']

# %% ../app.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% ../app.ipynb 3
learner = load_learner("export.pkl")

# %% ../app.ipynb 5
categories = ("Goldfish", "Tench", "White shark")

def classify_image(img):
    pred, idx, probs = learner.predict(img)
    probs_float = map(float, probs)
    return dict(zip(categories, probs_float))

# %% ../app.ipynb 7
image = gr.inputs.Image(shape= (192, 192))
label = gr.outputs.Label()
examples = ["goldfish.jpg", "tench.jpg", "white_shark.jpg"]

intf = gr.Interface(
    fn = classify_image,
    inputs = image,
    outputs = label,
    examples = examples)
intf.launch(inline= False)
