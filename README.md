# LLM Code Documentation Generator

`llmdocgen` is a library for automatically documenting code using large language models (LLMs). It takes code files as
input, sends them to an LLM to generate documentation comments, and returns the code with the generated documentation
added.

## Features

- Automatically documents code using LLMs
- Supports a wide variety of programming languages out of the box
- Easily configurable to add support for additional file types
- Can be used as a library or run as a command line tool
- Integrates with [LiteLLM](https://docs.litellm.ai) to work with OpenAI, Anthropic, and other LLM providers

## Installation

Install from PyPI using pip:

```bash
pip install llmdocgen
```

## Setup

`llmdocgen` requires a few environment variables to be set in order to authenticate with the LLM provider. The easiest
way to set these variables is to create a ~/.llmdocgen file with the following variables:

```bash
# Required for LiteLLM
LITELLM_MODEL=claude-3-opus-20240229  # or another supported model
LITELLM_API_BASE=https://api.litellm.ai

# Optional LiteLLM settings
LITELLM_TIMEOUT=60
LITELLM_TEMPERATURE=0
# See settings.py for additional optional variables

# llmdocgen settings
PROMPT_FILE=default_prompt.txt
ESCAPE_CHARACTERS=%"%"%"
```

See the LiteLLM docs for more details on authenticating.

## Usage

There are two main ways to use llmdocgen:

### As a library

```python
from llmdocgen import enrich

completion = enrich.get_file_completion(file_path)
print(completion)
```

This will print out the code from file_path with documentation comments added.

### As a command line tool

You can also run llmdocgen as a module:

```bash
python -m llmdocgen /path/to/directory --recursive
```

This will process all supported files in /path/to/directory. Pass --recursive to also process subdirectories.

## Configuration

### Supported File Types

By default, llmdocgen supports a wide variety of file types (see settings.DEFAULT_EXTENSIONS). You can add additional
file types by setting the llmdocgen_EXTRA_EXTENSIONS environment variable to a comma-separated list of extensions.
To override the default list entirely, set the llmdocgen_EXTENSIONS environment variable.

### Prompts

`llmdocgen` uses a prompt defined in default_prompt.txt to instruct the LLM on how to generate the documentation. You can
modify this prompt or provide a different file by setting the PROMPT_FILE environment variable.
The prompt should include %"%"% where the generated code should be inserted. llmdocgen will use this to extract the
generated code from the LLM's response.

### Authenticating with LLMs

As mentioned above, `llmdocgen` uses LiteLLM to integrate with LLM providers. All authentication happens through LiteLLM
by setting the appropriate environment variables.
See settings.LITELLM for the full list of supported settings. These map directly to arguments to LiteLLM's
litellm.completion() function.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the GitHub repository.

## License

`llmdocgen` is released under the MIT License. See [LICENSE](LICENSE) for more information.
