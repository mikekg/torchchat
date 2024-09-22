
import torch
import torch.nn as nn

from transformers import AutoModelForCausalLM # , AutoTokenizer, pipeline
from torchchat.model import TransformerArgs

def model_builder(builder_args) -> nn.Module:
    torch.random.manual_seed(0)
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map="cuda",
        torch_dtype="auto",
        trust_remote_code=True,
    )

    # let's get a default config SentencePiece
    # PS: SentencePiece is the default, but we assert it in the constructor for documentation
    model.config = TransformerArgs(use_tiktoken=False)
    print(model)

    return model


