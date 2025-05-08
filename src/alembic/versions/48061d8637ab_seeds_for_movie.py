from sqlalchemy import table
"""seeds for movie

Revision ID: 48061d8637ab
Revises: 1487e3f8134d
Create Date: 2025-05-08 17:53:25.421373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48061d8637ab'
down_revision: Union[str, None] = '1487e3f8134d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    movie_table = table('movies',
        sa.Column('id', sa.Integer),
        sa.Column('title', sa.String),
        sa.Column('release_date', sa.String),
        sa.Column('genre_id', sa.Integer)
    )
    op.bulk_insert(movie_table, [{'id': 1, 'title': 'The Great Escape', 'release_date': '1963-07-04', 'genre_id': 1}])
    op.bulk_insert(movie_table, [{'id': 2, 'title': 'Life Is Beautiful', 'release_date': '1997-12-20', 'genre_id': 3}])
    op.bulk_insert(movie_table, [{'id': 3, 'title': 'Airplane!', 'release_date': '1980-07-02', 'genre_id': 2}])


def downgrade() -> None:
    op.execute('DELETE FROM movies')