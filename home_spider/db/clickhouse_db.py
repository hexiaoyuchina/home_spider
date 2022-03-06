import logging

from clickhouse_driver import Client

logger = logging.getLogger(__name__)


class ConnectClickhouse:

    def __init__(self, host=None, database=None, user=None, password=None, port=9000):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

        self.client = None

    def connection(self):
        """
        连接
        :return:
        """
        try:
            client = Client(host=self.host,
                            port=self.port,
                            database=self.database,
                            user=self.user,
                            password=self.password)
            self.client = client
            return client
        except Exception as e:
            logger.error(f"connect clickhouse error {e}", exc_info=True)
            raise e

    def close(self):
        if self.client is not None:
            try:
                logger.info(f"start close clickhouse client")
                self.client.disconnect()
            except Exception as e:
                logger.error(f"disconnect clickhouse error {e}", exc_info=True)

        self.client = None
        logger.info(f"close clickhouse client success")

    def execute(self, query, params=None):
        """
        查询
        :param sql:
        :return:
        """
        if self.client is None:
            self.connection()
        logger.info(f"start get client execute query: {query}, params {params}")
        res = self.client.execute(query, params)
        return res

