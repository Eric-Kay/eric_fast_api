"""add remaining rows to post table

Revision ID: 23f3a47eade3
Revises: 0444f41f5185
Create Date: 2023-03-14 16:19:54.271660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23f3a47eade3'
down_revision = '0444f41f5185'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column("published", sa.Boolean(), nullable= False, server_default= 'TRUE'))
    op.add_column('posts',sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default= sa.text("now()"), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
