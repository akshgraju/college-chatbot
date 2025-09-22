import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# --- 1. PREPARE THE DATA ---
words = []
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Loop through each intent in the JSON file
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word in the pattern (sentence)
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add the pair (tokenized words, intent tag) to our documents list
        documents.append((w, intent['tag']))
        # If the intent's tag is not already in our classes list, add it
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize words, convert to lowercase, and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
# Sort classes alphabetically
classes = sorted(list(set(classes)))

# Print stats
print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# Save the words and classes lists to pickle files for later use
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# --- 2. CREATE TRAINING AND TESTING DATA ---
training = []
output_empty = [0] * len(classes)

# Create our training set (bag of words model)
for doc in documents:
    # Initialize our bag of words for this document
    bag = []
    # Get the tokenized words for the pattern
    pattern_words = doc[0]
    # Lemmatize and lowercase each word
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    # Create the bag of words array: 1 if word match found in current pattern, else 0
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # Create the output row: 0 for each tag, and 1 for the current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])

# Shuffle the training data and convert to a NumPy array
random.shuffle(training)
training = np.array(training, dtype=object) # Use dtype=object to handle lists of different lengths

# Split the data into features (train_x) and labels (train_y)
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")

# --- 3. BUILD AND TRAIN THE NEURAL NETWORK MODEL ---
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model
# Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
# An epoch is one run through all the training data
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save the trained model to a file
model.save('chatbot_model.h5', hist)

print("Model created and saved!")