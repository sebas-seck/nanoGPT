out_dir = 'out-bundestag-ger/41'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'bundestag-ger'
wandb_run_name = 'train-bt-ex41'

dataset = 'bundestag_ger'
init_from = "scratch"

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 1000

dropout = 0.1

warmup_iters = 100
decay_lr = True
learning_rate = 1e-4
decay_rate = 0.995405
decay_iters = 500

device = 'mps'
compile = False # do not torch compile the model
