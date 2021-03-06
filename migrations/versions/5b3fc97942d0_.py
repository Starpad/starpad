"""empty message

Revision ID: 5b3fc97942d0
Revises: 
Create Date: 2021-02-27 16:44:05.419722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b3fc97942d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('categories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('categories_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('type', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='categories_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('questions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('difficulty', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('category', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category'], ['categories.id'], name='category', onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='questions_pkey')
    )
    # ### end Alembic commands ###
