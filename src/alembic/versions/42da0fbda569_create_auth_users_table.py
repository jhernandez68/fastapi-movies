"""create auth_users table

Revision ID: 42da0fbda569
Revises: 
Create Date: 2025-05-08 17:53:23.188756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42da0fbda569'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'auth_users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('auth_users')