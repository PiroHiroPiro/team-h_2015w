"""empty message

Revision ID: cb1748f5bace
Revises: None
Create Date: 2016-02-24 16:24:13.581017

"""

# revision identifiers, used by Alembic.
revision = 'cb1748f5bace'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=512), nullable=True),
    sa.Column('tag', sa.String(length=32), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('published_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('article')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=512), nullable=True),
    sa.Column('body', sa.TEXT(), nullable=True),
    sa.Column('published_on', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post')
    ### end Alembic commands ###