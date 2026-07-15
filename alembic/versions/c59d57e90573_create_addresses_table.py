"""Create addresses Table

Revision ID: c59d57e90573
Revises: 3a81b802007e
Create Date: 2026-07-15 09:12:58.432675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c59d57e90573'
down_revision: Union[str, Sequence[str], None] = '3a81b802007e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "addresses",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey(
                "users.id",
                ondelete="CASCADE",
            ),
            nullable=False,
            unique=True,
        ),
        sa.Column(
            "province_code",
            sa.String(100),
            nullable=False,
        ),
        sa.Column(
            "province_name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "regency_code",
            sa.String(100),
            nullable=False,
        ),
        sa.Column(
            "regency_name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "subdistrict_code",
            sa.String(100),
            nullable=False,
        ),
        sa.Column(
            "subdistrict_name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "village_code",
            sa.String(100),
            nullable=False,
        ),
        sa.Column(
            "village_name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "full_address",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "postal_code",
            sa.String(5),
            nullable=True,
        ),
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


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("addresses")
