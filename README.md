# try-pixi

## Prerequisites

Install `pixi` and set autocompletion according [Getting Started - Pixi by prefix.dev](https://pixi.sh/latest/).
Currently, I use Pixi version: 0.26.1.

## Use Case: Pytorch

- [ ] 1. Install pytorch (check GPU)
- [ ] 2. Install other dependencies

### Setup From Scratch

Following is the showcase of setting up from empty project. And will choose the way of `pyproject.toml`.

In the root directory of the project, run `pixi init --pyproject`.

Install python: `pixi add python`.

Take cuda 11.8 as example:
```shell
pixi project channel add nvidia pytorch
# then manual change the channel sequence to ["nvidia", "conda-forge", "pytorch"]
pixi add --feature cuda118 pytorch==2.3.1 pytorch-cuda=11.8
pixi project environment add cuda118 -f cuda118
pixi install -e cuda118
```

Activate virtual environment: `pixi shell`.
