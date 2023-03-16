"""create users table

Revision ID: 4fd01eed41e0
Revises: 3b38ee2af733
Create Date: 2023-03-14 15:22:59.094758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd01eed41e0'
down_revision = '3b38ee2af733'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), nullable= False),
                    sa.Column("email", sa.String(), nullable= False),
                    sa.Column("password", sa.String(), nullable= False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default= sa.text("now()"), nullable= False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
