out_dir = 'out-bundestag-ger/36'
eval_interval = 5
eval_iters = 40
wandb_log = True
wandb_project = 'bundestag-ger'
wandb_run_name = 'tune-bt-ger-gpt2-ex36'

dataset = 'bundestag_ger'
init_from = 'ger-gpt2' # this is comparable to the smallest GPT-2 model

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
