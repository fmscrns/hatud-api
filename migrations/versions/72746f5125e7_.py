"""empty message

Revision ID: 72746f5125e7
Revises: 787829950859
Create Date: 2020-04-24 01:05:13.176231

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '72746f5125e7'
down_revision = '787829950859'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('contact_no', sa.String(length=20), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('email', table_name='user')
    op.drop_index('public_id', table_name='user')
    op.drop_index('username', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('registered_on', mysql.DATETIME(), nullable=False),
    sa.Column('admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('public_id', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'user', ['username'], unique=True)
    op.create_index('public_id', 'user', ['public_id'], unique=True)
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_table('customer')
    # ### end Alembic commands ###
