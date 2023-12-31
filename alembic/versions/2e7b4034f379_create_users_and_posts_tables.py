"""create users and posts tables

Revision ID: 2e7b4034f379
Revises: 
Create Date: 2023-06-20 11:02:04.534492

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = '2e7b4034f379'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE EXTENSION IF NOT EXISTS timescaledb")
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='true', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('weather_source',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POLYGON', from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('location_name', sa.String(length=128), nullable=False),
    sa.Column('source_name', sa.String(length=48), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    #op.create_index('idx_weather_source_location', 'weather_source', ['location'], unique=False, postgresql_using='gist')
    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_index('idx_weather_source_location', table_name='weather_source', postgresql_using='gist')
    op.drop_table('weather_source')
    op.drop_table('users')
    # ### end Alembic commands ###
