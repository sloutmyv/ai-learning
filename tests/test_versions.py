import importlib.metadata as md

def test_torch_version():
    major, minor, *_ = map(int, md.version("torch").split("."))
    assert (major, minor) >= (2, 2), "Torch >= 2.2.x requis"
