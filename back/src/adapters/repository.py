from sqlalchemy.orm import Session

class AbstractSQLAlchemyRepository():
    def __init__(self, session: Session):
        self.session = session