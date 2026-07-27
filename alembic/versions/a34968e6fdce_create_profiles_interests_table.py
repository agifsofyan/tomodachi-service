"""Create profiles_interests Table

Revision ID: a34968e6fdce
Revises: e4a2e37f011b
Create Date: 2026-07-15 09:14:33.799935

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a34968e6fdce"
down_revision: str | Sequence[str] | None = "e4a2e37f011b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "profiles_interests",
        sa.Column(
            "profile_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey(
                "profiles.id",
                ondelete="CASCADE",
            ),
            nullable=False,
        ),
        sa.Column(
            "interest_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey(
                "interests.id",
                ondelete="CASCADE",
            ),
            nullable=False,
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
        sa.PrimaryKeyConstraint(
            "profile_id",
            "interest_id",
            name="pk_profiles_interests",
        ),
    )

    op.create_index(
        "ix_profiles_interests_profile_id",
        "profiles_interests",
        ["profile_id"],
    )

    op.create_index(
        "ix_profiles_interests_interest_id",
        "profiles_interests",
        ["interest_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        "ix_profiles_interests_profile_id",
        table_name="profiles_interests",
    )

    op.drop_index(
        "ix_profiles_interests_interest_id",
        table_name="profiles_interests",
    )

    op.drop_table("profiles_interests")
