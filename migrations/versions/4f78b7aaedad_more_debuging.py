"""more debuging

Revision ID: 4f78b7aaedad
Revises: e3b3ff83ee53
Create Date: 2024-01-18 15:14:10.339324

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4f78b7aaedad'
down_revision = 'e3b3ff83ee53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
                    sa.Column('password_hash', sa.VARCHAR(length=200), nullable=True),
                    sa.Column('last_name', sa.VARCHAR(length=100), nullable=True),
                    sa.Column('drug_testing_phone', sa.VARCHAR(length=20), nullable=True),
                    sa.Column('ivr_code', sa.VARCHAR(length=20), nullable=True),
                    sa.Column('mobile_number1', sa.VARCHAR(length=20), nullable=True),
                    sa.Column('mobile_number2', sa.VARCHAR(length=20), nullable=True),
                    sa.Column('checkin_time', sa.TIME(), nullable=True),
                    sa.Column('days_of_week', sa.VARCHAR(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    # ### end Alembic commands ###