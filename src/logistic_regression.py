import random
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

class logistic_regression:
  def __init__(self, model_name, epochs = 2000, lr = 0.01, test_ratio = 0.2) -> None:
    self.model_name = model_name
    self.epochs = epochs
    self.lr = lr
    self.test_ratio = test_ratio
    self.load('params.csv')
    self.loss_history = []
  
  def split_train_test(self, x, y):
    combined = list(zip(x, y))
    random.shuffle(combined)
    shuffled_x, shuffled_y = zip(*combined)

    split_point = int((1 - self.test_ratio) * len(shuffled_x))
    self.x_train = np.array(shuffled_x[:split_point])
    self.y_train = np.array(shuffled_y[:split_point])
    self.x_test = np.array(shuffled_x[split_point:])
    self.y_test = np.array(shuffled_y[split_point:])

  def standardize(self, x, y):
      self.min_x = x.min(axis=0)
      self.max_x = x.max(axis=0)
      x_normalized = (x - self.min_x) / (self.max_x - self.min_x)
      return x_normalized

  def train(self, x, y):
    self.theta = np.zeros(len(x[0]))
    x = self.standardize(x,y)
    self.split_train_test(x, y)
    m, n = len(self.x_train), len(self.x_train[0])
    self.theta = np.zeros(n).reshape(-1, 1) 
    for epoch in range(self.epochs):
      z = np.dot(self.x_train, self.theta)
      g = 1 / (1 + np.exp(-z))
      g = g.reshape(-1, 1)  
      gradient = (np.dot(self.x_train.T, (g - self.y_train)) / m).reshape(-1, 1) 
      self.theta -= self.lr * gradient
      self.loss_history.append((epoch, self.calculate_loss()))
    y_pred = self.predict(self.x_test)
    acc = accuracy_score(self.y_test, y_pred)
    print(f"Model {self.model_name} achieved an accuracy of {acc} with a test ratio of {self.test_ratio}.")
    self.plot_loss()
    self.save('params.csv')

  def calculate_loss(self):
    z = np.dot(self.x_train, self.theta)
    g = 1 / (1 + np.exp(-z))
    epsilon = 1e-15
    loss = -np.sum(self.y_train * np.log(g + epsilon) + (1 - self.y_train) * np.log(1 - g + epsilon)) / len(self.x_train)
    return loss

  def plot_loss(self):
    epochs, loss_values = zip(*self.loss_history)
    plt.plot(epochs, loss_values)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Loss vs. Epoch")
    plt.show()
  
  def save(self, filename):
    with open(filename, mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([self.model_name])
      writer.writerow(['theta'] + [str(val[0]) for val in self.theta])
      writer.writerow(['min_x'] + [str(val) for val in self.min_x])
      writer.writerow(['max_x'] + [str(val) for val in self.max_x])
    print(f"Parameters saved for model '{self.model_name}' to {filename}")

  def load(self, filename):
    if not os.path.isfile(filename):
      print(f"File '{filename}' not found. Initializing with default values.")
      self.theta = np.zeros(1)
      self.min_x = np.zeros(1)
      self.max_x = np.zeros(1)
      return

    self.theta = np.zeros(1)
    self.min_x = np.zeros(1)
    self.max_x = np.zeros(1)
    
    with open(filename, mode='r', newline='') as file:
      reader = csv.reader(file)
      lines = list(reader)
      
      for i in range(len(lines)):
        if lines[i][0] == self.model_name:
          if lines[i + 1][0] == 'theta':
            self.theta = np.array([float(val) for val in lines[i + 1][1:]])
          if lines[i + 2][0] == 'min_x':
            self.min_x = np.array([float(val) for val in lines[i + 2][1:]])
          if lines[i + 3][0] == 'max_x':
            self.max_x = np.array([float(val) for val in lines[i + 3][1:]])
              
          print(f"Parameters loaded for model '{self.model_name}' from {filename}")
          return

    print(f"Model '{self.model_name}' not found in {filename}. Initializing with default values.")

  def predict_prob(self, x):
    x_normalized = (x - self.min_x) / (self.max_x - self.min_x)
    z = np.dot(x_normalized, self.theta)
    g = 1 / (1 + np.exp(-z))
    return g
  
  def predict(self, x):
    x_normalized = (x - self.min_x) / (self.max_x - self.min_x)
    z = np.dot(x_normalized, self.theta)
    g = 1 / (1 + np.exp(-z))
    predictions = (g >= 0.5).astype(int)
    return predictions