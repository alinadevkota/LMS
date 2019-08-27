# Generated by Django 2.2.3 on 2019-08-25 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('topic_count', models.IntegerField(default=0, verbose_name='topic count')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('thread_count', models.IntegerField(default=0, verbose_name='thread count')),
                ('topic_icon', models.CharField(max_length=30, verbose_name='topic_icon')),
                ('node_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='forum.NodeGroup', verbose_name='nodegroup')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('content_raw', models.TextField(verbose_name='raw content')),
                ('content_rendered', models.TextField(blank=True, default='', verbose_name='rendered content')),
                ('view_count', models.IntegerField(default=0, verbose_name='view count')),
                ('reply_count', models.IntegerField(default=0, verbose_name='reply count')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='published time')),
                ('last_replied', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='last replied time')),
                ('order', models.IntegerField(default=10, verbose_name='order')),
                ('hidden', models.BooleanField(default=False, verbose_name='hidden')),
                ('closed', models.BooleanField(default=False, verbose_name='closed')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='forum.Topic', verbose_name='topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ['order', '-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_raw', models.TextField(verbose_name='raw content')),
                ('content_rendered', models.TextField(default='', verbose_name='rendered content')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='published time')),
                ('hidden', models.BooleanField(default=False, verbose_name='hidden')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forum.Thread', verbose_name='thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False, verbose_name='read')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='published time')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post', verbose_name='reply')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
                ('thread', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Thread', verbose_name='thread')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL, verbose_name='recipient')),
            ],
        ),
        migrations.CreateModel(
            name='ForumAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_gravatar', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', max_length=255, null=True, upload_to='uploads/forum/avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='forum_avatar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appendix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='published time')),
                ('content_raw', models.TextField(verbose_name='raw content')),
                ('content_rendered', models.TextField(blank=True, default='', verbose_name='rendered content')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Thread', verbose_name='thread')),
            ],
        ),
    ]
