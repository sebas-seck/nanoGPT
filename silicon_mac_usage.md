# nanoGPT on Silicon Mac

Tested with Apple M1 Pro.

## Environment setup (pyenv)

```shell
pyenv install -v 3.10
pyenv virtualenv 3.10 gpt310
pyenv activate gpt310

poetry install --with dev
```

## Sharespeare Examples

### Character-level tokenization

```shell
python data/shakespeare_char/prepare.py
python train.py config/train_shakespeare_char_mps.py --device mps
python sample.py --out_dir=out-shakespeare-char --device=mps >> out-shakespeare-char/sample.txt
```

## Tracking with W&B

To visualize tracking, the W&B server needs to be started and requires an account [(link)](https://docs.wandb.ai/guides/hosting/how-to-guides/basic-setup).

```shell
brew install colima docker docker-compose
colima start
wandb server start
```
