# nanoGPT on (Silicon) Mac

Runs on an Apple M1 Pro with 16GB RAM.

## Examples Trainieren/Finetunen

```shell
wandb offline

# prepare data
python data/shakespeare_char/prepare.py
python data/shakespeare/prepare.py
python data/bundestag/prepare.py
python data/bundestag_ger/prepare.py

# 10 Shakespeare character-level tokenization
python train.py config/examples/10_train_shakespeare_char_mps.py
python sample.py --out_dir=out-shakespeare-char/10 >> out-shakespeare-char/10/sample.txt

# 20 Shakespeare sub-word encoding, quick training
python train.py config/examples/20_train_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/20 >> out-shakespeare/20/sample.txt

# 21 Shakespeare sub-word encoding, longer training
python train.py config/examples/21_finetune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/21 >> out-shakespeare/21/sample.txt

# 21 Shakespeare sub-word encoding, larger model
python train.py config/examples/22_tune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/22 >> out-shakespeare/22/sample.txt

# 30 Bundestag, quick training, medium model
python train.py config/examples/30_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/30 >> out-bundestag/30/sample.txt

# 31 Bundestag, longer training, medium model, high lr
python train.py config/examples/31_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/31 >> out-bundestag/31/sample.txt

# 32 Bundestag, longer training, small GerGPT model, high lr
python train.py config/examples/32_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/32 >> out-bundestag/32/sample.txt

# 33 Bundestag, longer training, medium model, improved lr
python train.py config/examples/33_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/33 >> out-bundestag/33/sample.txt

# 34 Bundestag, longer training, small GerGPT model, high lr, gpt2 encoding
python train.py config/examples/34_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/34 >> out-bundestag/34/sample.txt

# 35 Bundestag, longer training, small GerGPT model, high lr, ger-gpt2 encoding
python train.py config/examples/35_finetune_bundestag_mps.py
# python sample.py --out_dir=out-bundestag/35 --ger_encoding=True >> out-bundestag/35/sample.txt

# das hier dann komplett weg
python train.py config/examples/33_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/33 >> out-bundestag/33/sample.txt
python sample.py --out_dir=out-bundestag/31 >> out-bundestag/31/sample.txt
python sample.py --out_dir=out-bundestag/32 >> out-bundestag/32/sample.txt
python sample.py --out_dir=out-bundestag/35 --ger_encoding=True >> out-bundestag/35/sample.txt
```

## Tracking Lokal ansehen

Hier den lokalen API Key angeben, nicht den aus der Cloud Version die benötigt wird, um die kostenlose Lizenz zu organisieren. Warum einfach...

```shell
colima start
wandb server start
wandb login --host=http://localhost:8080  --relogin
wandb status # in case you want to check the host is the localhost
wandb sync --sync-all
wandb sync --clean
wandb server stop
colima stop
```


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
```

### 20. Shakespeare sub-word encoding

```shell

```

### 21. Shakespeare finetuning

Medium model works, large not.

```shell

```

### 22. Shakespeare finetuning

Medium model works, large not.

```shell
python train.py config/examples/22_tune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/22 >> out-shakespeare/22/sample.txt
```

## 30. Bundestag 20 iters

```shell

```

## 31. Bundestag 200 iters

```shell
python train.py config/examples/31_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/30 >> out-bundestag/31/sample.txt
```

## 32. Bundestag GermanGPT

```shell
python train.py config/examples/32_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/32 >> out-bundestag/32/sample.txt
```


## Tracking with W&B

To visualize tracking, the W&B server needs to be started and requires an account [(link)](https://docs.wandb.ai/guides/hosting/how-to-guides/basic-setup).

```shell
brew install colima docker docker-compose
colima start
wandb server start
```

## Wenn ich local mache

wandb offline






