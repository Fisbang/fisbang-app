"""empty message

Revision ID: 51a997b778b
Revises: 118a2d438805
Create Date: 2015-05-14 15:26:29.933670

"""

# revision identifiers, used by Alembic.
revision = '51a997b778b'
down_revision = '118a2d438805'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('environment_sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('environment_id', sa.Integer(), nullable=True),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['environment_id'], ['environment.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('device_sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sensor_data')
    op.add_column(u'sensor', sa.Column('key', sa.String(length=80), nullable=True))
    op.drop_constraint(u'sensor_environment_id_fkey', 'sensor', type_='foreignkey')
    op.drop_constraint(u'sensor_user_id_fkey', 'sensor', type_='foreignkey')
    op.drop_constraint(u'sensor_device_id_fkey', 'sensor', type_='foreignkey')
    op.drop_column(u'sensor', 'environment_id')
    op.drop_column(u'sensor', 'user_id')
    op.drop_column(u'sensor', 'device_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'sensor', sa.Column('device_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'sensor', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'sensor', sa.Column('environment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'sensor_device_id_fkey', 'sensor', 'device', ['device_id'], ['id'])
    op.create_foreign_key(u'sensor_user_id_fkey', 'sensor', 'user', ['user_id'], ['id'])
    op.create_foreign_key(u'sensor_environment_id_fkey', 'sensor', 'environment', ['environment_id'], ['id'])
    op.drop_column(u'sensor', 'key')
    op.create_table('sensor_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('value', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('sensor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], [u'sensor.id'], name=u'sensor_data_sensor_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'sensor_data_pkey')
    )
    op.drop_table('device_sensor')
    op.drop_table('environment_sensor')
    ### end Alembic commands ###
