# nanoGPT on Silicon Mac

Runs on an Apple M1 Pro with 16GB RAM.

## Environment setup (pyenv)

```shell
pyenv install -v 3.10
pyenv virtualenv 3.10 gpt310
pyenv activate gpt310

poetry install --with dev
```

## Shakespeare Examples

### Character-level tokenization

```shell
python data/shakespeare_char/prepare.py
python train.py config/train_shakespeare_char_mps.py
python sample.py --out_dir=out-shakespeare-char --device=mps >> out-shakespeare-char/sample.txt
```

### Shakespeare finetuning

Medium model works, large not.

```shell
python data/shakespeare/prepare.py
python train.py config/finetune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare --device=mps >> out-shakespeare/sample.txt
```

## Bundestag Beispiel

```shell
python data/bundestag/prepare.py
python train.py config/finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag --device=mps >> out-bundestag/sample.txt
```


## Tracking with W&B

To visualize tracking, the W&B server needs to be started and requires an account [(link)](https://docs.wandb.ai/guides/hosting/how-to-guides/basic-setup).

```shell
brew install colima docker docker-compose
colima start
wandb server start
```

## Wenn ich local mache
wandb server start
wandb login --host=http://localhost:8080
