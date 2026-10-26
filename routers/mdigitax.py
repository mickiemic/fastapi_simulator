from datetime import datetime
from decimal import Decimal
from fastapi import APIRouter, Header, Request, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
import logging
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()

# Retrieves the existing global instance configured in main.py
logger = logging.getLogger("fastapi_middleware_logger")

# ========= Digitax Simulator ==================

class Item(BaseModel):
    tax_type_code: str
    default_unit_price: float
    stock_quantity: Optional[float] = 0
    callback_url: Optional[str] = None
    item_bar_code: str
    item_class_code: str
    item_type_code: str
    item_name: str
    origin_nation_code: str
    package_unit_code: str
    quantity_unit_code: str

class SaleItem(BaseModel):
    item_name: str
    item_class_code: str
    item_bar_code: str
    item_tax_type_code: str
    quantity: float
    unit_price: Decimal
    total_amount: Decimal
    taxable_amount: Optional[Decimal] = None
    tax_amount: Optional[Decimal] = None
    package_unit_quantity: float
    discount_rate: Optional[float] = 0
    discount_amount: Optional[Decimal] = None
    item_description: str
    is_stockable: Optional[bool] = True


class SaleTrx(BaseModel):
    sale_date: str
    customer_tin: Optional[str] = None
    customer_name: Optional[str] = None
    customer_id: Optional[str] = None
    trader_invoice_number: str
    payment_type_code: str
    invoice_status_code: str
    callback_url: Optional[str] = None
    invoice_details: Optional[str] = None
    is_tax_exempt: Optional[bool] = False
    items: List[SaleItem]

@router.post("/ke/v2/items", summary="Create an item")
async def createitem(req: Item, x_api_key: str = Header(None)):
    jsonItem = jsonable_encoder(req)
    strPlayload = json.dumps(jsonItem)
    logger.info(f'>> /ke/v2/items [{req.item_bar_code}] >> {strPlayload}')
    jsonResponse = {
        "id": f"item_{req.item_bar_code}",
        "item_class_code": "84111600",
        "item_type_code": "3",
        "item_name": "Due from Related Parties CSL",
        "origin_nation_code": "KE",
        "package_unit_code": "NT",
        "quantity_unit_code": "NO",
        "tax_type_code": "A",
        "default_unit_price": 1,
        "etims_item_code": "KE3NTNO02036457",
        "is_stock_item": False,
        "stock_quantity": 0,
        "active": True,
        "status": "COMPLETED",
        "item_bar_code": req.item_bar_code
    }
    return JSONResponse(content=jsonResponse, status_code=201)


@router.post("/ke/v2/sales-with-items", summary="Add sale with item information")
async def addsalewithitems(req: SaleTrx, x_api_key: str = Header(None)):
    jsonReq = jsonable_encoder(req)
    strPlayload = json.dumps(jsonReq)
    logger.info(f'>> /ke/v2/sales-with-items [{req.trader_invoice_number}] >> {strPlayload}')
    now = datetime.now()
    jsonResponse = {
        "id": f"sale_{req.trader_invoice_number}",
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S %p"),
        "trader_invoice_number": req.trader_invoice_number,
        "receipt_type_code": "S",
        "sale_detail_url": "https://api.digitax.tech/ke/v2/sales/sale_01KZ5SE3A4S1WRV64G1YVTWY8V",
        "serial_number": "KRARVS000000005",
        "receipt_number": 0,
        "invoice_number": 1097621,
        "customer_id": "customer_01KX5D1F40G0BWR3NJZ6PJDYZX",
        "customer_name": "Safaricom",
        "customer_tin": "P051129820X",
        "internal_data": "",
        "receipt_signature": "",
        "etims_url": "",
        "offline_url": f"https://receipt.dg.tax/r/business_01KMJ9S89Z7ZZPMJST0V2R5QCR/{req.trader_invoice_number}",
        "status": "PENDING",
        "sales_tax_summary": {
            "taxable_amount_a": 0,
            "taxable_amount_b": 0,
            "taxable_amount_c": 539200,
            "taxable_amount_d": 0,
            "taxable_amount_e": 0,
            "tax_rate_a": 0,
            "tax_rate_b": 16,
            "tax_rate_c": 0,
            "tax_rate_d": 0,
            "tax_rate_e": 8,
            "tax_amount_a": 0,
            "tax_amount_b": 0,
            "tax_amount_c": 0,
            "tax_amount_d": 0,
            "tax_amount_e": 0
        }
    }
    jsonResponse["serial_number"] = "KRARVS000000005"
    jsonResponse["offline_url"] = f"https://receipt.dg.tax/r/business_01KMJ9S89Z7ZZPMJST0V2R5QCR/{req.trader_invoice_number}"
    for item in jsonReq["items"]:
        item["id"] = f"saleitem_{item['item_bar_code']}"
        item["item_id"] = f"item_{item['item_bar_code']}"
        item["tax_type_code"] = item["item_tax_type_code"]
        del item["item_tax_type_code"]
        del item["item_class_code"]
        del item["item_description"]
        item["tax_amount"] = 1.23
        item["unit_price"] = float(item["unit_price"])
        item["total_amount"] = float(item["total_amount"])
        item["taxable_amount"] = float(item["taxable_amount"])
        item["discount_amount"] = 0
        item["discount_rate"] = 0
    jsonResponse["item_list"] = jsonReq["items"]

    return JSONResponse(content=jsonResponse, status_code=201)


