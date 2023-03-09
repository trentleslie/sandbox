import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(4, 10)
        self.fc2 = nn.Linear(10, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create an instance of the neural network
net = Net()

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.1)

# Train the neural network
for epoch in range(100):
    running_loss = 0.0
    for i, data in enumerate(zip(X_train, y_train)):
        inputs, labels = data
        inputs = torch.Tensor(inputs)
        labels = torch.tensor([labels]).long()

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels.squeeze().long())  # convert labels to long here
        loss.backward()
        optimizer.step()

        # Print statistics
        running_loss += loss.item()
        if i % 10 == 9:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 10))
            running_loss = 0.0

print('Finished Training')

# Save the trained model
PATH = 'iris_net.pth'
torch.save(net.state_dict(), PATH)

# Evaluate the neural network on the test set
correct = 0
total = 0
with torch.no_grad():
    for i, data in enumerate(zip(X_test, y_test)):
        inputs, labels = data
        inputs = torch.Tensor(inputs)
        labels = torch.Tensor([labels]).long()

        # Predict the class label
        outputs = net(inputs)
        _, predicted = torch.max(outputs.data, 0)
        total += 1
        if predicted == labels:
            correct += 1

print('Accuracy of the network on the test set: %d %%' % (
    100 * correct / total))