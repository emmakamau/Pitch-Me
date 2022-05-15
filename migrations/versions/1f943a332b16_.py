"""empty message

Revision ID: 1f943a332b16
Revises: e2b3a6bd9aac
Create Date: 2022-05-11 19:53:31.262614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f943a332b16'
down_revision = 'e2b3a6bd9aac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_category_name', table_name='category')
    op.drop_table('category')
    op.add_column('pitch', sa.Column('category', sa.String(), nullable=True))
    op.drop_constraint('pitch_category_id_fkey', 'pitch', type_='foreignkey')
    op.drop_column('pitch', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitch_category_id_fkey', 'pitch', 'category', ['category_id'], ['id'])
    op.drop_column('pitch', 'category')
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    op.create_index('ix_category_name', 'category', ['name'], unique=False)
    # ### end Alembic commands ###
