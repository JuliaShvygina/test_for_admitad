from sqlalchemy import Column, String, Integer, DateTime

from services import datasource


class Order(datasource.Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    client_id = Column(String(10))
    date = Column(DateTime)
    source = Column(String)

    def __init__(
            self,
            date: str,
            client_id: str,
            source: str
    ) -> None:
        self.date = date
        self.client_id = client_id
        self.source = source
