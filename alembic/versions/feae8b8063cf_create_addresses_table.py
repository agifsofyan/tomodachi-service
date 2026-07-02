"""create addresses_table

Revision ID: feae8b8063cf
Revises: 51345ebf2e1d
Create Date: 2026-07-02 15:41:56.966640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'feae8b8063cf'
down_revision: Union[str, Sequence[str], None] = '51345ebf2e1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "addresses",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey(
                "users.id",
                ondelete="CASCADE",
            ),
            nullable=False,
        ),
        sa.Column(
            "province_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "province_name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "regency_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "regency_name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "subdistrict_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "subdistrict_name",
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
