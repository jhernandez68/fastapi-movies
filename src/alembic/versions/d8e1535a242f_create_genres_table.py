"""create genres table

Revision ID: d8e1535a242f
Revises: 42da0fbda569
Create Date: 2025-05-08 17:53:23.753557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8e1535a242f'
down_revision: Union[str, None] = '42da0fbda569'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'genres',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('genres')