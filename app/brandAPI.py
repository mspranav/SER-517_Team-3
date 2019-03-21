from flask_restful import Resource
from flask import jsonify, request, make_response
from brand import Brand
from flask_api import status


class BrandAPI(Resource):
    def post(self):
        data = request.get_json(force=True)
        if Brand.objects(email=data['email']):
            return make_response(jsonify(role='brand', message='brand already exists in database'),
                             status.HTTP_409_CONFLICT)
        else:
            Brand(
              first_name = data['first_name'],
              last_name = data['last_name'],
              email = data['email'],
              password = data['password'],
              website = data['website']
            ).save()

            return make_response(jsonify(role='brand', message='brand added successfully in database'),
                             status.HTTP_201_CREATED)

    def put(self):
        data = request.get_json(force=True)
        # handle case for invalid request
        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='brand', message='brand does not exist in database'),
                             status.HTTP_404_NOT_FOUND)
        else:
            brand = Brand.objects(email=data['email']).first()
            data = request.get_json()
            for key in data:
                brand[key] = data[key]
            brand.save()
            return make_response(jsonify(role='brand', message='brand details updated successfully in database'),
                                 status.HTTP_200_OK)
    def get(self):
        brands = [brand for brand in Brand.objects()]
        res = []
        for brand in brands:
            temp = dict()
            temp["first_name"] = brand.first_name
            temp["last_name"] = brand.last_name
            temp["email"] = brand.email
            res.append(temp)
        return make_response(jsonify(data=res, role='admin', message='list of brands'),
                             status.HTTP_200_OK)
