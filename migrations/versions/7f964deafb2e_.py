"""empty message

Revision ID: 7f964deafb2e
Revises: 309b1f2d42c4
Create Date: 2017-09-24 14:38:12.902346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f964deafb2e'
down_revision = '309b1f2d42c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_info_ibfk_1', 'user_info', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('user_info_ibfk_1', 'user_info', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###