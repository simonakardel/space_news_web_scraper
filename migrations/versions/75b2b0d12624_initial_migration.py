"""Initial migration.

Revision ID: 75b2b0d12624
Revises: 
Create Date: 2024-06-24 10:25:09.655611

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '75b2b0d12624'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('link', sa.VARCHAR(length=255), nullable=True),
    sa.Column('summary', sa.TEXT(), nullable=True),
    sa.Column('full_article', sa.TEXT(), nullable=True),
    sa.Column('image_url', sa.VARCHAR(length=255), nullable=True),
    sa.Column('date_scraped', sa.DATE(), nullable=True),
    sa.Column('categories', sqlite.JSON(), nullable=True),
    sa.Column('source', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###
