"""empty message

Revision ID: 301ff2e1e331
Revises: f57b627352c9
Create Date: 2023-04-05 13:57:45.547981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301ff2e1e331'
down_revision = 'f57b627352c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.add_column(sa.Column('run_time', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.drop_column('run_time')

    # ### end Alembic commands ###
