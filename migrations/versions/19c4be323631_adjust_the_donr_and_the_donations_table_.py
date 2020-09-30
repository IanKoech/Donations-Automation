""" adjust the donr and the donations table to arter for the donor anonimity

Revision ID: 19c4be323631
Revises: fd2a02e872f3
Create Date: 2020-09-30 02:47:32.258792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19c4be323631'
down_revision = 'fd2a02e872f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donations', sa.Column('donorAnonimity', sa.Boolean(), nullable=True))
    op.drop_column('donors', 'charities')
    op.drop_column('donors', 'anonymity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donors', sa.Column('anonymity', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('donors', sa.Column('charities', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('donations', 'donorAnonimity')
    # ### end Alembic commands ###