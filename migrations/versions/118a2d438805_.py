"""empty message

Revision ID: 118a2d438805
Revises: 4eb1efd14c83
Create Date: 2015-04-25 13:30:46.035679

"""

# revision identifiers, used by Alembic.
revision = '118a2d438805'
down_revision = '4eb1efd14c83'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('environment', sa.Column('name', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('environment', 'name')
    ### end Alembic commands ###
