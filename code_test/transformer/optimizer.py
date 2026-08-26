import torch
import torch.nn as nn
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
num_epochs = 10
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

for epoch in range(num_epochs):
    model.train()
    
    for x, y in dataloader:
         x = x.to(device)
         y = y.to(device)

         optimizer.zero_grad()
         output = model(x)
         loss = criterion(output, y)