from sqlalchemy import table
"""seeds for genre

Revision ID: 1487e3f8134d
Revises: 98e25aaad2f9
Create Date: 2025-05-08 17:53:24.883013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1487e3f8134d'
down_revision: Union[str, None] = '98e25aaad2f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    genre_table = table('genres',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String)
    )
    op.bulk_insert(genre_table, [{'id': 1, 'name': 'Action'}])
    op.bulk_insert(genre_table, [{'id': 2, 'name': 'Comedy'}])
    op.bulk_insert(genre_table, [{'id': 3, 'name': 'Drama'}])


def downgrade() -> None:
    op.execute('DELETE FROM genres')