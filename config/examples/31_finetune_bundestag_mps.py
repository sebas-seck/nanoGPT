import time

out_dir = 'out-bundestag/31'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'bundestag'
wandb_run_name = 'tune-bt-ger-gpt2-medium-ex31'

dataset = 'bundestag'
init_from = 'ger-gpt2-medium' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 200

# finetune at constant LR
learning_rate = 0.1
decay_lr = True

device = 'mps'  # run on cpu only
compile = False # do not torch compile the model
