from .main import Core
import os


__all__ = ["Core"]

__version__ = os.getenv("GITHUB_REF_NAME", "latest")
