"""add column content to table posts

Revision ID: 3b38ee2af733
Revises: 2a79cbc11513
Create Date: 2023-03-14 15:15:47.426792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b38ee2af733'
down_revision = '2a79cbc11513'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
