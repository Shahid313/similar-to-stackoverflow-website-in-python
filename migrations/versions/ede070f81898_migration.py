"""migration

Revision ID: ede070f81898
Revises: 
Create Date: 2021-07-10 10:51:27.405263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ede070f81898'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=55), nullable=False),
    sa.Column('email', sa.String(length=55), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('user_image', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('post_title', sa.String(length=250), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('post_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('replies',
    sa.Column('reply_id', sa.Integer(), nullable=False),
    sa.Column('reply_body', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('reply_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('replies')
    op.drop_table('posts')
    op.drop_table('user')
    # ### end Alembic commands ###
