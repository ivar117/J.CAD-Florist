"""company information table

Revision ID: 5d32adab9400
Revises: 
Create Date: 2024-10-11 15:49:43.618589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d32adab9400'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyPhoneNumber', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('company_information', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_company_information_companyPhoneNumber'), ['companyPhoneNumber'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company_information', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_company_information_companyPhoneNumber'))

    op.drop_table('company_information')
    # ### end Alembic commands ###
