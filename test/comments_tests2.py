import unittest
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.comments_database import Base
from routes.comments_routes import Comment, create_comment, get_comment, get_comments, update_comment, delete_comment

DATABASE_URL = "sqlite:///:memory:"

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.db = self.Session()
        self.comments_to_delete = []

    def tearDown(self):
        loop = asyncio.get_event_loop()
        tasks = [delete_comment(comment_id, self.db) for comment_id in self.comments_to_delete]
        loop.run_until_complete(asyncio.gather(*tasks))
        self.db.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    async def test_create_comment(self):
        comment = await create_comment("This is a test comment", self.db)
        self.assertIsNotNone(comment.id)
        self.assertEqual(comment.content, "This is a test comment")
        self.comments_to_delete.append(comment.id)

    async def test_get_comment(self):
        comment = await create_comment("This is a test comment", self.db)
        self.comments_to_delete.append(comment.id)
        fetched_comment = await get_comment(comment.id, self.db)
        self.assertEqual(fetched_comment.id, comment.id)
        self.assertEqual(fetched_comment.content, comment.content)

    async def test_get_comments(self):
        comment1 = await create_comment("Comment 1", self.db)
        comment2 = await create_comment("Comment 2", self.db)
        self.comments_to_delete.append(comment1.id)
        self.comments_to_delete.append(comment2.id)
        comments = await get_comments(db_session=self.db)
        self.assertEqual(len(comments), 2)
        self.assertEqual(comments[0].content, "Comment 1")
        self.assertEqual(comments[1].content, "Comment 2")

    async def test_update_comment(self):
        comment = await create_comment("Original Comment", self.db)
        self.comments_to_delete.append(comment.id)
        updated_comment = await update_comment(comment.id, "Updated Comment", self.db)
        self.assertEqual(updated_comment.content, "Updated Comment")

    async def test_delete_comment(self):
        comment = await create_comment("Comment to be deleted", self.db)
        delete_success = await delete_comment(comment.id, self.db)
        self.assertTrue(delete_success)
        deleted_comment = await get_comment(comment.id, self.db)
        self.assertIsNone(deleted_comment)

if __name__ == '__main__':
    unittest.main()

