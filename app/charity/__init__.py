from flask import Blueprint
charity = Blueprint('charity',__name__)
from . import forms,views