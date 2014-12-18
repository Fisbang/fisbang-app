"""empty message

Revision ID: 15d1e5037bba
Revises: 2fd34dfdef46
Create Date: 2014-12-10 00:08:39.777025

"""

# revision identifiers, used by Alembic.
revision = '15d1e5037bba'
down_revision = '2fd34dfdef46'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices_sensors',
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('devices_sensors')
    op.drop_table('device')
    ### end Alembic commands ###