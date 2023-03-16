"""add forgn key to our post table

Revision ID: 0444f41f5185
Revises: 4fd01eed41e0
Create Date: 2023-03-14 16:10:51.816894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0444f41f5185'
down_revision = '4fd01eed41e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable= False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
