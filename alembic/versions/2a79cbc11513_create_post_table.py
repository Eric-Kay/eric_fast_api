"""create post table

Revision ID: 2a79cbc11513
Revises: 
Create Date: 2023-03-14 15:06:56.024524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a79cbc11513'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id",sa.Integer(), nullable= False, primary_key= True ), sa.Column("title", sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
