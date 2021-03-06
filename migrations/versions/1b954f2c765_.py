"""empty message

Revision ID: 1b954f2c765
Revises: 544d12672a15
Create Date: 2015-02-05 21:54:16.302755

"""

# revision identifiers, used by Alembic.
revision = '1b954f2c765'
down_revision = '5745e5e728bf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_budget',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('project_category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('skills', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.Column('project_budget_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_budget_id'], ['project_budget.id'], ),
    sa.ForeignKeyConstraint(['project_category_id'], ['project_category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('project_budget')
    op.drop_table('project_category')
    ### end Alembic commands ###
