# Generated by Django 3.1 on 2021-06-08 05:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Aboutus')),
                ('description', froala_editor.fields.FroalaField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog')),
                ('description', froala_editor.fields.FroalaField()),
                ('view_count', models.BigIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardExecutiveMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('executive_member_name', models.CharField(max_length=200)),
                ('executive_member_designation', models.CharField(max_length=200)),
                ('executive_member_image', models.ImageField(upload_to='Board Members')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardImmediatePastPresident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('immediate_past_president_name', models.CharField(max_length=200)),
                ('immediate_past_president_designation', models.CharField(max_length=200)),
                ('immediate_past_president_image', models.ImageField(upload_to='Board Members')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardVicePresidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('vice_president_name', models.CharField(max_length=200)),
                ('vice_president_designation', models.CharField(max_length=200)),
                ('vice_president_image', models.ImageField(upload_to='Board Members')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('logo', models.ImageField(upload_to='Donors')),
                ('description', froala_editor.fields.FroalaField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('question', models.CharField(max_length=500)),
                ('answer', froala_editor.fields.FroalaField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FooterImportantLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery')),
                ('description', froala_editor.fields.FroalaField(default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsandMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='News')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='News')),
                ('description', froala_editor.fields.FroalaField()),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='organization')),
                ('address', models.CharField(max_length=500)),
                ('profile_image', models.ImageField(default='', upload_to='organization')),
                ('contact_no', models.CharField(max_length=200)),
                ('alt_contact_no', models.CharField(blank=True, max_length=200, null=True)),
                ('map_location', models.CharField(blank=True, max_length=2000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('alt_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('slogan', models.CharField(blank=True, max_length=500, null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=200, null=True)),
                ('viber', models.CharField(blank=True, max_length=200, null=True)),
                ('terms_and_conditions', models.TextField(blank=True, null=True)),
                ('introduction', models.TextField(default='')),
                ('mission', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mission_icon', models.ImageField(default='', upload_to='organization')),
                ('vision', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('vision_icon', models.ImageField(default='', upload_to='organization')),
                ('goal', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('goal_icon', models.ImageField(default='', upload_to='organization')),
                ('geographical_title', models.CharField(blank=True, max_length=200, null=True)),
                ('geographical_description', froala_editor.fields.FroalaField()),
                ('geographical_image', models.ImageField(default='', upload_to='geographical')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Programmes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Programmes')),
                ('description', froala_editor.fields.FroalaField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='publications')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='documents')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', froala_editor.fields.FroalaField(blank=True, default='', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image1', models.ImageField(upload_to='Sliders')),
                ('image2', models.ImageField(upload_to='Sliders')),
                ('image3', models.ImageField(upload_to='Sliders')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='Sliders')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='Sliders')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaNewsFeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('source', froala_editor.fields.FroalaField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuccessStories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='successstories')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='successstories')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='successstories')),
                ('description', froala_editor.fields.FroalaField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='Events')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Events')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='Events')),
                ('description', froala_editor.fields.FroalaField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('video_url', models.URLField()),
                ('video_id', models.CharField(default='', max_length=500)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='video thumbnail')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('logo', models.ImageField(upload_to='Projects')),
                ('description', froala_editor.fields.FroalaField()),
                ('accomplished', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('partner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='fweanapp.donors')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='gallery')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fweanapp.imagealbum')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('president_name', models.CharField(max_length=200)),
                ('president_designation', models.CharField(max_length=200)),
                ('president_image', models.ImageField(upload_to='Board Members')),
                ('general_secretary_name', models.CharField(max_length=200)),
                ('general_secretary_designation', models.CharField(max_length=200)),
                ('general_secretary_image', models.ImageField(upload_to='Board Members')),
                ('secretary_name', models.CharField(max_length=200)),
                ('secretary_designation', models.CharField(max_length=200)),
                ('secretary_image', models.ImageField(upload_to='Board Members')),
                ('treasurer_name', models.CharField(max_length=200)),
                ('treasurer_designation', models.CharField(max_length=200)),
                ('treasurer_image', models.ImageField(upload_to='Board Members')),
                ('executive_members', models.ManyToManyField(to='fweanapp.BoardExecutiveMembers')),
                ('immediate_past_presidents', models.ManyToManyField(to='fweanapp.BoardImmediatePastPresident')),
                ('vice_presidents', models.ManyToManyField(to='fweanapp.BoardVicePresidents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fweanapp.blog')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
