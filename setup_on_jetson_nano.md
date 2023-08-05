# Setup on Jetson Nano

- for inference with small models, only

# Steps

1. Start with the [Ubuntu 18.04 image by NVIDIA](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write).

2. Do the initial setup and enable SSH.

3. Upgrade to Ubuntu 20.04 ([instructions](https://qengineering.eu/install-ubuntu-20.04-on-jetson-nano.html)).

4. Install Rust (later needed to compile the package `tiktoken`).

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

5. Install poetry.

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

6. Add this to ~/.bashrc

```shell
PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
```

6. Create the environment with poetry

```shell
poetry install
```
