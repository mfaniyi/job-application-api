"""create vacancy and applicant tables

Revision ID: 667397876cf0
Revises:
Create Date: 2026-08-23 22:15:42.518998

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "667397876cf0"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create vacancy and applicant tables."""

    op.create_table(
        "vacancy",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=1000), nullable=False),
    )

    op.create_table(
        "applicant",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("vacancy_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["vacancy_id"],
            ["vacancy.id"],
        ),
    )


def downgrade() -> None:
    """Remove vacancy and applicant tables."""

    op.drop_table("applicant")
    op.drop_table("vacancy")