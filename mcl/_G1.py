import types
import ctypes

from . import utils
from . import builder
from ._Fp import Fp
from ._Fr import Fr

BUFFER_SIZE = 2048


class G1(ctypes.Structure):
    _fields_ = [
        ("x", Fp),
        ("y", Fp),
        ("z", Fp),
    ]


G1.__add__ = builder.buildThreeOp(G1, "add")
G1.__eq__ = builder.buildIsEqual(G1)
G1.__mul__ = builder.buildMul(G1, Fr)
G1.__neg__ = builder.buildTwoOp(G1, "neg")
G1.__sub__ = builder.buildThreeOp(G1, "sub")
G1.deserialize = builder.buildDeserialize(G1)
G1.getStr = builder.buildGetStr(G1)
G1.hashAndMapTo = builder.buildHashAndMapTo(G1)
G1.isZero = builder.buildIsZero(G1)
G1.serialize = builder.buildSerialize(G1)
G1.setStr = builder.buildSetStr(G1)
