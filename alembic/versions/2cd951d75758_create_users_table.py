"""Create users Table

Revision ID: 2cd951d75758
Revises: d7fb9e878f3f
Create Date: 2026-07-15 09:11:03.085838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '2cd951d75758'
down_revision: Union[str, Sequence[str], None] = 'd7fb9e878f3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("email", sa.String(100), nullable=False, unique=True, index=True),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )
    
    op.create_index(
        "ix_email",
        "users",
        ["email"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        "ix_email",
        table_name="users",
    )
    op.drop_table("users")
