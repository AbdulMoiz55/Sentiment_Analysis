
pip install transformers
pip install datasets
import transformers
from transformers import pipeline

pipe = pipeline("text-classification")
pipe("I love watching afghanistan lose a game")
from transformers import pipeline

classifier = pipeline("text-classification", model = "roberta-large-mnli")
classifier("A soccer game with multiple males playing. Some men are playing a sport.")
