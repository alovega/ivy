# local
import ivy
from ivy.func_wrapper import with_unsupported_dtypes

from ivy.functional.frontends.torch.func_wrapper import to_ivy_arrays_and_back


@to_ivy_arrays_and_back
@with_unsupported_dtypes({"2.0.1 and below": ("float16",)}, "torch")
def dropout(input, p=0.5, training=True, inplace=False):
    return ivy.dropout(input, p, training=training)


@to_ivy_arrays_and_back
@with_unsupported_dtypes({"2.0.1 and below": ("float16",)}, "torch")
def dropout1d(input, p=0.5, training=True, inplace=False):
    if inplace:
        return ivy.dropout1d(input, p, training=training, data_format="NCW", out=input)
    return ivy.dropout1d(input, p, training=training, data_format="NCW")
