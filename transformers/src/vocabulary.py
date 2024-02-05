"""Implement the token and sentence embedder"""
from torch import nn


class SelfAttentionMain(nn.Module):
    """A multi attention implementation

    Args:
        nn (_type_): _description_
    """
    def __init__(self, emb, heads=8, mask=False, kqnorm=False):
        """_summary_

        Args:
            emb (_type_): _description_
            heads (int, optional): _description_. Defaults to 8.
            mask (bool, optional): _description_. Defaults to False.
            kqnorm (bool, optional): _description_. Defaults to False.
        """