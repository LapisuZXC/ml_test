import torch
import numpy as np


def function1(tensor: torch.Tensor, count_over: str) -> torch.Tensor:
    match count_over:
        case "columns":
            return torch.Tensor(
                [
                    np.mean([tensor[x][y] for x in range(len(tensor[0]))])
                    for y in range(len(tensor))
                ]
            )
        case "rows":
            return torch.Tensor([tensor[x].mean() for x in range(len(tensor))])


tensor1 = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tensor2 = torch.Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

print(function1(tensor1, "rows"))
print(function1(tensor1, "columns"))
print(function1(tensor2, "rows"))
print(function1(tensor2, "columns"))
