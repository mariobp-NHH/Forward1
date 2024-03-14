from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2024_group2.forms import RegistrationForm, LoginForm,  BusForm, CarForm, FerryForm,trainForm, BicycleForm, WalkForm, CarFormSUV, Domestic_FlightForm, Long_haul_FlightForm, long_distance_busForm, tramForm
from datetime import timedelta, datetime
from webse import db, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json

gd_course_NHH_2024_group2=Blueprint('gd_course_NHH_2024_group2',__name__)

#Home routes
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/home')
def home_home():
  return render_template('gd_course/NHH_2024_group2/home.html', title = 'Home')

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/about_us')
def about_us_home():
  return render_template('gd_course/NHH_2024_group2/about_us.html', title='about_us')

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/contact')
def contact_home():
  return render_template('gd_course/NHH_2024_group2/contact.html', title='contact')

#Users routes
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/register', methods=['GET','POST'])
def register():
    form = RegistrationForm
    return render_template('gd_course/NHH_2024_group2/users/register.html', title='Register', form=form)

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/login', methods=['GET','POST'])
def login():
  form = LoginForm
  return render_template('gd_course/NHH_2024_group2/users/login.html', title='Login', form=form)

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/logout')
def logout():
  logout_user()
  return redirect(url_for('gd_course_NHH_2024_group2.home_home'))

# Methodology
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2024_group2/methodology.html', title='Methodology')



efco2={'Car: Small':{'Petrol':0.1462,'Diesel':0.1197,'Electric':0.0414},
    'Car: SUV':{'Petrol':0.2088,'Diesel':0.1835,'Electric':0.0477},
    'Domestic Flight':{'Not my choice':0.246},
    'Long-haul Flight':{'Not my choice':0.1480},
    'Bus':{'Not my choice':0.097},
    'Long distance bus (Coach)':{'Not my choice':0.027},
    'Tram':{'Not my choice':0.029},
    'Train':{'Not my choice':0.035},
    'Ferry':{'Not my choice':0.019},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

#if statement för att räkna co2 utsläpp fr alla classer

#if statement för att räkna om det finns ett annat transport sätt som är bättre
    #tar co2 från if statementen ovanför 
    #returnar bättre sätt att åka på 

#Carbon app, main page
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app')
#@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2024_group2/carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_bus', methods=['GET','POST'])
#@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        if float(kms) <= 15:
            saved = co2
            message = f"You could have saved {saved} by taking the bicycle or walking"
        else:
            saved = float(kms) - efco2['Tram'][fuel]
            saved2 = float(kms) * efco2['Train'][fuel]
            message = f"You could have saved {saved} by taking the tram and {saved2} by taking the train"
    
            
        #istellet för popup display bredvid graferna på samma sett så de är displayed


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
        #return render_template('index.html', popup_script=popup_script)
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car small
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_car', methods=['GET','POST'])
#@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        people= form.people.data
        transport = 'Car: Small'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / float(people)
        #ch4 = float(kms) * efch4[transport][fuel]
        #total = co2+ch4

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)
        #ch4 = float("{:.2f}".format(ch4))
        #total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=people, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry car SUV
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_carSUV', methods=['GET','POST'])
#@login_required
def new_entry_carSUV():
    form = CarFormSUV()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        people = form.people.data
        transport = 'Car: SUV'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / float(people)
        #ch4 = float(kms) * efch4[transport][fuel]
        #total = co2+ch4

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        #ch4 = float("{:.2f}".format(ch4))
        #total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4= people, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_carSUV.html', title='new entry car SUV', form=form) 

#New entry Domestic Flight
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_domestic_flight', methods=['GET','POST'])
#@login_required
def new_entry_domestic_flight():
    form = Domestic_FlightForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Domestic Flight'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_domestic_flight.html', title='new entry domestic flight', form=form)

#New entry Long-haul Flight
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_long_haul_flight', methods=['GET','POST'])
#@login_required
def new_entry_long_haul_flight():
    form = Long_haul_FlightForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Long-haul Flight'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_long_haul_flight.html', title='new entry Long-haul Flight', form=form)

#New entry Long distance bus (Coach) 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_long_distance_bus', methods=['GET','POST'])
#@login_required
def new_entry_long_distance_bus():
    form = long_distance_busForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Long distance bus (Coach)'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_long_distance_bus.html', title='new entry long distance bus (Coach)', form=form)

#New entry Tram 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_tram', methods=['GET','POST'])
#@login_required
def new_entry_tram():
    form = tramForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Tram'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_tram.html', title='new entry tram', form=form)

#New entry Train 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_train', methods=['GET','POST'])
#@login_required
def new_entry_train():
    form = trainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_train.html', title='new entry train', form=form)

#New entry Ferry 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_ferry', methods=['GET','POST'])
#@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)


#New entry Bicycle
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_bicycle', methods=['GET','POST'])
#@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry Walk
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_walk', methods=['GET','POST'])
#@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)


        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_walk.html', title='new entry walk', form=form)

#Your data
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/your_data')
#@login_required
def your_data():
    #Table
    
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2024_group2').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.EmissionsGD.asc()).all()

    return render_template('gd_course/NHH_2024_group2/carbon_app/your_data.html', title='your_data', entries=entries)


    

#Delete emission
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    
  


