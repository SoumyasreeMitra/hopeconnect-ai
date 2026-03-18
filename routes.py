from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from models import db, Volunteer, Opportunity, Donation
from ai_matcher import match_volunteer_to_opportunities

api = Blueprint('api', __name__)

# Auth
@api.route('/login', methods=['POST'])
def login():
    data = request.json
    token = create_access_token(identity=data['username'])
    return jsonify({"token": token})

# Volunteers
@api.route('/volunteers', methods=['POST'])
@jwt_required()
def add_volunteer():
    data = request.json
    v = Volunteer(**data)
    db.session.add(v)
    db.session.commit()
    return jsonify({"message": "Volunteer registered", "id": v.id}), 201

@api.route('/volunteers', methods=['GET'])
@jwt_required()
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([v.to_dict() for v in volunteers])

# Opportunities
@api.route('/opportunities', methods=['POST'])
@jwt_required()
def add_opportunity():
    data = request.json
    o = Opportunity(**data)
    db.session.add(o)
    db.session.commit()
    return jsonify({"message": "Opportunity added", "id": o.id}), 201

@api.route('/opportunities', methods=['GET'])
@jwt_required()
def get_opportunities():
    opportunities = Opportunity.query.all()
    return jsonify([o.to_dict() for o in opportunities])

# AI Matching
@api.route('/match/<int:volunteer_id>', methods=['GET'])
@jwt_required()
def match_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    opportunities = Opportunity.query.all()
    matches = match_volunteer_to_opportunities(
        volunteer.to_dict(),
        [o.to_dict() for o in opportunities]
    )
    return jsonify({
        "volunteer": volunteer.to_dict(),
        "matches": matches
    })

# Donations
@api.route('/donations', methods=['POST'])
@jwt_required()
def add_donation():
    data = request.json
    d = Donation(**data)
    db.session.add(d)
    db.session.commit()
    return jsonify({"message": "Donation recorded", "id": d.id}), 201

@api.route('/donations/summary', methods=['GET'])
@jwt_required()
def donation_summary():
    donations = Donation.query.all()
    total = sum(d.amount for d in donations)
    by_ngo = {}
    for d in donations:
        by_ngo[d.ngo_name] = by_ngo.get(d.ngo_name, 0) + d.amount
    return jsonify({"total_donations": total, "by_ngo": by_ngo})

# Error handlers
@api.app_errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@api.app_errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500