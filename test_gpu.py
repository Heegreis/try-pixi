import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
    print('GPU is available.')
    print('CUDA device name:', torch.cuda.get_device_name(0))

    # 簡單的 GPU 運算
    a = torch.randn(3, 3).to(device)
    b = torch.randn(3, 3).to(device)
    c = torch.matmul(a, b)
    print('Result of GPU computation:', c)
else:
    print('GPU is not available.')
    device = torch.device('cpu')
