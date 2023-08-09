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

# 35 Bundestag, longer training, small GerGPT model, constant small lr, ger-gpt2 encoding
python train.py config/examples/35_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag-ger/35 --ger_encoding=True >> out-bundestag-ger/35/sample.txt

# 36 Bundestag, longer training, small GerGPT model, high lr decaying, ger-gpt2 encoding
python train.py config/examples/36_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag-ger/36 --ger_encoding=True >> out-bundestag-ger/36/sample.txt

# 37 Bundestag, comparable to 36 but with non-GER model
python train.py config/examples/37_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag/37 --ger_encoding >> out-bundestag/37/sample.txt

# 38 Bundestag, even longer, GerGPT, start at 0.01, decay to 0.00003 after 300 iter
python train.py config/examples/38_finetune_bundestag_mps.py
python sample.py --out_dir=out-bundestag-ger/38 --ger_encoding=True >> out-bundestag-ger/38/sample.txt

# 40 Bundestag, same as 38 but from scratch
python train.py config/examples/40_train_bundestag_mps.py
python sample.py --out_dir=out-bundestag-ger/40 --ger_encoding=True >> out-bundestag-ger/40/sample.txt
```

## Tracking Lokal ansehen

Weights & Balances braucht einen Account, auch wenn das Tracking rein lokal stattfindet [(link)](https://docs.wandb.ai/guides/hosting/how-to-guides/basic-setup). Im Offline Modus muss kein Tracking Server laufen, alles wird in Files getrackt und später eingelesen. Um den Server an Mac ohne Docker Desktop anzuzeigen nutze ich Colima (`brew install colima docker docker-compose`). Beim Login muss der lokale API Key aus localhost:8080/authorize angegeben werden, nicht der aus dem obligatorischen Cloud Account. Warum einfach...

```shell
colima start
wandb server start
wandb login --host=http://localhost:8080  --relogin
wandb status # in case you want to check the host is the localhost
wandb sync --sync-all
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
