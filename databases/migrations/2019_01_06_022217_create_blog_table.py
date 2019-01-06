from orator.migrations import Migration


class CreateBlogTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('blogs') as table:
            table.increments('id')
            table.string('title')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.string('body')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('blogs')
