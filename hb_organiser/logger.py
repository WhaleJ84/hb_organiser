"""
Builds the logger to be shared across the project.
"""
import logging

from hb_organiser.config import Config

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=f"{Config.PROJECT_ROOT}/hb_organiser.log",
    level=logging.DEBUG
)
