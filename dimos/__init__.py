"""dimos — a fork of dimensionalOS/dimos.

A framework for building dimensional, agent-based robotic systems
with reactive pipelines and multimodal capabilities.
"""

__version__ = "0.1.0"
__author__ = "dimos contributors"
__license__ = "Apache-2.0"

from dimos.utils.logging import get_logger

logger = get_logger(__name__)

__all__ = [
    "__version__",
    "__author__",
    "__license__",
]
