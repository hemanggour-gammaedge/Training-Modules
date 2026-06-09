from app.database import Base
from app.database import engine


# Create tables automatically
# In production use Alembic.
Base.metadata.create_all(bind=engine)
