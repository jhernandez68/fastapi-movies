"""create movies table

Revision ID: 98e25aaad2f9
Revises: d8e1535a242f
Create Date: 2025-05-08 17:53:24.285171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98e25aaad2f9'
down_revision: Union[str, None] = 'd8e1535a242f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'movies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('release_date', sa.String, nullable=False),
        sa.Column('genre_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], name='movies_genre_id_fk', ondelete='CASCADE')
    )


def downgrade() -> None:
    op.drop_table('movies')