"""
This code is a practical implementation of the PyTorch RNN model for name classification.
References: https://www.youtube.com/watch?v=WEV61GmmPrk&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=19
"""
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from utils import POSSIBLE_LETTERS, N_LETTERS
from utils import load_data, letter_to_tensor, line_to_tensor, random_training_example

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        
        self.hidden_size = hidden_size
        # Input to hidden layer
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        # Input to output layer
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        # Softmax layer
        self.softmax = nn.LogSoftmax(dim=1)

    # Forward pass
    def forward(self, input_tensor, hidden_tensor):
        # Input + Hidden ==> Combined
        # Combined =[i2h]=> Hidden
        # Combined =[i2o]=> Pre_SoftMax =[softmax]=> Output
        combined = torch.cat((input_tensor, hidden_tensor), 1) # Along dimension 1

        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)

        return output, hidden
    
    # Initialize hidden state
    def init_hidden(self):
        return torch.zeros(1, self.hidden_size)
    
category_lines, all_categories = load_data()
n_categories = len(all_categories)

# Hyperparameters
n_hidden = 128

# Input ==> 1 x n_letters; Hidden ==> 1 x n_hidden; Output ==> 1 x n_categories
rnn = RNN(N_LETTERS, n_hidden, n_categories)

def category_from_output(output):
    # Output from SoftMax, therefore, take the index of the greatest value
    category_idx = torch.argmax(output).item()
    return all_categories[category_idx]

# Hyperparameters
crtiterion = nn.NLLLoss() # Negative Log Likelihood Loss
learning_rate = 0.005
optimizer = torch.optim.SGD(rnn.parameters(), lr=learning_rate) # Stocastic Gradient Descent

def train(line_tensor, category_tensor):
    # One training step
    hidden = rnn.init_hidden()

    # For each letter in the name
    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    # Calculate loss
    loss = crtiterion(output, category_tensor)

    # Backpropagation (Optimization)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return output, loss.item()

# Training
current_loss = 0
all_losses = []
plot_steps, print_steps = 1000, 5000
n_iters = 100000

for i in range(n_iters):
    category, line, category_tensor, line_tensor = random_training_example(category_lines, all_categories)

    output, loss = train(line_tensor, category_tensor)
    current_loss += loss

    if (i + 1) % plot_steps == 0:
        all_losses.append(current_loss / plot_steps)
        current_loss = 0
    
    if (i + 1) % print_steps == 0:
        guess = category_from_output(output)
        correct = '✓' if guess == category else '✗ (%s)' % category
        print(f'{i + 1} {i / n_iters * 100:.2f}% ({loss:.4f}) {line} / {guess} {correct}')

plt.figure()
plt.plot(all_losses)
plt.show()

def predict(input_line):
    print(f'Predicting category for {input_line}')
    with torch.no_grad():
        line_tensor = line_to_tensor(input_line)
        hidden = rnn.init_hidden()

        for i in range(line_tensor.size()[0]):
            output, hidden = rnn(line_tensor[i], hidden)

        print(category_from_output(output))

while True:
    name = input('Enter a name: ')
    if name == 'exit':
        break
    predict(name)