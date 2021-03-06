"""add second half and massage

Revision ID: b6fc61cb4ddf
Revises: 9937159f8e8c
Create Date: 2020-04-26 11:04:27.824731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6fc61cb4ddf'
down_revision = '9937159f8e8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('message', sa.String(length=300), nullable=True))
    op.add_column('game', sa.Column('secondhalf', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'secondhalf')
    op.drop_column('game', 'message')
    # ### end Alembic commands ###
