from flask_restful import Resource
from flask import jsonify, request, make_response
from brand import Brand
from flask_api import status


class AdminDeactivateBrandAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            brand = Brand.objects(email=data['email'])
            brand = brand[0]
            brand['isactive'] = False
            brand.save()

            return make_response(jsonify(role='admin', message='brand has been deactivated'), status.HTTP_200_OK)


class AdminApproveBrandSignupAPI(Resource):
    def post(self):
        data = request.get_json(force=True)

        if not Brand.objects(email=data['email']):
            return make_response(jsonify(role='admin', message='brand does not exists in database'),
                                 status.HTTP_404_NOT_FOUND)

        else:
            brand = Brand.objects(email=data['email'])
            brand = brand[0]
            if not brand['isapproved']:
                brand.isapproved = True
                brand.isactive = True
                brand.save()
                return make_response(jsonify(role='admin', message='brand is approved'), status.HTTP_200_OK)
            else:
                return make_response(jsonify(role='admin', message='brand is already approved'), status.HTTP_200_OK)
