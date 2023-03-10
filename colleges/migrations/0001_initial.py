# Generated by Django 4.1.3 on 2022-11-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=250)),
                ('region', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('Place', models.CharField(max_length=250)),
                ('affl_university', models.CharField(max_length=250)),
                ('established_year', models.IntegerField()),
                ('branch_code', models.CharField(max_length=250)),
                ('placements', models.IntegerField()),
                ('placement_ratio', models.FloatField()),
                ('college_fee', models.FloatField()),
                ('infra', models.IntegerField()),
                ('nirf_ranking', models.IntegerField()),
                ('nba_accredit', models.BooleanField(default=False)),
                ('hostel', models.CharField(max_length=250)),
                ('avg_sal', models.FloatField()),
                ('high_sal', models.FloatField()),
                ('top_comanies', models.CharField(max_length=500)),
                ('college_website', models.TextField()),
                ('oc_boys_rank', models.IntegerField()),
                ('oc_girls_rank', models.IntegerField()),
                ('sc_boys_rank', models.IntegerField()),
                ('sc_girls_rank', models.IntegerField()),
                ('st_boys_rank', models.IntegerField()),
                ('st_girls_rank', models.IntegerField()),
                ('bc_a_boys_rank', models.IntegerField()),
                ('bc_b_boys_rank', models.IntegerField()),
                ('bc_c_boys_rank', models.IntegerField()),
                ('bc_d_boys_rank', models.IntegerField()),
                ('bc_e_boys_rank', models.IntegerField()),
                ('bc_a_girls_rank', models.IntegerField()),
                ('bc_b_girls_rank', models.IntegerField()),
                ('bc_c_girls_rank', models.IntegerField()),
                ('bc_d_girls_rank', models.IntegerField()),
                ('bc_e_girls_rank', models.IntegerField()),
            ],
        ),
    ]
