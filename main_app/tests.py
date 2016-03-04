"""The tests module."""

import datetime

from django.test import TestCase

from main_app import models as app_models
from django.contrib.auth import models as auth_models
from django.core.exceptions import ObjectDoesNotExist


# Mock Data
USERNAME = "Dummy User"
TODO_LIST_TITLE = "Dummy TODOList"
TODO_LIST_UPDATED_TITLE = "UPDATED Dummy TODOList"
TASK_DESCRIPTION = "Dummy Task"
TASK_UPDATED_DESCRIPTION = "UPDATED Dummy Task"
TASK_DEADLINE = datetime.datetime.now() + datetime.timedelta(days=1)
TASK_UPDATED_DEADLINE = datetime.datetime.now() + datetime.timedelta(days=2)
TASK_DONE = False
TASK_UPDATED_DONE = True
COMMENT_TEXT = "Dummy Comment"
COMMENT_UPDATED_TEXT = "UPDATED Dummy Comment"


class FullCleanupTest(TestCase):

    def setUp(self):

        # delete all objects directly
        app_models.TODOList.objects.all().delete()
        app_models.Task.objects.all().delete()
        app_models.Comment.objects.all().delete()
        auth_models.User.objects.all().delete()

    def tearDown(self):

        # delete all objects directly
        app_models.TODOList.objects.all().delete()
        app_models.Task.objects.all().delete()
        app_models.Comment.objects.all().delete()
        auth_models.User.objects.all().delete()


class TODOListFullCleanupTest(FullCleanupTest):

    def test_create(self):

        """Creating a TODOList"""

        app_models.TODOList.objects.create(title=TODO_LIST_TITLE)

        self.assertIsNotNone(app_models.TODOList.objects.get(title=TODO_LIST_TITLE),
                             "The TODOList was not created correctly")

    def test_update_title(self):

        """Updating the TODOList title"""

        app_models.TODOList.objects.create(title=TODO_LIST_TITLE)
        todo_list = app_models.TODOList.objects.get(title=TODO_LIST_TITLE)

        todo_list.title = TODO_LIST_UPDATED_TITLE
        todo_list.save()

        updated_list = app_models.TODOList.objects.get(title=TODO_LIST_UPDATED_TITLE)

        self.assertEquals(todo_list.pk, updated_list.pk,
                          "The TODOList was not updated correctly")

    def test_delete(self):

        """Deleting a TODOList"""

        app_models.TODOList.objects.create(title=TODO_LIST_TITLE)
        app_models.TODOList.objects.get(title=TODO_LIST_TITLE).delete()

        self.assertRaises(ObjectDoesNotExist,                   # exception
                          app_models.TODOList.objects.get,      # method to call
                          title=TODO_LIST_TITLE)                # arg to method


