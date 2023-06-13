"""add votes

Revision ID: 31843afc85a1
Revises: 2aa79f6147eb
Create Date: 2023-06-13 21:55:32.269265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31843afc85a1'
down_revision = '2aa79f6147eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('votes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'votes')
    # ### end Alembic commands ###