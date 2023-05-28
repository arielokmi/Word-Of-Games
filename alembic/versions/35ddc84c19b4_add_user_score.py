"""add_user_score

Revision ID: 35ddc84c19b4
Revises: 
Create Date: 2023-05-24 18:12:17.439888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ddc84c19b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users_score',
        sa.Column('score', sa.INTEGER),
    )

def downgrade():
    op.drop_table('users_score')

