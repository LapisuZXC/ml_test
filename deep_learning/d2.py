import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset
from torchvision.datasets import MNIST
from torchvision import transforms

"""
Напишите функцию create_model, которая должна возвращать полносвязную нейронную сеть из двух слоев. 
На вход должно быть 100 чисел, на выход 1, посередине 10. В качестве нелинейности используйте ReLU. 
Воспользуйтесь nn.Sequential и передайте слои как последовательность.
"""


def create_model() -> nn.Sequential:
    return nn.Sequential(nn.Linear(100, 10), nn.ReLU(), nn.Linear(10, 1))


"""
Напишите функцию train. Она должна принимать на вход нейронную сеть, даталоадер, оптимизатор и функцию потерь. Она должна иметь следующую сигнатуру:
 def train(model: nn.Module, data_loader: DataLoader, optimizer: Optimizer, loss_fn):
Внутри функции сделайте следующие шаги:
1. Переведите модель в режим обучения.
2. Проитерируйтесь по даталоадеру.
3. На каждой итерации:
    - Занулите градиенты с помощью оптимизатора
    - Сделайте проход вперед (forward pass)
    - Посчитайте ошибку
    - Сделайте проход назад (backward pass)
    - Напечатайте ошибку на текущем батче с точностью до 5 символов после запятой (только число)
    - Сделайте шаг оптимизации
Функция должна вернуть среднюю ошибку за время прохода по даталоадеру.
"""


def train(
    model: nn.Module,
    data_loader: torch.utils.data.DataLoader,
    optimizer: optim.Optimizer,
    loss_fn,
) -> int | float:
    model.train()
    total_loss = 0.0
    num_batches = len(data_loader)
    for batch in data_loader:
        inputs, target = batch
        outputs = model(inputs)
        optimizer.zero_grad()
        loss = loss_fn(outputs, target)
        loss.backward()
        optimizer.step()
        print(f"{loss.item():.5f}")
        total_loss += loss.item()  # Добавляем ошибку в сумму

    return total_loss / num_batches


"""
Напишите функцию evaluate. Она должна принимать на вход нейронную сеть, даталоадер и функцию потерь. Она должна иметь следующую сигнатуру: def evaluate(model: nn.Module, data_loader: DataLoader, loss_fn):
Внутри функции сделайте следующие шаги:
1. Переведите модель в режим инференса (применения)
2. Проитерируйтесь по даталоадеру
3. На каждой итерации:
    - Сделайте проход вперед (forward pass)
    - Посчитайте ошибку
Функция должна вернуть среднюю ошибку за время прохода по даталоадеру.
"""


def evaluate(model: nn.Module, data_loader: DataLoader, loss_fn) -> float:
    model.eval()  # Переводим модель в режим инференса
    total_loss = 0.0
    num_batches = len(data_loader)

    device = next(model.parameters()).device  # Определяем устройство (CPU/GPU)

    with torch.no_grad():  # Отключаем градиенты
        for inputs, targets in data_loader:
            inputs, targets = (
                inputs.to(device),
                targets.to(device),
            )  # Переносим на GPU/CPU
            outputs = model(inputs)  # Прямой проход
            loss = loss_fn(outputs, targets)  # Вычисляем ошибку
            total_loss += loss.item()

    return total_loss / num_batches  # Возвращаем среднюю ошибку


"""
Обучите свою первую нейронную сеть!
Обучите полносвязную нейронную сеть для классификации на датасете MNIST. Добейтесь качества в 98% на тестовой выборке.
Обучите сверточную нейронную сеть для классификации на датасете MNIST. Добейтесь качества в 99.3% на тестовой выборке.
Можете использовать уже написанные ранее функции train и evaluate.3
Чтобы мы могли проверить вашу модель, напишите функцию, которая создает вашу модель и возвращает объект, назовите функцию create_mlp_model,
без аргументов. Вам понадобится сохранить веса вашей модели и сдать их в тестировщик, для этого воспользуйтесь методами torch.save и state_dict.
"""


def create_mlp_model():
    return MLP()


class MLP(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 10)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x.view(-1, 28 * 28)  # Преобразуем 28x28 вектора в одномерный массив
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x


class CNN(nn.Module):
    def __init__(self) -> None:
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(
            in_channels=32, out_channels=64, kernel_size=3, padding=1
        )
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.25)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.relu(self.conv1(x))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)  # Разворачиваем в вектор
        x = self.dropout(self.relu(self.fc1(x)))
        x = self.fc2(x)
        return x


# Функция для создания модели
def create_cnn_model() -> CNN:
    return CNN()


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform: transforms.Compose = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    )

    ds_train = MNIST("./data", True, transform=transform, download=True)
    ds_test = MNIST("./data", False, transform=transform, download=True)
    dl_train = DataLoader(dataset=ds_train, batch_size=3, shuffle=True)
    dl_test = DataLoader(dataset=ds_test, batch_size=10, shuffle=False)
    model = create_mlp_model().to(device)
    criterion: nn.CrossEntropyLoss = nn.CrossEntropyLoss()
    optimizer: optim.Adam = optim.Adam(model.parameters(), lr=0.001)

    train(model, dl_train, optimizer, criterion)
    test_accuracy: float = evaluate(model, dl_test, criterion)

    # Сохраняем веса модели
    torch.save(model.state_dict(), "mlp_mnist.pth")
    print("Модель сохранена в файл mlp_mnist.pth")
    print(f"test accuracy: {test_accuracy}")
    del model
    cnn = create_cnn_model().to(device)
    optimizer = optim.Adam(cnn.parameters(), lr=0.001)
    train(cnn, dl_train, optimizer, criterion)
    test_accuracy = evaluate(cnn, dl_test, criterion)
    torch.save(cnn.state_dict(), "cnn_mnist.pth")
    print("saved")
    print(f"test accuracy: {test_accuracy}")
