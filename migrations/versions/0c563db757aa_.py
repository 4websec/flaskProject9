"""empty message

Revision ID: 0c563db757aa
Revises: 4f78b7aaedad
Create Date: 2024-01-20 02:47:15.172226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c563db757aa'
down_revision = '4f78b7aaedad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('drug_testing_phone', sa.String(length=20), nullable=True),
    sa.Column('ivr_code', sa.String(length=20), nullable=True),
    sa.Column('mobile_number1', sa.String(length=20), nullable=True),
    sa.Column('mobile_number2', sa.String(length=20), nullable=True),
    sa.Column('checkin_time', sa.Time(), nullable=True),
    sa.Column('days_of_week', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
