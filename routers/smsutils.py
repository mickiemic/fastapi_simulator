from fastapi import APIRouter, Header, Query, Request, HTTPException, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPAuthorizationCredentials
import json
import logging
from typing import Annotated, Any, Dict, List, Optional
from pydantic import BaseModel
import secrets
from datetime import datetime, timezone
import time
import asyncio
import requests
import uuid

router = APIRouter()
logger = logging.getLogger("fastapi_middleware_logger")

# ======== SalumMessenger ================================
class SalumSMSRequest(BaseModel):
    apikey: str
    partnerID: str
    message: str
    shortcode: str
    mobile: str

class SalumRequest2(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_field = "Custom field value"

    apikey: str
    partnerID: str
    message: str
    shortcode: str
    mobile: str

class SalumBalRequest(BaseModel):
    apikey: str
    partnerID: str

class SalumDLRRequest(BaseModel):
    apikey: str
    partnerID: str
    messageid: str


@router.post("/salum/sendsms", summary="Send Salum SMS Message")
async def sendsalumsms(request: SalumSMSRequest, x_request_id: str = Header(None)): 
    # x_request_id = request.headers.get('x-request-id')
    print(f'x-request-id : {x_request_id}')
    respHeaders: Dict = {}
    if x_request_id:
        respHeaders['X-Request-ID'] = x_request_id
    
    # print(f'x-request-id : {X-Request-ID}')
    # headers = {key: value for key, value in request.headers.items()}

    jsonItem = jsonable_encoder(request)
    strPlayload = json.dumps(jsonItem)
    print(f'payload: {strPlayload}')

    time.sleep(7)
    jsonResponse = {
        "responses": [
            {
            "respose-code": 200,
            "response-description": "Success",
            "mobile": 254712345678,
            "messageid": 8290842,
            "networkid": "1"
            }
        ]
    }
    return JSONResponse(content=jsonResponse, headers=respHeaders, status_code=201)

@router.post("/salum/getbalance", summary="Check Salum SMS Balance")
async def getsalumbalance(request: SalumBalRequest, x_request_id: str = Header(None)): 
    # x_request_id = request.headers.get('x-request-id')
    print(f'x-request-id : {x_request_id}')
    respHeaders: Dict = {}
    if x_request_id:
        respHeaders['X-Request-ID'] = x_request_id

    jsonItem = jsonable_encoder(request)
    strPlayload = json.dumps(jsonItem)
    print(f'payload: {strPlayload}')

    time.sleep(7)
    jsonResponse = {
        "respose-code": 200,
        "credit": "24584.00",
        "partner-id": request.partnerID
    }
    return JSONResponse(content=jsonResponse, headers=respHeaders, status_code=200)

@router.post("/salum/getdlr", summary="Get Salum SMS Delivery Report")
async def getsalumdlr(request: SalumDLRRequest, x_request_id: str = Header(None)): 
    print(f'x-request-id : {x_request_id}')
    respHeaders: Dict = {}
    if x_request_id:
        respHeaders['X-Request-ID'] = x_request_id

    jsonItem = jsonable_encoder(request)
    strPlayload = json.dumps(jsonItem)
    print(f'payload: {strPlayload}')

    time.sleep(7)
    jsonResponse = {
        "respose-code": 500,
        "response-description": "Service Unavailable"
    }
    return JSONResponse(content=jsonResponse, headers=respHeaders, status_code=200)

# ======== OnFonMessenger ================================
class MessageParameter(BaseModel):
    Number: str
    Text: str
    
class OnFonSMSRequest(BaseModel):
    ApiKey: str
    ClientId: str
    SenderId: str
    IsFlash: bool
    IsUnicode: bool
    MessageParameters: List[MessageParameter]


@router.post("/onfon/SendBulkSMS", summary="Send OnFon SMS Message")
async def sendonfonsms(request: OnFonSMSRequest, x_request_id: str = Header(None)): 
    # x_request_id = request.headers.get('x-request-id')
    print(f'x-request-id : {x_request_id}')
    respHeaders: Dict = {}
    if x_request_id:
        respHeaders['X-Request-ID'] = x_request_id
    
    # print(f'x-request-id : {X-Request-ID}')
    # headers = {key: value for key, value in request.headers.items()}

    jsonItem = jsonable_encoder(request)
    strPlayload = json.dumps(jsonItem)
    print(f'payload: {strPlayload}')

    time.sleep(3)
    jsonResponse = {
        "ErrorCode": 0,
        "ErrorDescription": "null",
        "Data": [
            {
                "MessageErrorCode": 0,
                "MessageErrorDescription": "Success",
                "MobileNumber": "254722799445",
                "MessageId": "2805b6e5-c8f2-42c1-b46c-e82c3bd87861",
                "Custom": ""
            }
        ]
    }
    return JSONResponse(content=jsonResponse, headers=respHeaders, status_code=201)

@router.get("/onfon/Balance", summary="Check OnFon SMS Balance")
async def getonfonbalance(
    ApiKey: Annotated[str, Query(description = "ApiKey")],
    ClientId: Annotated[str, Query(description = "ClientId")],
    x_request_id: Annotated[str | None, Header()] = None
):
    print(f'x-request-id : {x_request_id}, ApiKey: {ApiKey}, ClientId: {ClientId}')
    respHeaders: Dict = {}
    if x_request_id:
        respHeaders['X-Request-ID'] = x_request_id

    time.sleep(1)
    jsonResponse = {
        "ErrorCode": 0,
        "ErrorDescription": "null",
        "Data": [
            {
                "PluginType": "SMS",
                "Credits": "25000"
            }
        ]
    }
    return JSONResponse(content=jsonResponse, headers=respHeaders, status_code=200)

# ======== Eneza Messenger ================================
security = HTTPBasic()

class EnezaSMSRequest(BaseModel):
    senderId: str
    message: str
    phoneNumber: str
    messageId: str
    sendOption: Optional[str] = None
    scheduleTime: Optional[str] = None
    description: Optional[str] = None
    callBackUrl: Optional[str] = None

def get_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    # Perform validation (e.g., check DB)
    # if not (secrets.compare_digest(credentials.username, "admin") and 
    #         secrets.compare_digest(credentials.password, "supersecret")):
    #     raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials


@router.get("/eneza/oauth/v1/generate", summary="Generate OAuth Token")
async def generateOAuth(credentials: Annotated[str, Depends(get_current_user)]):
    token = secrets.token_hex(16)
    logger.info(f'username:{credentials.username}, password:{credentials.password} => {token}')
    jsonResponse = {
        "accessToken": token,
        "expiresIn": "3599"        
    }
    return JSONResponse(content=jsonResponse, status_code=200)

def verify_token(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    token = credentials.credentials    
    # Replace this with your actual JWT decoding or database token verification logic
    if token != "super-secret-admin-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )    
    return {"user": "admin", "role": "administrator"}

@router.post("/eneza/messages/v1/balance", summary="Get Eneza SMS Balance")
async def getEnezaBalance():
    jsonResponse = {
        "smsCredits": 1234        
    }
    return JSONResponse(content=jsonResponse, status_code=200)

@router.post("/eneza/messages/v1/send/single", summary="Eneza Send Single SMS")
async def sendSingleEnezaSMS(req: EnezaSMSRequest):
    jsonReq = jsonable_encoder(req)
    strPlayload = json.dumps(jsonReq)
    logger.info(f'>> /eneza/messages/v1/send/single [{req.phoneNumber}], messageId:[{req.messageId}] >> {strPlayload}')
    jsonResponse = {
        "phoneNumber": req.phoneNumber,
        "message": req.message,
        "messageId": req.messageId,
        "senderId": req.senderId,
        "callBackUrl": req.callBackUrl,
        "description": req.description
    }
    return JSONResponse(content=jsonResponse, status_code=200)

# ======== SMS Leopard Messenger ================================
class Destination(BaseModel):
    number: str

class SMSLeopardSendReq(BaseModel):
    source: str
    message: str
    destination: List[Destination]
    status_url: Optional[str] = None
    status_secret: Optional[str] = None

@router.get("/smsleopard/balance", summary="SMS Leopard Check Balance")
async def getleopardbalance(
    credentials: Annotated[str, Depends(get_current_user)],
    x_request_id: Annotated[str | None, Header()] = None
):
    print(f'x-request-id : {x_request_id}')
    respHeaders: Dict = {}
    if x_request_id:
        respHeaders['X-Request-ID'] = x_request_id

    time.sleep(1)
    jsonResponse = {
        "balance": 2897.33,
        "conversion_rate": 1,
        "converted_balance": 2897.33,
        "currency": "KES",
        "pricing_tier_id": None,
        "pricing_tier_name": None
    }
    return JSONResponse(content=jsonResponse, headers=respHeaders, status_code=200)

@router.post("/smsleopard/sms/send", summary="SMS Leopard Send Single SMS")
async def smsleopardSendSingleSMS(req: SMSLeopardSendReq):
    jsonReq = jsonable_encoder(req)
    strPlayload = json.dumps(jsonReq)
    numList = []
    for dest in req.destination:
        numList.append(dest.number)
    logger.info(f'>> /smsleopard/sms/send {req.message}, {numList}, messageId:[{req.message}] >> {strPlayload}')
    unique_id = uuid.uuid4()
    jsonResponse = {
        "success": True,
        "message": "Sent to 1/1. Cost KES 0.30",
        "recipients": [
            {
                "id": str(unique_id),
                "cost": 0.3,
                "number": "+254722799445",
                "status": "queued"
            }
        ]
    }
    if req.status_url:
        asyncio.create_task(processCallback({"messageId": str(unique_id), "callbackUrl": req.status_url}))
    return JSONResponse(content=jsonResponse, status_code=200)

async def processCallback(data: dict):
    # Simulate async work (e.g., DB update, external API call)
    await asyncio.sleep(3)
    dt = datetime.now(timezone.utc)
    timestamp = int(dt.timestamp())
    jsonRequest = {
        "id": data['messageId'],
        "reason": "",
        "status": "DELIVRD",
        "time": timestamp
    }
    response = requests.post(
        data['callbackUrl'],
        json=jsonRequest
    )
    if response.ok:
        logger.info(f"Callback processed messageId:{data['messageId']}, {data} >> status_code: {response.status_code}")
    else:
        logger.error(f"Callback processed messageId:{data['messageId']}, {data} >> status_code: {response.status_code}")
