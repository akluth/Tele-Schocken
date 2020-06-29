"""add changs_of_fallling_dice to statistic remove secondhalf

Revision ID: e3ac3f6ecd4c
Revises: 18f13a149bea
Create Date: 2020-06-29 19:51:04.312535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e3ac3f6ecd4c'
down_revision = '18f13a149bea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'secondhalf')
    op.add_column('statistic', sa.Column('changs_of_fallling_dice', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('statistic', 'changs_of_fallling_dice')
    op.add_column('game', sa.Column('secondhalf', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
