import torch

if torch.cuda.is_available():
    print("GPU is available!")
    device = torch.device("cuda")
    print(f"Using device: {device}")
    print(f"Cuda version: {torch.version.cuda}")
    print()
else:
    print("GPU is not available.")
