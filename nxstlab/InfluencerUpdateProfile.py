from nxstlab.models import Influencer
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_api import status
from werkzeug.utils import secure_filename
import os

from nxstlab.user import User


class InfluencerUpdateProfile(Resource):
    # API to update signed up influencer profile
    def post(self):
        data = dict()
        for key in request.form:
            data[key] = request.form[key]
        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='influencer', message='Influencer does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            file1 = None
            file2 = None

            influencer = Influencer.objects(email=data['email']).first()
            if 'file1' in request.files:
                file1 = request.files['file1']
            if 'file2' in request.files:
                file2 = request.files['file2']
            if file1:
                filename = secure_filename(file1.filename)
                fileLocation = os.path.join('static/uploads/influencer_profile/', filename)
                file1.save(fileLocation)
                influencer.image = '/' + fileLocation

            if file2:
                filename2 = secure_filename(file2.filename)
                fileLocation2 = os.path.join('static/uploads/influencer_campaign/', filename2)
                file2.save(fileLocation2)
                influencer.campaignImages = '/' + fileLocation2

            for key in data:
                print(key)
                if key == 'file1' or key == 'file2':
                    continue
                else:

                    influencer[key] = data[key]
            influencer.save()

            if 'password' in data:
                temp = User.objects(email=data['email']).first()
                temp.password = User.generate_hash(data['password'])
                temp.save()
            return make_response(jsonify(role='influencer', message='Influencer details updated successfully in database'),
                                 status.HTTP_200_OK)

class InfluencerProfile(Resource):
    def post(self):
        data = request.get_json(force=True)
        influencer = Influencer.objects(email=data['email']).first()

        if not Influencer.objects(email=data['email']):
            return make_response(jsonify(role='influencer', message='Influencer does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            temp = dict()
            temp['first_name'] = influencer.first_name
            temp['last_name'] = influencer.last_name
            temp['email'] = influencer.email
            temp['website_social_media_handles'] = influencer.website_social_media_handles
            temp['followers'] = influencer.followers
            temp['areas_of_interest'] = influencer.areas_of_interest
            temp['dob'] = influencer.dob
            temp['gender'] = influencer.gender
            temp['image'] = influencer.image
            temp['campaignImage'] = influencer.campaignImages
            temp['password'] = influencer.password
            temp['big_deal_on_option1'] = influencer.big_deal_on_option1
            temp['big_deal_on_option2'] = influencer.big_deal_on_option2
            temp['big_deal_on_option3'] = influencer.big_deal_on_option3
            temp['big_deal_on_option4'] = influencer.big_deal_on_option4
            temp['big_deal_on_option5'] = influencer.big_deal_on_option5
            return make_response(jsonify(data=temp, role='influencer', message='Influencer profile details'),
                             status.HTTP_200_OK)
