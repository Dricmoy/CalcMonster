# train.py
from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_from_disk

def train_model(model_name, tokenized_dataset_path):
    # Load pre-trained model
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Load tokenized dataset
    tokenized_dataset = load_from_disk(tokenized_dataset_path)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./results",          # Output directory
        evaluation_strategy="steps",     # Evaluate at each step
        learning_rate=2e-5,              # Learning rate
        per_device_train_batch_size=4,   # Batch size for training
        per_device_eval_batch_size=4,    # Batch size for evaluation
        num_train_epochs=3,              # Number of epochs
        weight_decay=0.01,               # Weight decay
        logging_steps=100,               # Log every X steps
        save_steps=1000,                 # Save every X steps
        eval_steps=500,                  # Evaluate every X steps
        save_total_limit=2,              # Keep the 2 most recent checkpoints
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset['train'],
        tokenizer=model_name,
    )

    # Start training
    trainer.train()

if __name__ == "__main__":
    model_name = "meta-llama/Meta-Llama-3-70B"
    tokenized_dataset_path = "dataset/tokenized_textbook"
    
    train_model(model_name, tokenized_dataset_path)
