out_dir = 'out-bundestag-ger/40'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'bundestag-ger'
wandb_run_name = 'train-bt-ex40'

dataset = 'bundestag_ger'
init_from = "scratch"

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 600

decay_lr = True
learning_rate = 3e-2
decay_rate = 0.977237
decay_iters = 300

device = 'mps'
compile = False # do not torch compile the model
