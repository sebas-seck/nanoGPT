# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-shakespeare-char/10'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = True
wandb_project = 'shakespeare-char'
wandb_run_name = 'train-sp-ex10'

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

max_iters = 5000
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

decay_lr = True
learning_rate = 1e-3 # with baby networks can afford to go a bit higher
decay_rate = 0.99999
decay_iters = 4000

warmup_iters = 100 # not super necessary potentially

import torch
device = 'mps' if  torch.backends.mps.is_available() else 'cpu'
compile = False # do not torch compile the model
