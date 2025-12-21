"""users_alembic table is created

Revision ID: 60edbd3de9f6
Revises: 0ccb502e959d
Create Date: 2025-12-19 14:37:39.165766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60edbd3de9f6'
down_revision: Union[str, Sequence[str], None] = '0ccb502e959d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users_alembic',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('date', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
