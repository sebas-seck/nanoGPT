out_dir = 'out-shakespeare/23'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'shakespeare'
wandb_run_name = 'tune-sp-gpt2-medium-ex23'

dataset = 'shakespeare'
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
learning_rate = 1e-3
decay_rate = 0.98262
decay_iters = 200

device = 'mps'
compile = False # do not torch compile the model
