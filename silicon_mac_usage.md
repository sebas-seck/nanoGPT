# nanoGPT on (Silicon) Mac

Runs on an Apple M1 Pro with 16GB RAM.

## Examples Trainieren/Finetunen

```shell
wandb offline

# prepare data
python data/shakespeare_char/prepare.py
python data/shakespeare/prepare.py
python data/bundestag/prepare.py

# 10 Shakespeare character-level tokenization
python train.py config/examples/10_train_shakespeare_char_mps.py
python sample.py --out_dir=out-shakespeare-char/10 --device=mps >> out-shakespeare-char/10/sample.txt

# 20 Shakespeare sub-word encoding, quick training
python train.py config/examples/20_train_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/20 --device=mps >> out-shakespeare/20/sample.txt

# 21 Shakespeare sub-word encoding, longer training
python train.py config/examples/21_finetune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/21 --device=mps >> out-shakespeare/21/sample.txt

# 21 Shakespeare sub-word encoding, larger model
python train.py config/examples/22_tune_shakespeare_mps.py
python sample.py --out_dir=out-shakespeare/22 --device=mps >> out-shakespeare/22/sample.txt

# 30 Bundestag, quick training, medium model
python train.py config/examples/30_finetune_bundestag_mps.py
# python sample.py --out_dir=out-bundestag/30 --device=mps >> out-bundestag/30/sample.txt

# 31 Bundestag, longer training, medium model, high lr
python train.py config/examples/31_finetune_bundestag_mps.py
# python sample.py --out_dir=out-bundestag/31 --device=mps >> out-bundestag/31/sample.txt

# 32 Bundestag, longer training, small GerGPT model, high lr
python train.py config/examples/32_finetune_bundestag_mps.py
# python sample.py --out_dir=out-bundestag/32 --device=mps >> out-bundestag/32/sample.txt

# 33 Bundestag, longer training, medium model, improved lr
python train.py config/examples/33_finetune_bundestag_mps.py
# python sample.py --out_dir=out-bundestag/33 --device=mps >> out-bundestag/33/sample.txt

# 34 Bundestag, longer training, small GerGPT model, high lr
python train.py config/examples/34_finetune_bundestag_mps.py
# python sample.py --out_dir=out-bundestag/34 --device=mps >> out-bundestag/34/sample.txt

python train.py config/examples/10_train_shakespeare_char_mps.py
```

## Tracking Lokal ansehen

Hier den lokalen API Key angeben, nicht den aus der Cloud Version die benötigt wird, um die kostenlose Lizenz zu organisieren. Warum einfach...

```shell
colima start
wandb server start
wandb login --host=http://localhost:8080  --relogin
wandb status # check the host is the localhost
wandb sync --sync-all
wandb sync --clean
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
python sample.py --out_dir=out-shakespeare/22 --device=mps >> out-shakespeare/22/sample.txt
```

## 30. Bundestag 20 iters

```shell

```

## 31. Bundestag 200 iters

```shell
python train.py config/examples/31_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/30 --device=mps >> out-bundestag/31/sample.txt
```

## 32. Bundestag GermanGPT

```shell
python train.py config/examples/32_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/32 --device=mps >> out-bundestag/32/sample.txt
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






