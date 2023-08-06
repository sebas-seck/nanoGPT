out_dir = 'out-bundestag/31'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'bundestag'
wandb_run_name = 'tune-bt-gpt2-medium-ex31'

dataset = 'bundestag'
init_from = 'gpt2-medium' # this is the second smallest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 400

decay_lr = True
learning_rate = 0.1
decay_rate = 0.975
decay_iters = 300

device = 'mps'
compile = False # do not torch compile the model
