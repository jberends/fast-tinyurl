"""empty message

Revision ID: d28eba89a9a5
Revises: 
Create Date: 2021-04-05 15:26:02.942452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd28eba89a9a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shortened_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('utcnow()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('long', sa.Unicode(length=24576), nullable=True),
    sa.Column('short', sa.Unicode(length=64), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('is_active')
    )
    op.create_index(op.f('ix_shortened_urls_id'), 'shortened_urls', ['id'], unique=False)
    op.create_index(op.f('ix_shortened_urls_short'), 'shortened_urls', ['short'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shortened_urls_short'), table_name='shortened_urls')
    op.drop_index(op.f('ix_shortened_urls_id'), table_name='shortened_urls')
    op.drop_table('shortened_urls')
    # ### end Alembic commands ###
