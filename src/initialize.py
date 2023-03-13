import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from core.config import settings
from core.connection import create_mongo_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        client = create_mongo_client()
        response = client[settings.DATABASE_NAME].command("ping")
        logger.info(f"Got response from ping: {response}")
        if not response.get("ok"):
            raise ConnectionError
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
