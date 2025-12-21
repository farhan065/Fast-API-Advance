"""Foreign key constraint on post table

Revision ID: f5a57fbbb2ce
Revises: 60edbd3de9f6
Create Date: 2025-12-19 14:40:35.001573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5a57fbbb2ce'
down_revision: Union[str, Sequence[str], None] = '60edbd3de9f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts_alembic', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_alembic_users_fk', source_table='posts_alembic', referent_table='users_alembic',
                            local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
