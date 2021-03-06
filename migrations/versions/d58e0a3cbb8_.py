"""empty message

Revision ID: d58e0a3cbb8
Revises: 51a997b778b
Create Date: 2015-05-16 21:29:16.675241

"""

# revision identifiers, used by Alembic.
revision = 'd58e0a3cbb8'
down_revision = '51a997b778b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensor', 'key')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sensor', sa.Column('key', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    ### end Alembic commands ###
