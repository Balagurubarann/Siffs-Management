from src.extension import db
from src.model import StockItem, Stock
from flask import Blueprint, request, jsonify, g

stockRoute = Blueprint(
    "stocks",
    __name__,
    url_prefix="api/stock"
)
