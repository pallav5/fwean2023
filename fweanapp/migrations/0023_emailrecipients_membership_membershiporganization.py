# Generated by Django 2.1 on 2021-12-01 09:52

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fweanapp', '0022_auto_20211026_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to='members')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=100)),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_profession', models.CharField(blank=True, max_length=100, null=True)),
                ('spouse_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('son_name', models.CharField(blank=True, max_length=100, null=True)),
                ('daughter_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_no', models.CharField(max_length=15)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('educational_qualification', models.CharField(choices=[('Graduate', 'Graduate'), ('Post Graduate', 'Post Graduate'), ('Professional', 'Professional')], max_length=100)),
                ('edu_qualifications_others', models.TextField(blank=True, null=True)),
                ('enterprise_type', models.CharField(choices=[('Manufacturing', 'Manufacturing'), ('Trading', 'Trading'), ('Agriculture', 'Agriculture'), ('Service', 'Service')], max_length=100)),
                ('enterprise_type_others', models.TextField(blank=True, null=True)),
                ('enterprise_scale', models.CharField(choices=[('Micro/Cottage', 'Micro/Cottage'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=100)),
                ('additional_personal_information', models.TextField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=100)),
                ('company_phone_no', models.CharField(max_length=15)),
                ('company_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('designation', models.CharField(max_length=100)),
                ('pan_vat', models.IntegerField()),
                ('registration_date', models.DateField()),
                ('yearly_turnover', models.IntegerField()),
                ('current_assets', models.IntegerField()),
                ('correspondence_to_reach', models.CharField(choices=[('Residence', 'Residence'), ('Office', 'Office')], max_length=100)),
                ('correspondence_to_reach_others', models.TextField(blank=True, null=True)),
                ('how_did_you_know_about_fwean', models.TextField()),
                ('why_do_you_want_to_become_a_member', multiselectfield.db.fields.MultiSelectField(choices=[('Networking among fellow women.', 'Networking among fellow women.'), ('Business / Profession', 'Business / Profession.'), ('Legal issues', 'Legal issues.'), ('Women issues', 'Women issues.'), ('Opportunities to participate in training programs', 'Opportunities to participate in training programs.'), ('Expert opinion and guidance in your area of activity', 'Expert opinion and guidance in your area of activity.')], max_length=181)),
                ('why_do_you_want_to_become_a_member_other', models.TextField(blank=True, null=True)),
                ('contributing_to_the_objectives', multiselectfield.db.fields.MultiSelectField(choices=[('As trainers at (seminars, workshops) etc.', 'As trainers at seminars, workshops etc.'), ('Becoming a part of the organizational structure of FWEAN', 'Becoming a part of the organizational structure of FWEAN'), ('Fund Raising / Sponsoring / Co-sponsoring events', 'Fund Raising / Sponsoring / Co-sponsoring events'), ('Contributing in Newsletter', 'Contributing in Newsletter'), ('Attending seminars, conventions, debates, etc. ', 'Attending seminars, conventions, debates, etc. '), ('Membership Development', 'Membership Development')], max_length=245)),
                ('contributing_to_the_objectives_other', models.TextField(blank=True, null=True)),
                ('elborate_on_your_choices', models.TextField()),
                ('time_can_you_give_to_fwean_activities', models.CharField(choices=[('1-3 hours per week', '1-3 hours per week'), ('1-3 hours per fortnight', '1-3 hours per fortnight'), ('1-3 hours per month', '1-3 hours per month'), ('1-3 hours per quarter', '1-3 hours per quarter'), ('1-3 hours per half year', '1-3 hours per half year'), ('1-3 hours per year', '1-3 hours per year')], max_length=100)),
                ('time_would_yo_prefer_for_fwean_programs', models.CharField(choices=[('Weekdays', 'Weekdays'), ('Weekends', 'Weekends'), ('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=100)),
                ('type_of_programs_would_you_want_in_fwean', multiselectfield.db.fields.MultiSelectField(choices=[('Entrepreneurial', 'Entrepreneurial'), ('Business Support', 'Business Support'), ('Finance', 'Finance'), ('Marketing', 'Marketing'), ('Advocacy', 'Advocacy'), ('Networking', 'Networking'), ('Economic', 'Economic'), ('Women Issues', 'Women Issues'), ('Social', 'Social')], max_length=99)),
                ('type_of_programs_would_you_want_in_fwean_others', models.TextField(blank=True, null=True)),
                ('membership_proposed_by', models.CharField(max_length=100)),
                ('membership_applied_for', models.CharField(choices=[('Individual', 'Individual'), ('Institutional', 'Institutional')], max_length=100)),
                ('registration_certificate', models.FileField(upload_to='membership_documents')),
                ('pan_vat_certificate', models.FileField(upload_to='membership_documents')),
                ('citizenship_passport', models.FileField(upload_to='membership_documents')),
                ('cv', models.FileField(upload_to='membership_documents')),
                ('tax_clearance', models.FileField(upload_to='membership_documents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MembershipOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('name_of_other_org', models.TextField()),
                ('designation_of_other_org', models.TextField()),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='fweanapp.Membership')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