class TaskFullCleanupTest(FullCleanupTest):

    def test_create1(self):

        """Creating a Task, with description"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION)

        self.assertIsNotNone(app_models.Task.objects.get(description=TASK_DESCRIPTION),
                             "The Task was not created correctly")

    def test_create2(self):

        """Creating a Task, with description and deadline"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)

        self.assertIsNotNone(app_models.Task.objects.get(description=TASK_DESCRIPTION,
                                                         deadline=TASK_DEADLINE),
                             "The Task was not created correctly")

    def test_update1(self):

        """Creating a Task, with description. Then updating its description"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION)
        task = app_models.Task.objects.get(description=TASK_DESCRIPTION)

        task.description = TASK_UPDATED_DESCRIPTION
        task.save()

        updated_task = app_models.Task.objects.get(description=TASK_UPDATED_DESCRIPTION)

        self.assertEquals(task.pk, updated_task.pk,
                          "The Task was not updated correctly")

    def test_update2(self):

        """Creating a Task, with description. Then updating its deadline"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION)
        task = app_models.Task.objects.get(description=TASK_DESCRIPTION)

        task.deadline = TASK_UPDATED_DEADLINE
        task.save()

        updated_task = app_models.Task.objects.get(description=TASK_DESCRIPTION,
                                                   deadline=TASK_UPDATED_DEADLINE)

        self.assertEquals(task.pk, updated_task.pk,
                          "The Task was not updated correctly")

    def test_update3(self):

        """Creating a Task, with description. Then updating its done status"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION)
        task = app_models.Task.objects.get(description=TASK_DESCRIPTION)

        task.done = TASK_UPDATED_DONE
        task.save()

        updated_task = app_models.Task.objects.get(description=TASK_DESCRIPTION,
                                                   done=TASK_UPDATED_DONE)

        self.assertEquals(task.pk, updated_task.pk,
                          "The Task was not updated correctly")

    def test_update4(self):

        """Creating a Task, with description and deadline. Then updating its description"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)
        task = app_models.Task.objects.get(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)

        task.description = TASK_UPDATED_DESCRIPTION
        task.save()

        updated_task = app_models.Task.objects.get(description=TASK_UPDATED_DESCRIPTION,
                                                   deadline=TASK_DEADLINE)

        self.assertEquals(task.pk, updated_task.pk,
                          "The Task was not updated correctly")

    def test_update5(self):

        """Creating a Task, with description and deadline. Then updating its deadline"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)
        task = app_models.Task.objects.get(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)

        task.deadline = TASK_UPDATED_DEADLINE
        task.save()

        updated_task = app_models.Task.objects.get(description=TASK_DESCRIPTION,
                                                   deadline=TASK_UPDATED_DEADLINE)

        self.assertEquals(task.pk, updated_task.pk,
                          "The Task was not updated correctly")

    def test_update6(self):

        """Creating a Task, with description and deadline. Then updating its done status"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)
        task = app_models.Task.objects.get(description=TASK_DESCRIPTION, deadline=TASK_DEADLINE)

        task.done = TASK_UPDATED_DONE
        task.save()

        updated_task = app_models.Task.objects.get(description=TASK_DESCRIPTION,
                                                   done=TASK_UPDATED_DONE,
                                                   deadline=TASK_DEADLINE)

        self.assertEquals(task.pk, updated_task.pk,
                          "The Task was not updated correctly")

    def test_delete(self):

        """Deleting a Task"""

        app_models.Task.objects.create(description=TASK_DESCRIPTION)
        app_models.Task.objects.get(description=TASK_DESCRIPTION).delete()

        self.assertRaises(ObjectDoesNotExist,             # exception
                          app_models.Task.objects.get,    # method to call
                          description=TASK_DESCRIPTION)   # arg to method


class CommentFullCleanupTest(FullCleanupTest):

    def test_create(self):

        """Creating a Comment"""

        user = auth_models.User.objects.create(username=USERNAME)
        app_models.Comment.objects.create(text=COMMENT_TEXT, author=user)

        self.assertIsNotNone(app_models.Comment.objects.get(text=COMMENT_TEXT),
                             "The Comment was not created correctly")

    def test_update(self):

        """Creating a Comment with text. Then updating its text"""

        user = auth_models.User.objects.create(username=USERNAME)
        comment = app_models.Comment.objects.create(text=COMMENT_TEXT, author=user)

        comment.text = COMMENT_UPDATED_TEXT
        comment.save()

        updated_comment = app_models.Comment.objects.get(text=COMMENT_UPDATED_TEXT)

        self.assertEquals(comment.pk, updated_comment.pk,
                          "The Comment was not updated correctly")

    def test_delete(self):

        """Deleting a Comment"""

        user = auth_models.User.objects.create(username=USERNAME)
        app_models.Comment.objects.create(text=COMMENT_TEXT, author=user)

        app_models.Comment.objects.get(text=COMMENT_TEXT).delete()

        self.assertRaises(ObjectDoesNotExist,                # exception
                          app_models.Comment.objects.get,    # method to call
                          text=COMMENT_TEXT)                 # arg to method


class AddTest(FullCleanupTest):

    def test_add_task1(self):

        """Addings a Task with description to an existing TODOList"""

        todo_list = app_models.TODOList.objects.create(title=TODO_LIST_TITLE)
        task = app_models.Task.objects.create(description=TASK_DESCRIPTION)

        todo_list.tasks.add(task)
        todo_list.save()

        self.assertIn(task, todo_list.tasks.all())

    def test_add_task2(self):

        """Addings a Task with description and deadline to an existing TODOList"""

        todo_list = app_models.TODOList.objects.create(title=TODO_LIST_TITLE)
        task = app_models.Task.objects.create(description=TASK_DESCRIPTION,
                                              deadline=TASK_DEADLINE)

        todo_list.tasks.add(task)
        todo_list.save()

        self.assertIn(task, todo_list.tasks.all())

    def test_add_comment(self):

        """Adding a Comment to an existing Task"""

        task = app_models.Task.objects.create(description=TASK_DESCRIPTION)
        user = auth_models.User.objects.create(username=USERNAME)
        comment = app_models.Comment.objects.create(text=COMMENT_TEXT, author=user)

        task.comments.add(comment)

        self.assertIn(comment, task.comments.all())
