"""title column  is adding at the post_alembic table

Revision ID: 0ccb502e959d
Revises: 08e67d71180e
Create Date: 2025-12-19 14:17:25.165874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ccb502e959d'
down_revision: Union[str, Sequence[str], None] = '08e67d71180e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts_alembic', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts_alembic', 'content')
    pass
