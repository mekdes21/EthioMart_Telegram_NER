import pandas as pd

# Load dataset (replace with actual path to your dataset)
df = pd.read_csv('../data/preprocessed_data/preprocessed_data.csv')

# Function to label each message in CoNLL format
def label_message(message):
    tokens = message.split()
    labeled_tokens = []

    # Entity labeling logic (modify this as per your data)
    for token in tokens:
        if token in ['ዋጋ', 'ብር']:  # Example price entity
            label = 'B-PRICE' if token == 'ዋጋ' else 'I-PRICE'
        elif token in ['አዲስ', 'አበባ']:  # Example location entity
            label = 'B-LOC' if token == 'አዲስ' else 'I-LOC'
        elif token.lower() in ['shoe', 'bottle']:  # Example product entity
            label = 'B-Product' if token == 'shoe' else 'I-Product'
        else:
            label = 'O'  # Outside any entity
        
        labeled_tokens.append(f"{token}\t{label}")
    
    # Return labeled tokens in CoNLL format (separated by blank lines between messages)
    return '\n'.join(labeled_tokens) + '\n'

# Save the labeled data to a CoNLL formatted file
with open('labeled_data.txt', 'w', encoding='utf-8') as f:
    for idx, row in df.iterrows():
        message = row['Message']
        labeled_message = label_message(message)
        f.write(labeled_message)
        f.write('\n')  # Blank line between messages
