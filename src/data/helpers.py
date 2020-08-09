import logging

logging.basicConfig(
    format="ts :%(asctime)s, module %(module)s, lineno : %(lineno)d, message: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

logger.info("making final data set from raw data")

file_name = "data/raw/housing.csv"
print(file_name)
