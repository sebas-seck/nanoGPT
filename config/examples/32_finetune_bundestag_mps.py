import torch

out_dir = 'out-bundestag/32'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'bundestag'
wandb_run_name = 'tune-bt-ger-gpt2-ex32'

dataset = 'bundestag'
init_from = 'ger-gpt2' # this is comparable to the smallest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 200

learning_rate = 1e-3
lr_decay_iters = 300
min_lr = 3e-5 # learning_rate / 10 usually
decay_lr = True

device = 'mps' if  torch.backends.mps.is_available() else 'cpu'
compile = False # do not torch compile the model
