"""init migration

Revision ID: 72f7d1098e2e
Revises: 731276e42dda
Create Date: 2023-06-25 02:46:21.477856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72f7d1098e2e'
down_revision = '731276e42dda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)

    # ### end Alembic commands ###
