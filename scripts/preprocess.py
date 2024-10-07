# preprocess.py
from datasets import load_dataset
from transformers import AutoTokenizer

def preprocess_dataset(text_file, model_name):
    # Load your dataset
    dataset = load_dataset('text', data_files={'train': text_file})

    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the dataset
    def tokenize_function(examples):
        return tokenizer(examples['text'], padding='max_length', truncation=True, max_length=512)

    tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
    return tokenized_dataset

if __name__ == "__main__":
    # Path to the dataset and model name
    text_file = "dataset/textbook.txt"
    model_name = "meta-llama/Meta-Llama-3-70B"
    
    tokenized_dataset = preprocess_dataset(text_file, model_name)
    # Save tokenized dataset if needed
    tokenized_dataset.save_to_disk("dataset/tokenized_textbook")
