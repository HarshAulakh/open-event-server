"""empty message

Revision ID: 4cac94c86047
Revises: 5b9f83cede65
Create Date: 2018-05-02 19:59:47.823228

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '4cac94c86047'
down_revision = '5b9f83cede65'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    ticket_holders_table = sa.sql.table('ticket_holders',
                                        sa.Column('lastname', sa.VARCHAR()))

    op.execute(ticket_holders_table.update()
               .where(ticket_holders_table.c.lastname.is_(None))
               .values({'lastname': op.inline_literal(' ')}))

    op.alter_column('ticket_holders', 'lastname',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ticket_holders', 'lastname',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    # ### end Alembic commands ###
