# nanoGPT on (Silicon) Mac

Runs on an Apple M1 Pro with 16GB RAM.

## Environment setup (pyenv)

```shell
pyenv install -v 3.10
pyenv virtualenv 3.10 gpt310
pyenv activate gpt310

poetry install --with dev
```

## Shakespeare Examples

### 10. Character-level tokenization

```shell
python data/shakespeare_char/prepare.py
python train.py config/examples/10_train_shakespeare_char_mps.py
python sample.py --out_dir=out-shakespeare-char/10 --device=mps >> out-shakespeare-char/10/sample.txt
```

### 20. Shakespeare sub-word encoding

```shell
python data/shakespeare/prepare.py
python train.py config/examples/20_train_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/20 --device=mps >> out-shakespeare/20/sample.txt
```

### Shakespeare finetuning

Medium model works, large not.

```shell
python train.py config/examples/21_tune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/21 --device=mps >> out-shakespeare/21/sample.txt
```

## 30. Bundestag Beispiel

```shell
python data/bundestag/prepare.py
python train.py config/examples/30_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/30 --device=mps >> out-bundestag/30/sample.txt
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
