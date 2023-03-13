"""Init

Revision ID: 9e4a6bf6b801
Revises: 
Create Date: 2023-03-13 11:53:03.689120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e4a6bf6b801'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('artist', sa.String(length=255), nullable=False),
    sa.Column('album', sa.String(length=255), nullable=False),
    sa.Column('relase_date', sa.Date(), nullable=False),
    sa.Column('genre', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    # ### end Alembic commands ###
