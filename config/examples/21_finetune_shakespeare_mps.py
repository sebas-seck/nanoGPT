import time

out_dir = 'out-shakespeare/21'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'shakespeare_test'
wandb_run_name = 'tune-sp-gpt2-ex21'

dataset = 'shakespeare'
init_from = 'gpt2' # this is the smallest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 200

decay_lr = True
learning_rate = 0.1
decay_rate = 0.95
decay_steps = 150

device = 'mps'
compile = False # do not torch compile the model
