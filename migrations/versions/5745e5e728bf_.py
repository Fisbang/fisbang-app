"""empty message

Revision ID: 5745e5e728bf
Revises: 1175e9afec06
Create Date: 2014-12-16 08:18:02.453686

"""

# revision identifiers, used by Alembic.
revision = '5745e5e728bf'
down_revision = '1175e9afec06'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=80), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    ### end Alembic commands ###
