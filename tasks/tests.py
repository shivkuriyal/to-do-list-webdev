from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskModelTests(TestCase):
    def test_create_task(self):
        task = Task.objects.create(
            title="Complete Web Dev Assignment",
            description="Use HTML, CSS, and Django."
        )
        self.assertEqual(str(task), "Complete Web Dev Assignment")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.created_at)


class TaskViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task1 = Task.objects.create(
            title="Buy groceries",
            description="Milk, bread, eggs",
            completed=False
        )
        self.task2 = Task.objects.create(
            title="Submit project",
            description="Django assignment",
            completed=True
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, "Buy groceries")
        self.assertContains(response, "Submit project")
        self.assertContains(response, "Total: 2")
        self.assertContains(response, "Done: 1")
        self.assertContains(response, "Pending: 1")

    def test_empty_state(self):
        Task.objects.all().delete()
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks yet.")

    def test_task_create_get(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')
        self.assertContains(response, "Add Task")

    def test_task_create_post(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'Read a book',
            'description': 'Clean Code chapter 1',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title='Read a book').exists())
        self.assertContains(response, "Task created successfully!")

    def test_task_update_get(self):
        response = self.client.get(reverse('task_update', args=[self.task1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')
        self.assertContains(response, "Update Task")
        self.assertContains(response, self.task1.title)

    def test_task_update_post(self):
        response = self.client.post(reverse('task_update', args=[self.task1.pk]), {
            'title': 'Buy groceries updated',
            'description': 'Milk, cheese, butter',
            'completed': True,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Buy groceries updated')
        self.assertTrue(self.task1.completed)

    def test_task_toggle(self):
        self.assertFalse(self.task1.completed)
        response = self.client.get(reverse('task_toggle', args=[self.task1.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.completed)

        # Toggle back
        response = self.client.get(reverse('task_toggle', args=[self.task1.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.task1.refresh_from_db()
        self.assertFalse(self.task1.completed)

    def test_task_delete_get(self):
        response = self.client.get(reverse('task_delete', args=[self.task1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_confirm_delete.html')
        self.assertContains(response, "Are you sure you want to delete this task?")
        self.assertContains(response, self.task1.title)

    def test_task_delete_post(self):
        response = self.client.post(reverse('task_delete', args=[self.task1.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())
        self.assertContains(response, "Task deleted successfully!")
